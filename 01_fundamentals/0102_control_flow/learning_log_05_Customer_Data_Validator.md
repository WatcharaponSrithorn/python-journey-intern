# 📘 Learning Log — 05_Customer_Data_Validator.py
<br> แปลงข้อมูลลูกค้าเป็น CSV ไปแล้ว แต่ในงานจริง ก่อนข้อมูลจะถูกส่งเข้าระบบ ต้องผ่านการตรวจสอบคุณภาพก่อนเสมอ ไม่งั้นข้อมูลเสีย (bad data) จะเข้าไปปนในฐานข้อมูล แล้วทำให้รายงานหรือการวิเคราะห์ผิดพลาดทั้งระบบ

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #12 | Customer Data Validator | 🟢 Merged | 2026.10.04 10:14 | 2026.10.01 13:36 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.10.04] — Issue #12: [Customer Data Validator]
 
### สิ่งที่เรียน / ทำวันนี้
- About `if` `elif` `else` `Operator` `input` `Casting`
- Receive value from user 4 field
- Write validation rules for each field
- section about validation summary by change data type is Bool
- Create Readable Summary

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Off-by-one error (OBOE) | เวลาเขียนเงื่อนไขช่วงตัวเลข (range) <br>ให้ถามตัวเองเสมอว่า "ค่าขอบ (boundary value) ควรผ่านหรือไม่ผ่าน"|---|
| chaining comparison | แทนที่จะเขียนแยก if/elif สำหรับช่วงตัวเลข ก็แบบใช้ chaining comparison รวมเงื่อนไข `18 <= age <= 100` ทำให้ code สั้นและอ่านง่าย |---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  Off-by-one error (OBOE)
- **สาเหตุ:**  เพราะต้องทำเข้าใจ Requirement ให้ชันเจนตีให้แตก
- **วิธีแก้:**  ถามตัวเองเสมอว่า "ค่าขอบ (boundary value) ควรผ่านหรือไม่ผ่าน" 18 ต้อง ผ่านไหม 100 ต้องผ่านไหม
- **วิธีป้องกัน:** -

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> แยก result_age (string สำหรับคนอ่าน) กับ bool_age (True/False สำหรับโปรแกรมตัดสินใจ) <br> ใช้ ternary if ทำให้โค้ดสั้นลง อ่านง่าย <br> สรุปผลรวมด้วย and ทั้ง 4 ตัวถูกต้อง โดย casting เป็น `bool`
- สิ่งที่ต้องแก้/ปรับปรุง: <br> 1. เงื่อนไข age ผิด (off-by-one error) <br> 2. membership_fee cast ผิด type ตอนแรกใช้เป็น `int` <br> 3. Comment มีจุดสะกด
- Insight ที่ได้จาก feedback นี้: <br> ได้เรียนรู้เรื่อง logical ในการ เขียน codition และ ต้องตรวจสอบ logical ในเรื่องการรับค่า ที่เป็นความจริง membership_fee

### สิ่งที่จะทำต่อ (Next Steps)
- Practice ต่อ About `if` `elif` `else` `Operator` `input` `Casting` เพื่อทำความเข้าใจให้มากยิ่งขึ้น
---

## 🧠 คลัง Concept สะสม (Cheat Sheet ส่วนตัว)

> ย้าย concept สำคัญจากด้านบนมารวมไว้ที่นี่ และเอา คลัง Concept สะสม ของไฟล์ก่อนหน้ามารวม เพื่อไว้อ่านทบทวน

### Python
- พอสามารถที่จะคำสั่ง print() ในรูปแบบ f-string การจัดแนวได้ การตั้งชื่อตัวแปรที่สื่อความหมาย
- การสร้าง Variable เก็บข้อความไว้ก่อน แล้วค่อยนำมาใช้ใน print()จะทำให้ แก้ไข Code จุดเดียว
- Casting ทันทีตอนรับ input
- Decimal ตัวเลขอย่าง เงิน, BMI, หรือคะแนน ควรจะ Used :`.2f`
- Variable อักษรตัวใหญ่ทั้งหมดจะเป็น constants ค่าคงที่
- alignment การจัดคอลัมน์ให้ตรงกัน โดยใช้ `:<15`
- `in` เป็นตัวดำเนินการ (operator) return is True / False ใช้ในการตรวจสอบ สมาชิกภายในนั้น
- Off-by-one error (OBOE) เวลาเขียนเงื่อนไขช่วงตัวเลข (range) ต้องคิดถึงขอบเขตของความต้องการจริงๆๆ
- chaining comparison คือ การรวมเงื่อนไข ทำให้ code สั้นและอ่านง่าย
- Casting value ที่เป็น จำนวนเงิน สมควรที่จะเป็น Data type `float`

### Git / GitHub Workflow
- Git workflow : branch → Coding → ทดสอบรันก่อน commit → Commit → Push → PR → review → merge
- เขียน commit message ให้คนอื่นเข้าใจได้
- Milestone ช่วยบอกว่า sprint นี้ทำอะไร และมีระยะที่กำหนด จะคล้ายที่เรียน Software engineering -> Software process
- commit เช็ค "Current branch" ทุกครั้งก่อน commit

### Data Engineering
- CSV เป็นรูปแบบไฟล์ที่ใช้ส่งข้อมูลระหว่างระบบมากที่สุด
- CSV ต้องระวังเรื่อง comma หลุดเข้าไปในข้อมูล จะทำให้ไฟล์ CSV อ่านผิดคอลัมน์ทันที
- Data Number เก็บข้อมูลต้นฉบับเท่านั้น
- customer_id ควรเก็บเป็น String 
- Data ก่อนข้อมูลจะถูกส่งเข้าระบบ ต้องผ่านการตรวจสอบคุณภาพก่อนเสมอ เพื่อไม่ให้ bad data
---