# 📘 Learning Log — 08_API_Pagination_Simulator.py
<br> งานนี้จะจำลองสถานการณ์ดึงข้อมูลจาก API ที่แบ่งส่งเป็น "หน้า" (page) โดยใช้ while loop วนดึงข้อมูลไปเรื่อย ๆ จนกว่าจะไม่มีข้อมูลเหลือ

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #19 | API Pagination Simulator | 🟢 Merged | 2026.10.08 23:28 | 2026.10.09 01:44 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.10.08] — Issue #19: [API Pagination Simulator]
 
### สิ่งที่เรียน / ทำวันนี้
- Simulate the total number of records in the system with a fixed constant
- Use a while loop to fetch data page by page
- Add a safety counter: stop the loop if it runs too many times and protect bug


### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| infinite loop | Safety Counter ป้องกัน infinite loop ใส่ "ทางออกฉุกเฉิน" ไว้เสมอ ไม่ว่าจะเป็นตัวนับรอบ |---|
| Summary | ถ้าดำเนินการยังไม่สำเร็จและ Safety Counter สิ้นสุด ควจจะมีบอก Status เพื่อให้ คนอ่านผลสรุปจะไม่เข้าใจผิดว่าสำเร็จ เป็นเรื่องสำคัญในการดึงข้อมูลแปลว่า ข้อมูลยังไม่ครบแล้วนำไปใช้เลย |---|
| boundary test | ทดสอบ ค่าขอบ ด้วยเลข 1000 กับ 1009 |---|


### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  Status Summary ไม่ได้มีการทำ การโชว์ Status ว่า ยังดำเนินการยังไม่สำเร็จจาก Safety Counter สิ้นสุด
- **สาเหตุ:**  ลืมคิดในส่วนที่ต้องแสดงสถานะ หาก ระบบยังดำเนินการยังไม่สำเร็จ
- **วิธีแก้:**   สร้าง feature เพิ่มในส่วน # section summary ใช้ if ในการตรวจสอบ safety_counter เพราะว่า variable  นี้จะ +1 ก็ไปเช็คเงื่อนไข ในการ break loop ซึ่งถ้ามากกว่า แปลว่าระบบยังมีข้อมูลให้ดึงต่อ แต่ถึงสุดขีดจำกัดของระบบแล้ว
- **วิธีป้องกัน:** หากระบบมีการกำหนด ขีดจำกัด ในการทำงาน เราจะต้องมี feature ที่แสดงสถานะ ของการทำงานระบบ

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br>while records_fetched < TOTAL_RECORDS ถูกต้อง และมี safety counter <br> ตั้งชื่อ constant เป็นตัวพิมพ์ใหญ่ ตาม PEP8 <br>ทดสอบด้วยค่า 1005 ซึ่งเป็นค่า edge case ที่น่าสนใจ
- สิ่งที่ต้องแก้/ปรับปรุง: <br> Summary ตอนนี้ไม่บอกเลยว่าดึงไม่ครบ ถ้าโปรแกรมชนขีดจำกัด คนอ่านผลสรุปจะเข้าใจผิดว่าสำเร็จ <br> Comment ยังไม่ครบ "ทำไมต้องมี safety counter" 
- Insight ที่ได้จาก feedback นี้: <br> ใช้ while กับเงื่อนไขหยุด และใส่ safety counter ป้องกัน infinite loop <br> ต้องทดสอบ ค่าขอบ (boundary) ด้วยเลข 1000 กับ 1009 <br> ให้ Summary บอกสถานะ Complete / Incomplete ชัดเจน
 
### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `For looop` และจะกลับมา Pracice coding again
---

## 🧠 คลัง Concept สะสม (Cheat Sheet ส่วนตัว)

> ย้าย concept สำคัญจากด้านบนมารวมไว้ที่นี่ และเอา คลัง Concept สะสม ของไฟล์ก่อนหน้ามารวม เพื่อไว้อ่านทบทวน

### Python
- พอสามารถที่จะคำสั่ง print() ในรูปแบบ f-string การจัดแนวได้ `:^50`, `:<50`การตั้งชื่อตัวแปรที่สื่อความหมาย
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
- Comment ใน Nested if เป็นเรื่องสำคัญมาก เพราะเป็นความซับซ้อนของ "เหตุผลเชิงธุรกิจ" (business logic) จะต้องทำให้สามารถมาอ่านย้อนหลังได้
- Comment ควรอยู่ "เหนือโค้ดที่ซับซ้อน" ไม่ใช่ "ท้ายทุกบรรทัด"
- หลัง `or` ไม่ควรใส่ String เฉย เพราะค่าจะเป็น True เสมอ
- `while` loop ควรจะสร้าง Safety Counter เพื่อป้องกัน infinite loop

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
- การแยก นามสกุลไฟล์ จะสามารถช่วยในการนำไปดำเนินการต่อได้งานขึ้น
- Summary ควจมีเงื่อนไขในการเช็ค ทั้งหมดว่าทำสำเร็จครบทุกส่วน เพื่อป้องกันการเข้าใจผิด เพราะการนำข้อมูลที่ไม่ครบหรือไม่สมบูรณ์ ไปใช้ต่อไม่สมควร
---