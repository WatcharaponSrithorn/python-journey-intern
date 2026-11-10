# 📘 Learning Log — 17_Daily_Order_Report.py
<br> ใน Issue เก่า ต้องเขียน if amount >= MIN_AMOUNT ซ้ำสองที่ เพราะ function ยังส่งค่ากลับไม่ได้ ตอนนี้น้องเรียน return แล้ว มาแก้ให้ function ส่งคำตอบกลับ แล้วให้ loop เอาไปใช้ต่อ

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ

---

## สรุปภาพรวม (Progress Tracker)

| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #38 | Daily order report with return functions | 🟢 Merged | 2026.11.09 20:48 | 2026.11.10 21:18 |

สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked

---

## 📅 [2026.11.09] — Issue #38: [17_Daily_Order_Report.py]

### สิ่งที่เรียน / ทำวันนี้
#### Main data
#### Part A Create function and return
- Create Function Print a title with lines **additional
- Create Function for clean raw_name
- Create Function for check quantity must not be less than MIN_QUANTITY
- Create Function for calculate amount of each order_id
- Create Function for sum of function calculateTotal
#### Part B Use function in loop
- Check amount of Main data before
- call function printTitle
- For loop for check Quantity and display each row
- count valid and count reject
#### Part C Summary
- Display result of count valid and count reject
- call function addall() for grand total
- Control check by count valid + count reject = main data
#### Part D test default value
- Change default value

### 🧰 What I used
- `return`, `*args`
- `def`, `parameter`, `default parameter`
- `string methods`
- `for` loop
- `if/elif/else`
- `list of tuple`, f-string, casting

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| `return` | ส่งค่ากลับให้เรียกใช้ ถ้าไม่รับค่าด้วยตัวแปรหรือ print ค่านั้นจะหายไป |---|
| เขียนกฎไว้ที่เดียว | ถ้าวันหนึ่ง MIN_QUANTITY เปลี่ยน แก้แค่ที่เดียว ผลเปลี่ยนทุกที่ |---|
| `*args` | รับ argument กี่ตัวก็ได้ แล้วเก็บเป็น tuple |---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:**  addAll ยังไม่ใช้ *args
- **สาเหตุ:**  โค้ดเป็น def addAll(total): และเรียก addAll(list_total) (ส่ง list ก้อนเดียว)
- **วิธีแก้:**   เปลี่ยนชื่อ parameter เป็น *totals, ตอนเรียกใช้ ใส่ * หน้า list

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> มี function 4 ตัว ชื่อชัดเจน  <br> for + tuple unpacking <br> เช็กด้วย isValidQuantity ที่เดียว
- สิ่งที่ต้องแก้/ปรับปรุง: <br> addAll ยังไม่ใช้ *args
- Insight ที่ได้จาก feedback นี้: <br> ได้เรียนรู้การออกแบบ Function ให้แบ่งหน้าที่ชัดเจน <br>การใช้ For Loop ร่วมกับ Tuple Unpacking เพื่อให้อ่านและจัดการข้อมูลได้ง่ายขึ้น <br> ได้การพัฒนา Function addAll() โดยใช้ *args เพื่อให้สามารถรับ Arguments ได้หลายจำนวนโดยไม่จำกัดจำนวน Parameters ที่กำหนดไว้ล่วงหน้า

### สิ่งที่จะทำต่อ (Next Steps)
- ทบทวนเรียนรู้ `Lambda` และจะกลับมา Pracice coding again
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
- 0 หารไม่ได้ตามหลักการ จะต้องทำการเช็คก่อน และ ตรวจ "ตัวหาร" ไม่ใช่ "ผลลัพธ์" คือ ค่าว่าง ไม่ใช่ 0
- Ternary if `ตัวแปร = [ค่าที่จะได้ถ้าจริง] if [เงื่อนไข] else [ค่าที่จะได้ถ้าเท็จ]`
- List Comprehension `[ expression for item in iterable if condition ]`
- `default parameter` สามารถส่งจาก Argument ไปเปลี่ยนได้ด้วย
- list of tuple หากต้อง วน loop ควร tuple unpacking ต่อ for เลย
- `*args` หากสร้าง Function รับ parameter เป็น `*args` และ Argument ที่ส่งไปเป็น List ให้ใส่ *หน้า list

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
- พอเข้าใจ พื้นฐาน คิดเป็น stage : Extract → Clean → Validate → Transform → Load/Report และเราต้องเป็นเป็น Part ในการใช้งาน หรือทำงาน ง่ายต่อการ Test หรือ ตรวจสอบ
- Control checks ทำให้รายงาน และข้อมูลที่ผ่าน stage น่าเชื่อถือได้
- 1 function ทำ 1 งาน เพราะทดสอบและแก้ไขง่ายกว่า
- Data work => clean ก่อนเช็ก, edge case, control check
---