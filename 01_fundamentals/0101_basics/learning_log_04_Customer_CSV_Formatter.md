# 📘 Learning Log — 04_Customer_CSV_Formatter.py
<br> Data Engineer ส่วนหนึ่งคือ รับข้อมูลดิบ (raw data) แล้วแปลงให้อยู่ในรูปแบบมาตรฐาน ก่อนส่งเข้าระบบฐานข้อมูลหรือไฟล์ เช่น CSV (Comma-Separated Values)
โปรแกรมรับข้อมูลลูกค้า แล้วแปลงเป็น 1 แถว CSV ที่พร้อมนำไปใช้ในระบบอื่นได้จริง

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #9 | Customer Data to CSV Row Formatter
 | 🟢 Merged | 2026.10.01 | 2026.10.01 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.10.01] — Issue #9: [Customer Data to CSV Row Formatter]
 
### สิ่งที่เรียน / ทำวันนี้
- Ask the user for 6 fields of customer data
- Must not have comma (,) 
- Convert the 6 fields into ONE CSV row, separated by commas, and show it 2 ways: Header + Data , Readable Summary
- In real work, we usually don't round numbers when saving to CSV — we keep the original precision. Rounding is only for display purposes.


### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| CSV | CSV เป็นรูปแบบไฟล์ที่ใช้ส่งข้อมูลระหว่างระบบมากที่สุด เพราะเปิดได้ทั้ง Excel, database|---|
| Data | เก็บข้อมูลต้นฉบับให้แม่นยำที่สุด ปัดเลขแค่ตอนแสดงผล |---|
| customer_id | เก็บเป็น string เพราะเป็น Primary Key ตามหลัก ระบบฐานข้อมูลไม่ได้นำไปคำนวณ |---|
| CSV | ต้องระวังเรื่อง comma หลุดเข้าไปในข้อมูล จะทำให้ไฟล์ CSV อ่านผิดคอลัมน์ทันที |---|
| `in` | เป็นตัวดำเนินการ (operator) ที่ใช้เช็คว่า "มีสิ่งนี้อยู่ข้างในสิ่งนั้นไหม" return `bool` |---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  เผลอ commit ไปที่ main
- **สาเหตุ:**  ลืมสลับไป branch feature-0101-basic
- **วิธีแก้:**  ทำการ Revest -> Push origin การ Revert ขึ้น GitHub -> เลือก Branch ใหม่ -> เขียนไฟล์ 04_Customer_CSV_Formatter.py ใหม่ 
- **วิธีป้องกัน:** - เช็ค "Current branch" ทุกครั้งก่อน commit

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> has_comma = "," `in` full_name ใช้ in ถูกต้อง และ comment อธิบายดี <br> CSV row เก็บค่าดิบ ไม่ปัดทศนิยม ส่วน Summary ปัดด้วย .2f <br> แยกตัวแปรข้อความ (display_1, display_2, ...) ไว้ด้านบน อ่านง่าย แก้ไขง่าย
- สิ่งที่ต้องแก้/ปรับปรุง: Typo ในชื่อตัวแปร <br> ต้องใช้ Nested f-string แบบเดียวกับที่เคยแก้ใน Issue #1 เช็คตัวเองก่อนส่งงานว่า "มี f-string ซ้อน quote เดียวกันไหม" <ข้อความ prompt ยาวไปนิดและอ่านสับสน> 
- Insight ที่ได้จาก feedback นี้: <br> มีความเข้าใจเรื่อง CSV row เก็บค่าดิบ <br> แยก Variable อ่านง่าย แก้ไขง่าย <br> การใช้ `in` ค่าที่ได้จะเป็นแค่ True / False ถ้าทบวนเรื่อง `if` จะทำให้สมบูรณ์ยิ่งขึ้น
### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรื่องของ 0102. Control Flow ต่อเพื่อกลับมา Practice coding ต่อ
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
- `in` เป็นตัวดำเนินการ (operator) return is True / False 

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
---