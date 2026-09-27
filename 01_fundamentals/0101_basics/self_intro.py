"""
Task : 
ใช้ print() แนะนำ ชื่อ, มหาวิทยาลัย/สาขา, เป้าหมายการฝึกงาน
มี comment อธิบายทุก section ของโค้ด (บรรทัดนี้ทำอะไร ทำไมถึงเขียนแบบนี้)
จัดรูปแบบผลลัพธ์ให้อ่านง่าย (เช่นใช้ "="*30 คั่น section)
โดยมี 3 Section 
Section 1: ข้อมูลส่วนตัว
Section 2: เป้าหมายการฝึกงาน
Section 3: แสดงผลลัพธ์แนะนำตัว
"""
# ============================================
# File : intro.py
# Purpose: Introduce yourself before starting the internship
# Author: Watacharapon
# ============================================

# Section 1: Personal my self
Fname = "Watcharapon"
Lname = "Srithorn"
university = "Rajamangala University of Technology Tawan-ok"
campus = "Chakrabongse Bhuvanarth Campus"
major = "Bachelor of Science in Information Technology"
contact = "srith.watcharapon@gmail.com"

#Section 2: Internship Goal
goal_1 = "I am interested in an internship in software development "
goal_11 ="or data-related roles"
goal_2 = "My goal is to transition from my current career into a career "
goal_22 = "in software development or data-related roles."
goal_3 = "I am also open to continuing with the company and starting "
goal_33 = "a full-time position after the internship."

#Section 2: Output
print(f"╔"+"═"*70+"╗")              # Use F-String for can put variable {} inside f" "
print(f"║{"PROFILE - INTERNSHIP CANDIDATE":^70}║")      # use :^70 becuase defind width of channel
print(f"╠"+"═"*70+"╣ ")             # Use "="*40 for reduce coding.
print(f"║{"Personal my self":^70}║")  
print(f"╠"+"═"*70+"╣ ")
print(f"║{f"Name : {Fname} {Lname}":<70}║")             # use :<70 for if text < 40 modify width is 40
print(f"║{f"University : {university}":<70}║")  
print(f"║{f"Campas : {campus}":<70}║")
print(f"║{f"Major : {major}":<70}║")
print(f"║{f"Contact : {contact}":<70}║")
print(f"╠"+"═"*70+"╣ ")
print(f"║{"Internship Goal":^70}║")
print(f"╠"+"═"*70+"╣ ")
print(f"║{f"{goal_1}":<70}║")
print(f"║{f"{goal_11}":<70}║")
print(f"║"+" "*70+"║ ")
print(f"║{f"{goal_2}":<70}║")
print(f"║{f"{goal_22}":<70}║")
print(f"║{f"*****":<70}║")
print(f"║{f"{goal_3}":<70}║")
print(f"║{f"{goal_33}":<70}║")
print(f"║"+" "*70+"║ ")
print(f"╚"+"═"*70+"╝ ")