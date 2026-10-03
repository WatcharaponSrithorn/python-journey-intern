# 📘 Learning Log — 02_BMI_Calculator.py
<br> สร้างโปรแกรมเล็ก ๆ ที่รับข้อมูลจากผู้ใช้ (user input) แล้วนำไปคำนวณ ไม่ใช่แค่ print ข้อความตายตัวเหมือนงานก่อนหน้า

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #3 | BMI Calculator | 🟢 Merged | 2026.09.28 | 2026.09.29 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.09.28] — Issue #3: [BMI Calculator]
 
### สิ่งที่เรียน / ทำวันนี้
- The program must ask the user for 2 values using `input()` by weight in kg, height in meters
- Cast the input values to `float`, because `input()` always returns a `str`.
- Formula   `BMI = weight ÷ (height × height)` 
- Using f-string, rounded to 2 decimal places with `:.2f`
- By Don't use `if`


### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Label | ไม่สร้าง label ซ้ำซ้อนกัน ที่ความหมายเหมือนกัน |---|
| UI | UI ที่ไม่เหมือนคู่มือหรือที่คนอื่นบอก ให้ ถ่าย screenshot แล้วถามทีม |[Label](../../source_image/no-have-new-label.webp)|
| Milestone | Description ของ Milestone ช่วยให้คนที่เพิ่งเข้าทีมเปิดมาดูแล้วเข้าใจทันทีว่า sprint นี้เน้นอะไร |---|
| Casting | Cast ทันทีตอนรับ input ไม่ใช่ทีหลัง |---|
| Decimal | ตัวเลขอย่าง เงิน, BMI, หรือคะแนน ถ้าไม่ปัด จะได้ทศนิยมยาวเป็นสิบตำแหน่ง |---|
| input() | ข้อความใน input() ควรบอกหน่วยเสมอ ลดโอกาส error จากคนกรอกผิดหน่วย|---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:** Labels ใน GitHub ไม่สามารถเพิ่มได้ และ Milestone ก็เหมือนกัน
- **สาเหตุ:** น่าจะเกิดจาก UI ของทาง GitHub ตอนนั้นเกิด Bug (ตามตวามเข้าใจ)
- **วิธีแก้:**  กด Feedback Preview และถาม AI เพิ่มเติม เพื่อดูวิธีที่จะเพิ่ม Labels, Milestone
- **ผลลัพธ์:** Labels จะเพิ่ม สามารถ ใส่คนว่า create ในช่องค้นหา จะขึ้น New Lable ส่วน Milestone ใส่คำว่า /new ในช่อง URL ต่อท้าย กด Enter จะขึ้น UI เป็น Create milestone

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br>Cast `input()` to float in the same line. This is a good habit. <br>The BMI formula is correct <br> Used :`.2f` Correct!
- สิ่งที่ต้องแก้/ปรับปรุง: <br>Typo in variable name <br> Variable name should be lowercase because `BMI` will values that never change (constants)
- Insight ที่ได้จาก feedback นี้: <br> เรื่องคำศัพท์ภาษาอังกฤษที่ยังอ่อน เข้าใจเรื่องการตั้งชื่อ Variable มากขึ้น
### สิ่งที่จะทำต่อ (Next Steps)
- ฝึกเรื่องการ coding print + comment input + casting + f-string format ให้มากขึ้น อีก 1 Issues
---

## 🧠 คลัง Concept สะสม (Cheat Sheet ส่วนตัว)

> ย้าย concept สำคัญจากด้านบนมารวมไว้ที่นี่ เพื่อทบทวนก่อนสัมภาษณ์

### Python
- พอสามารถที่จะคำสั่ง print() ในรูปแบบ f-string การจัดแนวได้ การตั้งชื่อตัวแปรที่สื่อความหมาย
- การสร้าง Variable เก็บข้อความไว้ก่อน แล้วค่อยนำมาใช้ใน print()จะทำให้ แก้ไข Code จุดเดียว
- Casting ทันทีตอนรับ input
- Decimal ตัวเลขอย่าง เงิน, BMI, หรือคะแนน ควรจะ Used :`.2f`
- Variable อักษรตัวใหญ่ทั้งหมดจะเป็น constants ค่าคงที่

### Git / GitHub Workflow
- Git workflow : branch → Coding → ทดสอบรันก่อน commit → Commit → Push → PR → review → merge
- เขียน commit message ให้คนอื่นเข้าใจได้
- Milestone ช่วยบอกว่า sprint นี้ทำอะไร และมีระยะที่กำหนด จะคล้ายที่เรียน Software engineering -> Software process
---
