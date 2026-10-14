# 📘 Learning Log — 10_Customer_Contact_Cleaner.py
<br> ข้อมูลลูกค้าที่กรอกจากฟอร์มมักไม่สะอาด เช่น มีช่องว่างเกิน ตัวพิมพ์ปนกัน เบอร์โทรมีขีด งานนี้ให้เขียนโปรแกรมรับข้อมูลดิบ 1 รายการ แล้ว ทำความสะอาด + ตรวจรูปแบบ ด้วย string method basic ที่เรียนมา

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ
 
---
 
## สรุปภาพรวม (Progress Tracker)
 
| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #23 | Customer Contact Cleaner | 🟢 Merged | 2026.10.12 20:24 | 2026.10.13 22:59 |
 
สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked
 
---
 
## 📅 [2026.10.12] — Issue #23: [Customer Contact Cleaner]
 
### สิ่งที่เรียน / ทำวันนี้
- Ask the user for 3 raw values as `str`. Do not clean. Clean in the next step.
- Clean the name: Remove whitespace and capitalize the first letter
- Clean the email: Remove whitespace convert all letters to lowercase.
- Clean the phone number: Remove whitespace and remove all hyphens `(-)`.
- Validate :  tel 10 digits, Email one `@` symbol., email end with `.com`.
- Display the Before / After comparison 
- Display PASS or FAIL: reason for each item E-mail, Mobile Phone and Overall status.
- Retrieve data before `@` is Username and display phone number with `(-)` (xxx-xxx-xxxx)
- Stop Progarm if enter name incorrect 

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Order matters | Clean ก่อน Validate เสมอ การ clean ก่อนทำให้กฎ validation เรียบง่าย |---|
| Keep raw data | งานจริงเก็บค่าต้นฉบับไว้เสมอ เพื่อ debug ได้ว่า "ข้อมูลเปลี่ยนไปยังไง" |---|


### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  บั๊ก `.find('@')` คืน -1 ถูกเอาไป slice
- **สาเหตุ:**  ถ้าอีเมลไม่มี `@` เช่น anna.mail.com ค่า position จะเป็น -1 แล้ว clean_email[:-1] จะได้ anna.mail.co (ตัดตัวสุดท้ายทิ้ง) โค้ดไม่ error แต่ได้ค่าผิด ตอนนี้ยังไม่เห็นผลเพราะ print ของ user_name อยู่ใน if is_valid == True
- **วิธีแก้:**   จะให้ทำ `.find('@')` ทำงานก็ต่อเมื่อ `if result_check_email == "PASS":`

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> เรียงลำดับ clean ก่อน validate ถูกต้อง และเก็บ `raw_*` ไว้เทียบกับค่าที่ clean แล้ว <br> ตรวจชื่อไม่ครบ 2 คำด้วย len(name) == 2 ก่อนใช้ index จึงไม่ crash เมื่อกด Enter เฉย ๆ <br> จัดชื่อด้วย i[0:1].upper() + i[1:].lower() (slice + method) ได้ถูกต้อง ไม่ต้องพึ่ง `.title()`
- สิ่งที่ต้องแก้/ปรับปรุง: <br> บั๊ก .find() คืน -1 ถูกเอาไป slice <br> FAIL ของอีเมลซ้ำ `"FAIL: must be 1 @"` กับ `FAIL: must have exactly one @ `เป็นปัญหาเดียวกัน <br> ตัวแปรที่ประกาศไว้ต้นไฟล์แต่ไม่ได้ใช้ <br> Edge case : ลองใส่อีเมล `@.com`  โปรแกรมให้ PASS ทั้งที่ไม่ใช่อีเมลจริง 
- Insight ที่ได้จาก feedback นี้: <br> clean ก่อน validate <br> เก็บ `raw_*` ไว้เทียบ <br> `.title()` มันใช้งานง่าย ไม่ต้อง slice 
 
### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `List` และจะกลับมา Pracice coding again
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
- Failed rows ต้องไม่ปนใน Total ข้อมูลที่ไม่ผ่านการตรวจห้ามถูกนำไปคำนวณต่อ ไม่งั้นรายงานจะผิดทั้งฉบับ
- ข้อมูลช่องว่างแอบมา ต้องจัดการก่อนเลยโดยใช้ `.strip()` เป็นเครื่องมือพื้นฐานของงาน data 
- ทำความสะอาด + ตรวจรูปแบบ เป็นการ clean ก่อนทำให้กฎ validation เรียบง่าย
- เก็บค่าต้นฉบับไว้เสมอ เพื่อ debug เทียบความเปลี่ยนแปลง
---