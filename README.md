# LINE Chatbot for alive and IoT Device Control

โครงการนี้เกี่ยวกับการสร้าง Line chatbot ที่สามารถควบคุมอุปกรณ์ IoT โดยใช้ Dialogflow เป็นเครื่องมือประมวลผลภาษาธรรมชาติ แชทบอทสามารถรับคำสั่งภาษาธรรมชาติจากผู้ใช้ ตีความโดยใช้ Dialogflow และควบคุมอุปกรณ์ IoT 

โครงการนี้ใช้ LINE Chatbot โดยใช้ Python Flask และ Firebase Realtime Database แชทบอทสามารถรับข้อความจากผู้ใช้และส่งการตอบกลับตามข้อมูลที่ผู้ใช้ป้อน

แชทบอทออกแบบมาเพื่อควบคุมอุปกรณ์ IoT ที่เชื่อมต่อกับ Firebase Realtime Database ผู้ใช้สามารถส่งคำสั่งไปยังแชทบอทเพื่อควบคุมอุปกรณ์ เช่น เปิด/ปิดไฟ 
จากนั้นแชทบอทจะส่งคำสั่งที่เกี่ยวข้องไปยัง Firebase Realtime Database ซึ่งอุปกรณ์ IoT จะได้รับและดำเนินการตามที่ต้องการ นอกจากนั้นยังมีการ แสดงอุณหภูมิ ฝุ่น pm 2.5 โดยจะนำข้อมูลจากตัวหน้าเว็ป aqicn มาใช้งาน
รวมถึงโปรแกรมสำหรับหารค่าอาหาร

## ความต้องการ
Python 3.x
Flask
Firebase Admin SDK
Line Messaging API
Ngrok

## เริ่มต้นใช้งาน
1. โคลนที่เก็บนี้ไปยังเครื่องของคุณ
2. สร้างโปรเจ็กต์ Firebase ใหม่และเพิ่ม Firebase Realtime Database ให้กับโปรเจ็กต์
3. ดาวน์โหลดคีย์ส่วนตัว Firebase Admin SDK และบันทึกไว้ในไดเร็กทอรีโครงการ
4. สร้างช่อง LINE Messaging API ใหม่และกำหนดค่า URL ของเว็บฮุคให้ชี้ไปที่ ngrok URL
5. ติดตั้งแพ็คเกจ Python ที่จำเป็นโดยใช้ pip
6. เริ่ม ngrok และเปิดเผยแอป Flask บนอินเทอร์เน็ต
7. เริ่มแอป Flask โดยใช้ python app.py
8. เพิ่ม LINE Chatbot เป็นเพื่อนและเริ่มแชทได้เลย!

## การตั้งค่าโครงการ
ในการตั้งค่าโครงการ คุณจะต้องทำตามขั้นตอนเหล่านี้:

1. สร้างช่อง Line Bot และรับ Channel Access Token และ Channel Secret
2. สร้าง Dialogflow และกำหนดค่าความตั้งใจและเอนทิตีสำหรับการควบคุมอุปกรณ์ IoT
3. ตั้งค่าโปรเจ็กต์ Firebase และสร้างอินสแตนซ์ฐานข้อมูลเรียลไทม์
4. ตั้งค่าสภาพแวดล้อมการพัฒนา Python และติดตั้งแพ็คเกจที่จำเป็น (Flask, คำขอ, firebase-admin เป็นต้น)
5. เขียนโค้ด Python สำหรับแบ็กเอนด์ของแชทบอทและปรับใช้กับเซิร์ฟเวอร์หรือแพลตฟอร์มคลาวด์
6. ตั้งค่าเว็บฮุคเพื่อรับข้อความ Line และประมวลผลโดยใช้แบ็กเอนด์แชทบอท
7. เชื่อมต่อแบ็กเอนด์ของ Chatbot กับ Dialogflow API และ Firebase Realtime Database โดยใช้ข้อมูลประจำตัวที่เหมาะสม


## การใช้งาน
ปัจจุบัน chatbot รองรับคำสั่งต่อไปนี้:

* เปิดหรือปิด: เปิด/ปิดอุปกรณ์ 
* รับค่าปัจจุบันของอุปกรณ์
* แสดงอุณหภูมิ ฝุ่น pm 2.5 และ โปรแกรมสำหรับหารค่าอาหาร

ผู้ใช้สามารถส่งคำสั่งไปยังแชทบอทและแชทบอทจะส่งคำสั่งที่เกี่ยวข้องไปยัง Firebase Realtime Database อุปกรณ์ IoT จะรับคำสั่งและดำเนินการตามที่ต้องการ

## งานในอนาคต
เพิ่มการสนับสนุนสำหรับอุปกรณ์ IoT เพิ่มเติม
ใช้การรับรองความถูกต้องและการอนุญาตสำหรับผู้ใช้
ปรับปรุงความสามารถในการประมวลผลภาษาธรรมชาติของแชทบอท

## อ้างอิง
- [python linechatbot]([https://flask.palletsprojects.com/](https://www.youtube.com/playlist?list=PLeohJaMRzYHohBzFbKJknovLFmQGwbBS-))
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Firebase Realtime Database Documentation](https://firebase.google.com/docs/database)
- [Firebase Admin SDK Documentation](https://firebase.google.com/docs/admin/setup)
- [Line Messaging API Documentation](https://developers.line.biz/en/docs/messaging-api/overview/)
- [Ngrok Documentation](https://ngrok.com/docs)



