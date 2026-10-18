# 📘 Learning Log — 12_Sales_Row_Tuple_Validator.py
<br> ทีม Sales ส่งข้อมูลยอดขายมาเป็น "แถว" (row) แต่ละแถวเก็บเป็น tuple บางแถวผิดรูปแบบ บางแถวตัวเลขผิด บางแถวซ้ำ งานคือตรวจทีละแถว แยกแถวที่ดีกับแถวที่ผิด และบอก เหตุผล ที่ปฏิเสธ

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ

---

## สรุปภาพรวม (Progress Tracker)

| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #28 | Sales Row Tuple Validator | 🟢 Merged | 2026.10.17 18:53 | 2026.10.18 00:14 |

สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked

---

## 📅 [2026.10.15] — Issue #25: [Order ID Batch Cleaner]

### สิ่งที่เรียน / ทำวันนี้
- Sales data comes as rows is Tuple
- for loop each row and get the row number and data
- Check that each row has 4 items before unpacking if invalid will `reason_reject`
- Check Order ID must start with "ORD-" if invalid will `reason_reject`
- Check Quantity must be more than 0 if invalid will `reason_reject`
- Price must be more than 0 if invalid will `reason_reject`
- Separate valid rows from invalid rows by check `reason_reject` if valid Calculate total and Grand total then find the top order
- If the list is empty, show a message and stop.
- If there are no valid rows, display "No valid orders found"

### 🧰 What I used
- Tuple
- `for` loop and `enumerate()`
- `if..else`
- String method `.startswith()`
- list method `.append()`


### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Tuple = one record, list = many records. | ในงานจริง ฐานข้อมูลส่งข้อมูลกลับมาเป็น list ของ tuple เช่น `sqlite3` ใช้ `fetchall()` |---|
| Check the shape before you unpack. | unpack tuple ที่จำนวนช่องไม่ตรงจะเกิด ValueError และสคริปต์ล้มทั้งงาน |---|
| Always say why. | แถวที่ถูกปฏิเสธต้องมีเหตุผลบอก ทีม Data ต้องไปแก้ที่ต้นทางได้ |---|
| Do not change the source data. | อย่าแก้ tuple เดิม ให้สร้างอันใหม่ (นี่คือเหตุผลที่ tuple ปลอดภัย) |---|


### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  Top order Logigal ผิด
- **สาเหตุ:**  loop `for item in list_total` วนแค่ ตัวเลข ไม่มี Order ID ที่คู่กัน แล้วไปใช้ order_id จาก loop
- **วิธีแก้:**   เพิ่ม Unpacking ต่อภายใน Loop แล้วค่อยนำ order_id ไปเก็บใน top_order ทุกครั้งหลังการเช็ค ยอด total ที่มากกว่ายอดเก่า

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> `reason_reject = ""` อยู่ใน loop ไม่มีเหตุผลค้างจากรอบก่อน <br> ตั้ง elif เช็ก "ซ้ำ" เป็นข้อสุดท้าย และเพิ่ม ID เฉพาะแถวที่ผ่านทุกข้อ <br> จัดการ rows ว่างได้ถูกต้อง (No rows to check) <br> ชื่อ label_... สม่ำเสมอทั้งไฟล์ <br> ใช้ :<10, :.2f จัดตารางอ่านง่าย
- สิ่งที่ต้องแก้/ปรับปรุง: <br> Order ID ผิด (ค่าเก่าค้างอีกแล้ว) เป็นค่าเก่าจากแถวที่ 4 นี่คือบั๊ก “stale value” <br> Top order คำนวณผิดเมื่อแถวที่ยอดสูงสุดไม่ใช่แถวสุดท้าย <br> ไม่ได้ `.sort()`
- Insight ที่ได้จาก feedback นี้: <br> 1. อย่าใช้ตัวแปรที่มาจาก loop ก่อนหน้าโดยไม่ตรวจสอบ Scope และค่าเดิม ดังนั้นควรใช้ข้อมูลจาก source ที่แน่นอน เช่น item[0] แทนตัวแปรที่อาจไม่มีค่า <br> 2. การทดสอบที่ผ่าน ไม่ได้แปลว่า Logic ถูกต้อง ควรออกแบบ Test Case ให้เปลี่ยนตำแหน่งของข้อมูลสำคัญ ที่มีความหลากหลาย

### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `Set` และจะกลับมา Pracice coding again
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
- ตั้งตัวแปรสะสม ก่อน เข้า loop และอัปเดตด้วย +=
- `.strip()` ก็การลบ spacebar หน้าและหลังข้อมูลออก
- `.split()` คือการแยก ข้อมูลออกโดยยึด ช่องว่าง หรือ ข้อมูลที่ระบุภายใน วงเล็บ Retrun เป็น List
- ระวังการใช้ `.find('@')`คืน -1
- `.title()` เป็นการทำให้ ตัวอักษรแรกของคำตัวใหญ่
- `.remove()` ลบ ตัวแรก ใน list
- `sort()` ค่าที่ sort จะเปลี่ยนไปทันที แต่ถ้าต้องการ เก็บค่าเดิม ให้ใช้ `variable_new = sorted(unique_ids)`
- `tuple` unchangeable และ  อย่าแก้ tuple เดิม ให้สร้างอันใหม่
- `unpack tuple` จำนวนช่องจะต้อง ตรงกับ variable เท่านั้น ดังนั้น ก่อน `unpack` ควจเช็ค len(tuple) ก่อนเสมอ เพื่อป้องกัน `ValueError`

### Git / GitHub Workflow
- Git workflow : branch → Coding → ทดสอบรันก่อน commit → Commit → Push → PR → review → merge
- เขียน commit message ให้คนอื่นเข้าใจได้
- Milestone ช่วยบอกว่า sprint นี้ทำอะไร และมีระยะที่กำหนด จะคล้ายที่เรียน Software engineering -> Software process
- commit เช็ค "Current branch" ทุกครั้งก่อน commit
- One Issue, one PR. อย่าแอบแก้เรื่องอื่นใน PR เดียวกัน

### Data Engineering
- CSV เป็นรูปแบบไฟล์ที่ใช้ส่งข้อมูลระหว่างระบบมากที่สุด
- CSV ต้องระวังเรื่อง comma หลุดเข้าไปในข้อมูล จะทำให้ไฟล์ CSV อ่านผิดคอลัมน์ทันที
- Data Number เก็บข้อมูลต้นฉบับเท่านั้น
- customer_id ควรเก็บเป็น String
- Data ก่อนข้อมูลจะถูกส่งเข้าระบบ ต้องผ่านการตรวจสอบคุณภาพก่อนเสมอ เพื่อไม่ให้ bad data
- "จัดกลุ่ม/จัดระดับข้อมูล" (data classification) ตามเงื่อนไขหลายชั้น ถูกใช้ต่อใน dashboard หรือ การ Analysis
- การแยก นามสกุลไฟล์ จะสามารถช่วยในการนำไปดำเนินการต่อได้งานขึ้น
- Summary ควรมีเงื่อนไขในการเช็ค ทั้งหมดว่าทำสำเร็จครบทุกส่วน เพื่อป้องกันการเข้าใจผิด เพราะการนำข้อมูลที่ไม่ครบหรือไม่สมบูรณ์ ไปใช้ต่อไม่สมควร
- Failed rows ต้องไม่ปนใน Total ข้อมูลที่ไม่ผ่านการตรวจห้ามถูกนำไปคำนวณต่อ ไม่งั้นรายงานจะผิดทั้งฉบับ
- ข้อมูลช่องว่างแอบมา ต้องจัดการก่อนเลยโดยใช้ `.strip()` เป็นเครื่องมือพื้นฐานของงาน data
- ทำความสะอาด + ตรวจรูปแบบ เป็นการ clean ก่อนทำให้กฎ validation เรียบง่าย
- เก็บค่าต้นฉบับไว้เสมอ เพื่อ debug เทียบความเปลี่ยนแปลง
- เก็บ ID ที่ผิดไว้ใน list แล้วรายงานออกมา จะทำให้รู้ว่าอะไรถูกตัดทิ้ง
- หลังจาก validation จำเป็นต้อง Always say why. แถวที่ถูกปฏิเสธต้องมีเหตุผลบอก ทีม Data ต้องไปแก้ที่ต้นทางได้
---