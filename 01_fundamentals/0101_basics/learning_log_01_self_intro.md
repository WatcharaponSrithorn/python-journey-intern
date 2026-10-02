# 📘 Learning Log — 01_self_intro.py

> อัปเดตทุกครั้งที่เรียนจบ 1 Topic หรือทำ 1 Issue เสร็จ

---

## สรุปภาพรวม (Progress Tracker)

| Issue # | หัวข้อ | สถานะ | วันที่เริ่ม | วันที่ Merge |
|---|---|---|---|---|
| #1 | Introduce yourself before starting the internship | 🟢 Merged | 2026.08.27 | 2026.08.27 |

สถานะ: 🔴 Not Started · 🟡 In Progress · 🟢 Merged · 🔵 Blocked

---

## 📅 [2026.08.27] — Issue #1: [Setup Repository + Self Introduction Script]

### สิ่งที่เรียน / ทำวันนี้
- Create a file self_intro.py that
- Uses print() to introduce
- Has comments explaining every section
- Formats the output for readability

### Concept ใหม่ที่เจอ
| Concept | สรุปสั้นๆ ในแบบตัวเอง | ลิงก์อ้างอิง (ถ้ามี) |
|---|---|---|
| Git workflow | branch → PR → review → merge | |
| การแสดงผล | การจัดรูปแบบการเเสดงผล | |

### ปัญหาที่เจอ + วิธีแก้
- **ปัญหา:** ยังไม่เข้าใจ workflow 
- **สาเหตุ:** เป็น ไฟล์แรกที่เริ่มทำ
- **วิธีแก้:** จะต้องทำการฝึกฝนไปเรื่อยเพื่อให้ ชำนาญ

### Feedback จาก Code Review
- Comment ที่ได้รับ: <br>1. ใช้ box-drawing characters (╔ ═ ╗) กับ f-string alignment (:^70, :<70) 
- สิ่งที่ต้องแก้/ปรับปรุง: <br>1. Docstring บนสุดของไฟล์ (บรรทัด 1-9) ตรงนี้คือ task description ที่ copy จาก issue มา ไม่ใช่ docstring ของไฟล์จริง ๆ ในโค้ดจริงเราจะไม่ทิ้ง requirement/task ไว้ในไฟล์ <br>2. Section numbering ผิด (comment ซ้ำเลข)<br>3. ตัวแปรแตกเป็นชิ้นเยอะเกินไป (goal_1, goal_11, goal_2, goal_22...)<br>4. Nested f-string ซ้อนกัน (ระวังเรื่อง Python version)<br>5. Comment ที่เขียนไม่ตรงกับโค้ดจริง<br>6. Naming convention (PEP8) ตาม PEP8 (มาตรฐานการตั้งชื่อของ Python) ตัวแปรทั่วไปควรเป็น snake_case ตัวพิมพ์เล็กทั้งหมด ไม่ใช่ตัวใหญ่นำหน้าแบบนี้ (แบบนี้มักใช้กับชื่อ Class)<br>7. คำผิด (Typo) ใน output
- Insight ที่ได้จาก feedback นี้: <br> 1. เริ่มเข้าใจการใช้งาน Git workflow <br> 2. ทำให้ว่า ไม่สมควรเอา task description มาใส่ในงาน ตอนนที่ทำ กลัวลืม<br> 3. ต้องตรวจเช็คความถูกต้องอีกที ก่อน commit <br> 4. ได้เรียนรู้เพิ่มเรื่องการตั้งชื่อ variable ไม่ควรย่อยตัวเลข

### สิ่งที่จะทำต่อ (Next Steps)
-
สร้างสคริปต์คำนวณค่า BMI (BMI Calculator)
---

## 🧠 คลัง Concept สะสม (Cheat Sheet ส่วนตัว)

> ย้าย concept สำคัญจากด้านบนมารวมไว้ที่นี่

### Python
- พอสามารถที่จะคำสั่ง print() ในรูปแบบ f-string การจัดแนวได้ การตั้งชื่อตัวแปรที่สื่อความหมาย
- การสร้าง Variable เก็บข้อความไว้ก่อน แล้วค่อยนำมาใช้ใน print()จะทำให้ แก้ไข Code จุดเดียว

### Git / GitHub Workflow
- Git workflow : branch → Coding → ทดสอบรันก่อน commit → Commit → Push → PR → review → merge
- เขียน commit message ให้คนอื่นเข้าใจได้

---
