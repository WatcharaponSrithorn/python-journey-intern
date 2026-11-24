# 📘 Learning Log — 19_Daily_Data_Load_Report.py
<br> ทุกเช้า job โหลดข้อมูลจะดึงข้อมูลจากหลายแหล่ง (ไฟล์ CSV, API, database) ทีมอยากเห็นรายงานสั้น ๆ ว่าแต่ละแหล่งโหลดกี่แถว เสียกี่แถว คุณภาพผ่านเกณฑ์ไหม แต่ละแหล่งมีข้อมูลประกอบไม่เหมือนกัน เช่น ทีมเจ้าของ (team) หรือ environment จึงต้องออกแบบให้เพิ่มข้อมูลได้โดยไม่ต้องแก้ function

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ

---

## สรุปภาพรวม (Progress Tracker)

| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #42 | Daily Data Load Report with return, *args and **kwargs | 🟢 Merged | 2026.11.14 15:39 | 2026.11.21 07:26 |

สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked

---

## 📅 [2026.11.14] — Issue #42: [19_Daily_Data_Load_Report.py]

### สิ่งที่เรียน / ทำวันนี้
#### Part A : Copy 3 function From #18
- `printTitle`, `cleanName`, `printInfo`
#### Part B : Calculate Success Rate
- check condition rows_read not 0
#### Part C Quality Gate
- default parameter is variable constant
#### Part D Sum Rows (*args)
- Receive is *args repeats use for loop for Accumulation
#### Part E Build Run Record (**kwargs + call function other)
- Receive parameter normal and **kwargs
- create dictionary and for loop add key, value from **kwargs retrun dict
#### Part F Run Stats (return multiply values)
- Receive is *args, call other function for sum
- check count not 0 and calculate average
- retrun 3 value
#### Part G : Main report (Main loop)
- check amount of sources
- call function `printTitle`
- Main loop for display report


### 🧰 What I used
- `**kwargs`
- `return`, `*args`
- `def`, `parameter`, `default parameter`
- `string methods`
- `for` loop
- `if/elif/else`
- `list of tuple`, f-string, casting

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| คำนวณ = return, แสดงผล = print | แยกหน้าที่ชัดเจน function ที่ return เอาไปใช้ซ้ำและทดสอบได้ง่าย |---|
| Control check เทียบหลายแหล่ง | ช่วยจับข้อมูลที่หายระหว่างทาง และต้อง FAIL ได้จริง |---|

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:** โค้ดซ้ำใน branch PASS และ FAIL ใน if isGoodQuality(...) ที่ main loop มี 2 branch เขียนเหมือนกัน
- **สาเหตุ:**  เนื่องจากใช้การเเสดง PASS กับ FAIL เลยใน
- **วิธีแก้:**   ตั้ง status เป็น "PASS" หรือ "FAIL" ใน if..else พอ แล้วย้ายการแสดงผลทั้งหมดออกมาหลัง if/else

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br> รายงานหลัก + Control check logic ถูก
- สิ่งที่ต้องแก้/ปรับปรุง: <br> ชื่อ key `row_reject` ต้องเป็น `rows_rejected` <br> โค้ดซ้ำใน branch PASS และ FAIL <br> `min_rate=MIN_SUCCESS_RATE` ใน loop ไม่จำเป็น <br> `.get()` กับ key ที่ต้องมีเสมอ แต่ `.get` จะคืน None เงียบ ๆ `dict[key]` จะ error ทันที (KeyError)
- Insight ที่ได้จาก feedback นี้: <br> ยังเข้าใจว่า คุณภาพและโครงสร้างของโค้ด การลดโค้ดซ้ำระหว่าง Branch PASS และ FAIL และเข้าใจความแตกต่างระหว่าง .get() และ dict[key] ซึ่งควรเลือกใช้ตามความจำเป็นของข้อมูล ส่วน `.get` เก็บไว้ใช้กับ key ที่ อาจไม่มี การใช้ dict[key] กับข้อมูลที่ต้องมีเสมอ ช่วยให้ตรวจพบปัญหา Missing Required Fields ได้ทันที แทนที่จะปล่อยให้ค่า None ไหลไปยังขั้นตอนประมวลผลถัดไป

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
- ลำดับ parameter ที่ถูกต้อง = parameter ปกติ  →  default value  →  *args  →  **kwargs
- return หลายค่า เขียน return a, b, c จริง ๆ แล้วคือส่ง tuple 1 ก้อน แล้วรับด้วย tuple unpacking: x, y, z

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
- การใช้ dict[key] กับข้อมูลที่ต้องมีเสมอ ช่วยให้ตรวจพบปัญหา Missing Required Fields ได้ทันที แทนที่จะปล่อยให้ค่า None ไหลไปยังขั้นตอนประมวลผลถัดไป
- การใช้ .get() เหมาะกับการเข้าถึงข้อมูลที่อาจไม่มี Key อยู่ใน Dictionary เพื่อรองรับข้อมูลที่ไม่สมบูรณ์ได้ ช่วยให้กระบวนการประมวลผลข้อมูลมีความยืดหยุ่นและลดปัญหาจาก Missing Data
---