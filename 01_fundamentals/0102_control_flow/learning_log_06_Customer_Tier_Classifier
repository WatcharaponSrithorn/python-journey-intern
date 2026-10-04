# 📘 Learning Log — 06_Customer_Tier_Classifier.py
<br> "จัดกลุ่ม/จัดระดับข้อมูล" (data classification) ตามเงื่อนไขหลายชั้น
<br> โดยดูจากยอดใช้จ่ายและอายุสมาชิก ข้อมูลนี้มักถูกใช้ต่อใน dashboard หรือระบบการตลาด

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #14 | Customer Tier Classifier | 🟢 Merged | 2026.10.04 17:20 | 2026.10.01 18:14 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.10.04] — Issue #14: [Customer Tier Classifier]
 
### สิ่งที่เรียน / ทำวันนี้
- About `Nested if` `input` `Casting`
- Receive value from user 3 field
- Write Nested if as per rules for business logic main factor is spending 
- if sub need 3+ years and no complaint
- Create tier and reason for readable

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Nested if | การจำลอง "decision tree" แบบง่าย ๆ โดยมีปัจจัยหลักที่จะตรวจสอบก่อน และปัจจัยรองถัดไปในการตรวจสอบตามลำดับ|---|
| Comment | การ Comment ใน Nested if เป็นเรื่องสำคัญมาก เพราะเป็นความซับซ้อนของ "เหตุผลเชิงธุรกิจ" (business logic) จะต้องทำให้สามารถมาอ่านย้อนหลังได้ ถ้ามีการเพิ่มเงื่อนไข เพื่อการปรับปรุง code ได้ง่ายในอนาคต |---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  Comment ใน Nested if
- **สาเหตุ:**  เพราะต้องไม่รู้จะอธิบายยังไงดี เพื่อให้สามารถย้อมมาอ่านได้ในอนาคต
- **วิธีแก้:**   ต้องอธิบายตามเงื่อนไข หลัก ก่อนและค่อย Nested if ลงไปใน if ย่อย
- **วิธีป้องกัน:** -

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> Nested if ถูกต้องครบทุกเงื่อนไข <br> Boundary values ถูกต้อง <br> มีการตรวจสอบค่า Yes/No หรือ yes/no กัน bug
- สิ่งที่ต้องแก้/ปรับปรุง: <br> ยังไม่มี comment อธิบาย "ทำไมต้องซ้อน if" <br> ภาษาอังกฤษประโยค "no has complaint" อ่านแล้วแปลก ๆ <br> Mix การใช้ f-string โดยไม่จำเป็น ให้ใช้แบบเดียวกันทั้งไฟล์เพื่อความสม่ำเสมอ (consistency)
- Insight ที่ได้จาก feedback นี้: <br> comment โค้ดมี nested if หลายชั้น แบบนี้ ความซับซ้อนของ "เหตุผลเชิงธุรกิจ" (business logic) จะต้องทำความเข้าใจ Requirement ว่าอันไหนเป็น ปัจจัยหลัก ต้องเป็น If นอก หรือ If หลัก

### สิ่งที่จะทำต่อ (Next Steps)
- เรียนรู้ `match statement` และจะกลับมา Pracice coding again
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
- Nested if ทำความเข้าใจ Requirement ว่าอันไหนเป็น ปัจจัยหลัก ต้องเป็น If นอก หรือ If หลัก
-  Comment ใน Nested if เป็นเรื่องสำคัญมาก เพราะเป็นความซับซ้อนของ "เหตุผลเชิงธุรกิจ" (business logic) จะต้องทำให้สามารถมาอ่านย้อนหลังได้

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
- "จัดกลุ่ม/จัดระดับข้อมูล" (data classification) ตามเงื่อนไขหลายชั้น ถูกใช้ต่อใน dashboard หรือ การ Analysis
---