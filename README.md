# LINE Chatbot for alive and IoT Device Control

![joshu](https://user-images.githubusercontent.com/104154862/233819991-05188dc3-0275-4604-932b-89e9f80a0391.jpg)

โครงการนี้เกี่ยวกับการสร้าง Line chatbot ที่สามารถควบคุมอุปกรณ์ IoT โดยใช้ Dialogflow เป็นเครื่องมือประมวลผลภาษาธรรมชาติ แชทบอทสามารถรับคำสั่งภาษาธรรมชาติจากผู้ใช้ ตีความโดยใช้ Dialogflow และควบคุมอุปกรณ์ IoT

โครงการนี้ใช้ LINE Chatbot โดยใช้ Python Flask และ Firebase Realtime Database แชทบอทสามารถรับข้อความจากผู้ใช้และส่งการตอบกลับตามข้อมูลที่ผู้ใช้ป้อน

แชทบอทออกแบบมาเพื่อควบคุมอุปกรณ์ IoT ที่เชื่อมต่อกับ Firebase Realtime Database ผู้ใช้สามารถส่งคำสั่งไปยังแชทบอทเพื่อควบคุมอุปกรณ์ เช่น เปิด/ปิดไฟ
จากนั้นแชทบอทจะส่งคำสั่งที่เกี่ยวข้องไปยัง Firebase Realtime Database ซึ่งอุปกรณ์ IoT จะได้รับและดำเนินการตามที่ต้องการ นอกจากนั้นยังมีการ สภาพอากาศ ฝุ่น pm 2.5 โดยจะนำข้อมูลจาก กรรมอุตุ และ aqicn มาใช้งาน
รวมถึงโปรแกรมสำหรับหารค่าอาหาร

## Requirements

* Python 3.7+
* Flask
* Firebase Admin SDK
* Line Messaging API
* Ngrok
* Git

## เริ่มต้นใช้งาน

1. Clone github repo ลงเครื่อง
2. สร้างโปรเจ็กต์ Firebase ใหม่และเพิ่ม Firebase Realtime Database ให้กับโปรเจ็กต์
3. ดาวน์โหลดคีย์ส่วนตัว Firebase Admin SDK และบันทึกไว้ในไดเร็กทอรีโครงการ
4. สร้างช่อง LINE Messaging API ใหม่และกำหนดค่า URL ของเว็บฮุคให้ชี้ไปที่ ngrok URL
5. ติดตั้งแพ็คเกจ Python ที่จำเป็นโดยใช้ pip
6. เริ่ม ngrok และเปิดเผยแอป Flask บนอินเทอร์เน็ต
7. เริ่มแอป Flask โดยใช้ python app.py
8. เพิ่ม LINE Chatbot เป็นเพื่อนและเริ่มแชทได้เลย!

## Setup

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
* แสดสภาพอากาศ ฝุ่น PM 2.5 และ โปรแกรมสำหรับหารค่าอาหาร

ผู้ใช้สามารถส่งคำสั่งไปยังแชทบอทและแชทบอทจะส่งคำสั่งที่เกี่ยวข้องไปยัง Firebase Realtime Database อุปกรณ์ IoT จะรับคำสั่งและดำเนินการตามที่ต้องการ

## งานในอนาคต

เพิ่มการสนับสนุนสำหรับอุปกรณ์ IoT เพิ่มเติม
ใช้การรับรองความถูกต้องและการอนุญาตสำหรับผู้ใช้
ปรับปรุงความสามารถในการประมวลผลภาษาธรรมชาติของแชทบอท

## อ้างอิง

* [Tutorial](https://www.youtube.com/playlist?list=PLeohJaMRzYHohBzFbKJknovLFmQGwbBS-)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Firebase Realtime Database Documentation](https://firebase.google.com/docs/database)
* [Firebase Admin SDK Documentation](https://firebase.google.com/docs/admin/setup)
* [Line Messaging API Documentation](https://developers.line.biz/en/docs/messaging-api/overview/)
* [Ngrok Documentation](https://ngrok.com/docs)

## ตัวอย่างการใช้งาน

![Untitled-1](https://user-images.githubusercontent.com/104154862/233785189-f91af317-f07d-464c-bce1-89c7f77bfa32.jpg)
![Untitled-2](https://user-images.githubusercontent.com/104154862/233785015-b9d832fb-b5a5-4250-8993-6ead6117b52e.jpg)
