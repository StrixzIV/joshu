#Import Library
import json
import os
from flask import Flask
from flask import request
from flask import make_response
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Flask
app = Flask(__name__)
@app.route('/', methods=['POST']) 

def MainFunction():

    #รับ intent จาก Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(answer_from_bot)
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
        print("="*10,'food share worked')
    elif intent_group_question_str == 'pm25':
        answer_str = pm25()
        print("="*10,'pm25 worked')
    elif intent_group_question_str == 'สภาพอากาศ':
        answer_str = tem()
        print("="*10,'tem worked')
    elif intent_group_question_str == 'iot':
        answer_str = iot_sta()
        print("="*10,'iot worked')
    elif intent_group_question_str == 'iot sl':
        answer_str = iot_sl(question_from_dailogflow_dict)
        print("="*10,'iot sl worked')
    else: answer_str = "ผมไม่เข้าใจ คุณต้องการอะไร"

    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot

def food_share(respond_dict): #ฟังก์ชั่นสำหรับแชร์ค่าอาหาร
    total = float(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["total.original"])  #respond_dict
    n = float(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["n.original"])
    
    answer_function = '%.2f' %(total/n)     #2 ทศนิยม
    return answer_function  

def pm25() : #ฟังก์ชั่นสำหรับแสดงผล pm2.5 pm25
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
    answer_function = " ".join(str(x) for x in output_tuple)
    return answer_function  


def tem() : #ฟังก์ชั่นสำหรับแสดงผลสภาพอากาศ
    url = 'http://www.metalarm.tmd.go.th/monitor/media'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # find the div with class "view_media_desc"
    div = soup.find('div', {'class': 'view_media_desc'})

    answer_function = div.text
    return answer_function

# Initialize Firebase Admin SDK
cred = credentials.Certificate("D:\\tatsukere\\final-test-bf8f8-firebase-adminsdk-qk61i-36963744fa.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://final-test-bf8f8-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
# Read data from the Realtime Database
ref = db.reference('/')
data = ref.get()

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
    answer_function = '\n'.join(data_list)
    
    return answer_function

def iot_sl(respond_dict):  
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
    answer_function = f'{sl_sta} {sl_value}'
    return answer_function

#Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
