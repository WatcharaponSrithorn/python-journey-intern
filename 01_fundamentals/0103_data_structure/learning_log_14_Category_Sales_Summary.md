# 📘 Learning Log — 14_Category_Sales_Summary.py
<br> ทีม Sales อยากได้รายงาน ยอดขายแยกตามหมวดสินค้า ข้อมูลมาเป็นแถว (tuple) และใช้ รหัสหมวด เช่น STA, ELC ไม่ใช่ชื่อเต็ม งานคือแปลงรหัสเป็นชื่อ รวมยอดขายแต่ละหมวด และสรุป เหตุผลที่แถวถูกปฏิเสธ ว่าเกิดเพราะอะไรบ่อยที่สุด

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ

---

## สรุปภาพรวม (Progress Tracker)

| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #32 | Category Sales Summary | 🟢 Merged | 2026.10.22 22:36 | 2026.10.23 17:57 |

สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked

---

## 📅 [2026.10.22] — Issue #32: [14_Category_Sales_Summary.py]

### สิ่งที่เรียน / ทำวันนี้
- Section check the row size before unpack and store reason data no have 4 item
- clean category_id after unpack
- check validate as per codition : Unknown category, Quantity and price must be more than 0
- check valid row must reason == "" else is reason must reject and calculate total, grand total, += 1 row to valid and invalid
- Section find Top category
- Section calculate Avg/order
- Section display report table use for loop for display
- Have check value if no have row will end program

### 🧰 What I used
- `Dictionary` , Dictionary function
- `for` loop
- `if..else`

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Group by | คือรูปแบบรวมยอดต่อกลุ่ม `d[key] = d.get(key, 0) + ค่า` |---|
| ไม่ hard-code จากข้อมูล | วนจาก dictionary แทน ไม่เช่นนั้นหมวดที่ไม่มีข้อมูลจะพัง และหมวดใหม่จะหาย |---|
| Decide vs Act | chain if..else # Decide: ตัดสินใจ , # Act: ลงมือทำ  |---|
| Self-check ต้องมาจากคนละแหล่ง | ถ้านับจากแหล่งเดียวกัน จะไม่มีวันจับบั๊กได้ |---|


### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  ตารางเขียนชื่อหมวดแบบตายตัว (hard-code) จะพังเมื่อหมวดไหนไม่มียอดขาย ในส่วน Section display report
- **สาเหตุ:**  hard-code จากข้อมูล ประกาศตัวแปร โดยดูจากข้อมูลที่ยกตัวอย่างมา
- **วิธีแก้:**   ใช้ for วน dictionary ดึงชื่อเต็มด้วย `category_names[code]` ดึงจำนวนออเดอร์ด้วย `orders_by_category[code]` และ Avg ด้วย `avg_order[code]`

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> Group by ด้วย dictionary ถูกต้อง ใช้ .get(key, 0) <br> Clean หลัง unpack ก่อนค้นหา <br> reason = "" อยู่ใน loop ไม่มีค่าเก่าค้าง <br> ตรวจด้วย if / elif ตามลำดับ First failure wins <br> Top category ถูกต้อง <br> Avg/order คำนวณถูก
- สิ่งที่ต้องแก้/ปรับปรุง: <br>  ตารางเขียนชื่อหมวดแบบตายตัว (hard-code) <br> เขียน `reject_reasons[reason] = reject_reasons.get(reason,0) +1` ซ้ำ 4 รอบ <br> ให้นับแยกต่างหากใน loop ตรวจแถว (ถ้าแถวผ่าน → valid_rows += 1 และ grand_total += total, ถ้าปฏิเสธ → reject_rows += 1)
- Insight ที่ได้จาก feedback นี้:<br> ลดการเขียนโค้ดซ้ำ วิธีจัดการ `reject_reasons`ให้เป็นรูปแบบเดียว <br> ลดการ Hard-code ตารางผลลัพธ์ควรดึงจากข้อมูลใน Dictionary แทนการเขียนชื่อหมวดไว้ตายตัว เพื่อให้รองรับหมวดหมู่ใหม่ <br> แยกส่วนประมวลผลออกจากส่วนแสดงผล

### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `Function` และจะกลับมา Pracice coding again
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
- `dics` สามาารถ Group by คือรูปแบบรวมยอดต่อกลุ่ม `d[key] = d.get(key, 0) + ค่า`
- `dics` สามารถ ใช้ loop ดึงจากข้อมูลใน Dictionary แทนการเขียนชื่อหมวดไว้ตายตัว

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
- Group By (รวมยอดต่อกลุ่ม) : รวมหลายแถวให้เหลือ 1 แถวต่อ 1 กลุ่ม เช่น ยอดขายรวมต่อหมวด
- Lookup Table : ตารางเล็ก ๆ ที่ใช้ แปลงรหัสเป็นชื่อ
- Data-driven Code vs Hard-coding ข้อมูลเปลี่ยนรูปไปจากที่คาดไว้: ข้อมูลจริงเปลี่ยนเสมอ โค้ดที่วนจากข้อมูลจึงทนกว่า
---