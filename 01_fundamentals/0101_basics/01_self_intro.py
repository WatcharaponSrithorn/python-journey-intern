# ============================================
# File : intro.py
# Purpose: Introduce yourself before starting the internship
# Author: Watacharapon
# ============================================

# Section 1: Personal my self
first_name = "Watcharapon"
last_name = "Srithorn"
university = "Rajamangala University of Technology Tawan-ok"
campus = "Chakrabongse Bhuvanarth Campus"
major = "Bachelor of Science in Information Technology"
contact = "srith.watcharapon@gmail.com"
# declaring for use not f-string inside another f-string
title_line = "PROFILE - INTERNSHIP CANDIDATE"
personal_header = "Personal my self"
full_name = f"{first_name} {last_name}"
line_university = f"university : {university}"
line_campus = f"campus : {campus}"
line_major = f"major : {major}"
line_concact = f"contact : {contact}"
goal_header = "Internship Goal"

#Section 2: Internship Goal
goal_line1 = "I am interested in an internship in software development"
goal_line2 = "or data-related roles"
goal_line3 = "My goal is to transition from my current career into a career"
goal_line4 = "in software development or data-related roles."
goal_line5 = "I am also open to continuing with the company and starting"
goal_line6 = "a full-time position after the internship."

#Section 3: Output
print(f"╔"+"═"*70+"╗")                  # Use F-String for can put variable {} inside f" "
print(f"║{title_line:^70}║")            # use :^70 becuase defind width of channel
print(f"╠"+"═"*70+"╣ ")                 # Use "="*70 for reduce coding.
print(f"║{personal_header:^70}║")  
print(f"╠"+"═"*70+"╣ ")
print(f"║{full_name:<70}║")             # use :<70 for if text < 70 modify width is 70
print(f"║{line_university:<70}║")  
print(f"║{line_campus:<70}║")
print(f"║{line_major:<70}║")
print(f"║{line_concact:<70}║")
print(f"╠"+"═"*70+"╣ ")
print(f"║{goal_header:^70}║")
print(f"╠"+"═"*70+"╣ ")
print(f"║{goal_line1:<70}║")
print(f"║{goal_line2:<70}║")
print(f"║{goal_line3:<70}║")
print(f"║{goal_line4:<70}║")
print(f"║{goal_line5:<70}║")
print(f"║{goal_line6:<70}║")
print(f"╚"+"═"*70+"╝")