# 📘 Learning Log — 11_Order_ID_Batch_Cleaner.py
<br> รับ Order ID จาก 2 ร้าน (Store A และ Store B) แต่ข้อมูลสกปรก มีช่องว่าง ตัวพิมพ์เล็ก ค่าว่าง และ ID ซ้ำ คือเขียนสคริปต์ทำความสะอาดข้อมูลก่อนส่งเข้าระบบ

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #25 | Order ID Batch Cleaner | 🟢 Merged | 2026.10.15 22:17 | 2026.10.16 22:16 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.10.15] — Issue #25: [Order ID Batch Cleaner]
 
### สิ่งที่เรียน / ทำวันนี้
- Receive value from user store A and store B.
- split value is data type list
- Section cleanning before validate become report : upper, strip,
- Section check valid : count empty_values , Skip empty, check start with "ORD-", Remove duplicates, Sort IDs
- Improve :
- improve code # section clean by List comprehension: Try using it in the cleaning step.
- improve code # section Remove duplicates.by use `if item in unique_ids:` if have not append into unique_ids 
- improve code # Sort IDs use `.sort()` direct with `unique_ids` 

### 🧰 What I used
- list methods: `.count("")` `append()` `.sort()`
- string methods: `.upper()` `.strip()` `len()`
- for loop
- if, if..else

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Never delete bad data silently. | เก็บ ID ที่ผิดไว้ในอีก list แล้วรายงานออกมา ทีมจะได้รู้ว่าอะไรถูกตัดทิ้ง |---|
| Count everything. | จำนวนแถวที่อ่าน, ข้าม, ซ้ำ, ผิด ควรรวมกันได้เท่ากับจำนวนทั้งหมด ถ้าไม่เท่ากัน แปลว่ามีบั๊ก |---|


### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  การลบ ID ซ้ำออก แต่เราไม่ได้ "เก็บตัวที่เจอก่อน" 
- **สาเหตุ:**  เพราะใช้ `.count()` กับ `.remove()`
- **วิธีแก้:**   ใช้ `for` loop ในการเข้าถึงข้อมูลก่อน จากนั้น ใช้ `if` เช็คเงื่อนไข ถ้า `item` in เป็นสมาชิกอยู่แล้วใน `unique_ids` ให้ count_remove += 1 แต่ถ้าไม่มี `else` ให้ `.append(item)` ใน `unique_ids`

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> ใช้ `.count("")` นับค่าว่าง ไม่ต้อง loop เพิ่ม <br>ใช้ [-1] เอา ID สุดท้ายได้ถูกต้อง <br> จัดหน้าตารายงานด้วย `:<25` อ่านง่าย
- สิ่งที่ต้องแก้/ปรับปรุง: <br> ลบ ID ซ้ำ ไม่ได้ "เก็บตัวที่เจอก่อน" <br> `sort()` ไม่จำเป็นต้องใช้ใน loop และ ไม่ต้องสร้าง list ใหม่เลย  <br> ชื่อตัวแปรบอกความหมายไม่ชัด `display_1`,`display...` เปลี่ยนเป็น `label` อะไร
- Insight ที่ได้จาก feedback นี้: <br> การใช้ `.remove()` มีข้อจำกัด ต้องคิดให้ดี ลบ ตัวแรก ใน list <br> `sort()` ใน loop ซ้ำทุกครั้งที่ append ทั้งที่ต้องการแค่ผลลัพธ์สุดท้าย ถ้ามี 1 ล้านแถว จะทำงานช้ามาก
 
### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `Tuple` และจะกลับมา Pracice coding again
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
---