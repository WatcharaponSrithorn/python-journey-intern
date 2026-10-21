# 📘 Learning Log — 13_Customer_ID_Reconciliation.py
<br> งาน Reconciliation ลูกค้าเดียวกันควรมี ID อยู่ทั้งในระบบ CRM และระบบ Billing แต่ข้อมูลสกปรก และมี ID ที่ฝั่งหนึ่งขาดหายไป งานคือทำความสะอาด เทียบกัน และสรุปว่าใครอยู่ฝั่งไหนบ้าง

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ

---

## สรุปภาพรวม (Progress Tracker)

| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #30 | Customer ID Reconciliation | 🟢 Merged | 2026.10.18 19:41 | 2026.10.19 00:46 |

สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked

---

## 📅 [2026.10.18] — Issue #30: [13_Customer_ID_Reconciliation.py]

### สิ่งที่เรียน / ทำวันนี้
- Casting data type from `list` to `set` for remove closed IDs from both systems.
- Cleaning data both system before validation
- Validation then store valid and invalid
- Calculate count duplicate, Find closed IDs excluded, Find remove closed IDs by use `set` menthod
- Union Closed IDs excluded of both sytem and sort for display
- Compare the data using set operations.
- Store the 3 results as a list of tuples. Print them with one for loop.
- Union Invalid IDs both system
- Check amount of all customer for calculate match_rat by protect value 0

### 🧰 What I used
- `set` , `set` function
- `for` loop
- lits of tuple
- lite function, String method
- if..else


### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Set ไม่มีลำดับ | ถ้ารายงานต้องออกมาเหมือนเดิมทุกครั้ง ต้อง sort ก่อนแสดงเสมอ ไม่งั้นผลอาจเรียงต่างกันในแต่ละรอบ |---|
| Config เก็บเป็น tuple | ค่าที่ไม่ควรถูกแก้ระหว่างโปรแกรมทำงาน (เช่น รายการ closed) ใช้ tuple จะปลอดภัยกว่า list |---|
| เช็กก่อนหารเสมอ | ข้อมูลว่างเกิดได้จริงในงานจริง (เช่น ระบบล่มส่งข้อมูลมา 0 แถว) |---|


### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  Set ไม่มีลำดับ ผลลัพธ์บางบรรทัดเรียงไม่คงที่
- **สาเหตุ:**  เปลี่ยนเป็น list แล้วแต่ไม่ได้ดำเนิการ sort
- **วิธีแก้:**   เพิ่ม การ sort อีกบรรทัดต่อ

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> Set operations ถูกต้อง `&, -, |` ให้ผลตรงทุกเคส <br> Closed IDs excluded ใช้ intersection แยกแต่ละระบบ แล้ว union รวมกัน <br> แปลง tuple เป็น set  <br> กันหารด้วยศูนย์ <br> จัดโค้ดเป็น section
- สิ่งที่ต้องแก้/ปรับปรุง: <br> คอลัมน์ Unique นับผิด <br> Set ไม่มีลำดับ <br> รูปแบบผลลัพธ์ไม่ตรง Expected 2 จุด <br> เรียก set(...) ซ้ำหลายรอบ
- Insight ที่ได้จาก feedback นี้: <br> การนำตัวแปรมาใช้ Unique ยังต้องตรวจสอบให้ดี <br> โค้ดที่ดีควรถูกต้องและมีประสิทธิภาพ การลดการเรียก set() ซ้ำ และจัดเก็บผลลัพธ์ระหว่างทางในตัวแปร ช่วยให้โค้ดกระชับ อ่านง่าย และดูแลรักษาได้สะดวกขึ้น

### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `Dictionary` และจะกลับมา Pracice coding again
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
- `set` ไม่มีลำดับ จะเปลี่ยน data type เป็น list เพื่อ sort เพื่อเรียงลำดับในการแสดงผล

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
- Reconciliation ช่วยให้ตรวจสอบความถูกต้องของข้อมูลเพื่อ และให้เป็นฐานข้อมูลเดียว รักษาความเป็นมาตราฐานข้อมูล
---