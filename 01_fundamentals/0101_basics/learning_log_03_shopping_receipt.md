# 📘 Learning Log — 03_shopping_receipt.py
<br> โปรแกรมที่ใกล้งานจริงมากขึ้น คือคำนวณใบเสร็จร้านค้า ต้องรับข้อมูลสินค้าหลายอย่าง คำนวณราคารวม บวกภาษี แล้วแสดงผลเหมือนใบเสร็จจริง

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #7 | Shopping Receipt Calculator | 🟢 Merged | 2026.09.29 | 2026.09.30 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.09.29] — Issue #7: [Shopping Receipt Calculator]
 
### สิ่งที่เรียน / ทำวันนี้
- The program must get info for 3 items. For each item, ask for: item name, price per unit, quantity
- Calculate the subtotal for each item: price × quantity
- Sum subtotal of 3 items
- Calculate tax vat 
- Calculate Total (Subtotal + Tax)
- Display the result as a readable receipt.
- Don't use a loop for unlimited items


### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| alignment | การจัดคอลัมน์ให้ตรงกัน สำคัญมากในงานจริง ฝึก `:<15`, `:>10` อาจจะใช้ในงาน data |---|
| floating point error | ตัวเลขเงินต้องปัดเสมอ ไม่ปล่อยทศนิยมยาว |---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:** -
- **สาเหตุ:** -
- **วิธีแก้:**  -
- **ผลลัพธ์:** -

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br>Calculation logic is correct <br> reused the pattern from Issue #2 nested f-string, nice header
- สิ่งที่ต้องแก้/ปรับปรุง: <br>quantity should be int, not float <br> Money numbers are not rounded to 2 decimal places <br> Typo <br> Column alignment could be clearer using : `<15` or `:>10` replace `\t` <br> `VAT = 7` then /100 — a small style note should use `VAT = 0.07`
- Insight ที่ได้จาก feedback นี้: <br> เรื่องคำศัพท์ภาษาอังกฤษที่ยังอ่อน brเข้าใจเรื่องการตั้งชื่อ Variable มากขึ้น
### สิ่งที่จะทำต่อ (Next Steps)
- ฝึกเรื่องการ logical ของสายงาน Data Engineer อีก 1 Issues โดยแค่ใช้ความรู้ ที่ทบทวนใน 0101_basic 
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

### Git / GitHub Workflow
- Git workflow : branch → Coding → ทดสอบรันก่อน commit → Commit → Push → PR → review → merge
- เขียน commit message ให้คนอื่นเข้าใจได้
- Milestone ช่วยบอกว่า sprint นี้ทำอะไร และมีระยะที่กำหนด จะคล้ายที่เรียน Software engineering -> Software process
---
