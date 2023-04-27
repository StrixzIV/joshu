import os
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, make_response

import firebase_admin
from firebase_admin import db, credentials

# Initialize
app = Flask(__name__)

cred = credentials.Certificate("./firebase-adminsdk.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'Your database URL'
})

# Read data from the Realtime Database
ref = db.reference('/')
data = ref.get()

@app.route('/', methods=['POST']) 
def joshu_api():

    #รับ intent จาก Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    bot_answer = generating_answer(question_from_dailogflow_raw)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(bot_answer)
    r.headers['Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป

    return r


def generating_answer(question_from_dailogflow_dict):

    #Print intent ที่รับมาจาก Dailogflow
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #เก็บต่า ชื่อของ intent ที่รับมาจาก Dailogflow
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"]

    #ลูปตัวเลือกของฟังก์ชั่นสำหรับตอบคำถามกลับ
    if intent_group_question_str == 'food share':
        answer_str = food_share(question_from_dailogflow_dict)
        print(f'{"="*10} food share worked')

    elif intent_group_question_str == 'pm25':
        answer_str = pm25()
        print(f'{"="*10} PM 2.5 worked')

    elif intent_group_question_str == 'สภาพอากาศ':
        answer_str = tem()
        print(f'{"="*10} tem worked')
        
    elif intent_group_question_str == 'iot':
        answer_str = iot_sta()
        print(f'{"="*10} IoT worked')

    elif intent_group_question_str == 'iot sl':
        answer_str = iot_sl(question_from_dailogflow_dict)
        print(f'{"="*10} IoT sl worked')

    else: 
        answer_str = "ผมไม่เข้าใจ คุณต้องการอะไร"

    #สร้างการแสดงของ dict 
    bot_answer = {"fulfillmentText": answer_str}
    
    #แปลงจาก dict ให้เป็น JSON
    bot_answer = json.dumps(bot_answer, indent=4) 
    
    return bot_answer


def food_share(respond_dict: dict) -> str: 
    
    '''
        ฟังก์ชั่นสำหรับแชร์ค่าอาหาร
    '''
    
    total = float(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["total.original"])  #respond_dict
    n = float(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["n.original"])
    
    result = f'{(total/n):.2f}' #2 ทศนิยม
    return result


def pm25() -> str: 
    
    '''
        ฟังก์ชั่นสำหรับแสดงผล PM 2.5
    '''
    
    pm_url = 'https://aqicn.org/city/beijing/'
    pm_response = requests.get(pm_url)

    soup = BeautifulSoup(pm_response.content, 'html.parser')
    aqi_element = soup.find('div', {'class': 'aqivalue'})

    if aqi_element:
        aqi_value = aqi_element.text.strip()
        info_element = soup.find('div', {'id': 'aqiwgtinfo'})

        if info_element:
            info_text = info_element.text.strip()
        else:
            print("Information element not found.")
    else:
        print("AQI element not found.")
    output_tuple = aqi_value,info_text
    result = " ".join(str(x) for x in output_tuple)
    return result  


def tem() -> str: 
    
    '''
        ฟังก์ชั่นสำหรับแสดงผลสภาพอากาศ
    '''
    
    url = 'http://www.metalarm.tmd.go.th/monitor/media'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # find the div with class "view_media_desc"
    div = soup.find('div', {'class': 'view_media_desc'})
    result = div.text
    
    return result


def iot_sta():  #ฟังก์ชั่นสำหรับแสดงผล iot
    ref_sta = db.reference('/')
    data_sta = ref_sta.get()
    key_map = {
        'l_1': 'ไฟดวงที่1',
        'l_2': 'ไฟดวงที่2',
    }
    data_list = []
    for key, value in data_sta.items():
        if key in key_map:
            data_list.append(f"{key_map[key]} {value}")
    result = '\n'.join(data_list)
    
    return result


def iot_sl(respond_dict: dict) -> str:  
    
    sl_value = str(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["value.original"])   #sl_value, sl_sta
    sl_sta = str(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["sta.original"])
    
    key_map_sl = {
        'ดวงที่1': 'l_1',
        'ดวงที่2': 'l_2',
        'เปิด': 'ON',
        'ปิด': 'OFF'
    }
    
    db_key = key_map_sl[sl_value]
    db_value = key_map_sl[sl_sta]
    
    ref.update({db_key: db_value})
    
    result = f'{sl_sta} {sl_value}'
    return result


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
