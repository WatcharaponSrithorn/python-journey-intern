# 🗺️ Roadmap_fundamental
A learning log for tracking my basic Python learning progress, including the topics I learn and review, practice activities, and learning dates. It helps me build consistent practice habits and prepare for an IT internship.
---

## 0101. Basics

| Sub-Topics |
|---|
| Basic Elements of Statements and Syntax |
| Data type basic , Varible , Casting data type |
| Input/Output |

**Learning Log :**
>
| Date | Topics Reviewed | Learning Notes | 
|---|---|---|
| 2026.09.25 | Introduction | <br> Python runs on an **interpreter**. <br> **Advantages:** It supports multiple operating systems, is open source, supports OOP, and has many libraries. <br> Python does not require `;` or `{}` to end a statement. <br> Python files use the `.py` file extension. <br> Python requires **indentation** because it is important for defining the **scope** of the code. <br> You can check the installed Python version in the local computer's CMD by using: `python --version`
| 2026.09.26 | Comment | Use explain code , use temporarity cancelled to prevert from executing code <br> Commenting have 2 way <br> 1. Oneline comment use `#` <br> 2. Multiline comment use `"' '"` triple quotes |
| | Output | Use `print()` to display output on the screen. <br> Use `print()` with `( )` to display text. Strings must be inside `" "` or `' '`. <br> To print multiple items to display output on one line, use `print()` with `end=" "`. <br> Numbers do not need single or double quotes, and can perform mathematical operations inside `( )`.|
|  | Primitive Data Type | Type Number -> `int`, `float`, `complex` <br> Type Logic -> `bool` <br> Type String -> `str` <br> Type null -> `None` <br> can check data type use by `type()` inside specify value <br> Python must not setting data type can assign value to varible but if need specify can use by `int()`, `float()`, `str()`, `bool` |
|  | Type number | `int` is integer whole number without decimal <br> `float` is integer whole number have decimal or Floating point number <br> `complex` Numberical scientific to have `e` is power of 10 |
|  | Type String |`str` Use store text or character by use `" "` or `' '` |
|  | Type Logic | `bool` has only two values: `True` and `False`. programming need to know, <br> when compare two value for result return Value is Boolean is answer,<br> when run condition in if statement `if`, `else`, `elif`, <br> can use `bool()` inside `()` put value for check Boolean is `True` or `False` <br> Most values are `True` , but some values are `False` as except empty string `bool("")`,  value zero `0` value `None`. |
|  | Variable | <br> Python does not require a command to declare a variable, can assign a value directly using `variable = value`. <br> can assign multiple values to multiple variables in one line using `,`: `variable1, variable2 = value1, value2`. <br> can assign one value to multiple variables in one line using `=`: `variable1 = variable2 = value`.<br>`=` is the assignment operator. It assigns the value on the right to the variable on the left.|
|  | Rules naming Variable | names must start with a letter or an underscore `_`.<br> names must not start with a number. <br> names are case-sensitive.<br> names must not contain special characters, such as `{}`, `%`, or `^`. <br> names must not contain spaces.<br> names must not be the same as Python keywords. <br> **Tips for Naming Variables** <br>**Camel Case:** The first word starts with a lowercase letter, and each following word starts with an uppercase letter. <br> Example: `studentName`<br>**Pascal Case:** Each word starts with an uppercase letter.<br>Example: `StudentName`<br>**Snake Case:** Words are separated by an underscore `_`.<br>Example: `student_name`|
|  | Input | Receive data from the user through the keyboard and store it in a variable `varible = input()`. <br> can define the data type of the input value by using **type casting**, such as `variable = int(input())`. <br>The `input()` function always returns the input value as a string (`str`).|
|  | Casting | Use a data type name to convert a variable to the required data type.<br> `float(varible)` `str(int)` `str(5)` <br>If the original data type is `float` and you cast it to `int`, the decimal part will be discarded.|
| 2026.09.27| F-String | F-String `f" string "`can insert a variable in `" "` by put `{}` `f" name {variable}"` <br> can math inside `f"{5+3}"` <br> can format decimal numbers`f"price : {price:.2f}"` <br> Short and easy to read. |
|  | Variable <br>(Additional) | variable can store multiple lines of text.  on varible by use `variable = (" text 1 "\n " text 2 ")` by `\n` is start new line |
|  | `\` (Backslash) | `\n` new line , `\t` it is Tab, `\` End of line of code for code long <br> if will path file must use `r"C:\Users\test"`|
|---|---|---|

**Code Practice :**
| Date | File Code | Learning Log | 
|---|---|---|
| 2026.09.27 | [01_self_intro.py](./01_fundamentals/0101_basics/01_self_intro.py) | [Learning Log](./01_fundamentals/0101_basics/learning_log_01_self_intro.md) |
| 2026.09.29 | [02_BMI_Calculator.py](./01_fundamentals/0101_basics/02_BMI_Calculator.py)|[Learning Log](./01_fundamentals/0101_basics/learning_log_02_BMI_Calculator.md)|
| 2026.09.30 | [03_shopping_receipt.py](./01_fundamentals/0101_basics/03_shopping_receipt.py) |[Learning Log](./01_fundamentals/0101_basics/learning_log_03_shopping_receipt.md)|
| 2026.10.01 | [04_Customer_CSV_Formatter.py](./01_fundamentals/0101_basics/04_Customer_CSV_Formatter.py) |[Learning Log](./01_fundamentals/0101_basics/learning_log_04_Customer_CSV_Formatter.md)|
|---|---|---|

---

## 0102. Control Flow

| Sub-Topics |
|---|
| Operators |
| Match Statement  |
| if, elif, else |
| for, while |

**Learning Log :**
>
| Date | Topics Reviewed | Learning Notes |
|---|---|---|
| 2026.10.03 | Operator | Oprerator is perform on variable and value by <br> **Arithmetic** use with number value to perform mathematic `+` add, `-` substrac, `*` multi, `/` divis, `%` moduls, `**` power, `//`fool divis return integer <br> **Assignment** perform same Arithmetic is reduce to form `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`  <br> **Logical** Ues combie condition statement `and` True and True is value True always , `or` False or False is value False always , `not` opposite,  <br> **Comparison** Use to compare 2 value `==` equal , `!=` not equal, `<` less than, `>` more than , `<=`less than or equal, `>=`more than or equal <br> **Identity** Use compare object with same memory location return is `True` or `False`, `is`, `is not` <br> Differance between `is` check both variable to same in memory and `==` check value of both variable equal <br> **Membership** Use check value in variable have this value is element in variable and can chaeck also work with String  |
|  | if Statement | if Statement is statement logicalcal condition <br> `if` use when have 1 condition and if condition is True will perform inside statement but must indent because to define scope <br> `else` use when have 2 condition and perform inside statement when if is False `elif` Use when have more than 2 condition and can have `elif` more than 1 statement and perform when previous condition not True |
|  | Ternary if | Use when have one statement to execute need result is True or False by have 2 condition |
|  | Nested if | `if` Statement can have if inside if by have if main and if sub and will execute if main before |
|  | Pass | `if` can not empty must inside have statement But can put `pass` inside `if` statement for execute no error |
|---|---|---|

**Code Practice :**
| Date | File Code | Learning Log | 
|---|---|---|
|2026.10.04 | [05_Customer_Data_Validator.py](./01_fundamentals/0102_control_flow/05_Customer_Data_Validator.py) | [Learning Log](./01_fundamentals/0102_control_flow/learning_log_05_Customer_Data_Validator.md) |
|2026.10.04 | [06_Customer_Tier_Classifier.py](./01_fundamentals/0102_control_flow/06_Customer_Tier_Classifier.py) | [Learning Log](./01_fundamentals/0102_control_flow/learning_log_06_Customer_Tier_Classifier) |
---

## 0103. data_structure

| Sub-Topics |
|---|
| List, function manage List |
| Tuple, Set |
| Dictionary function manage Dictionary |

**Learning Log :**
>
| Date | Topics Reviewed | Learning Notes |
|---|---|---|
|---|---|---|

**Code Practice :**

---

## 0104. functions

| Sub-Topics |
|---|
| Creating Functions |
| Functions with Parameters, Functions with Default Parameters |
| Arguments (args and kwargs) |
| Functions with Return Values |
| Functions with Parameters and Return Values |
| Lambda Functions |
| Variable Scope |
| Return Keyword |

**Learning Log :**
>
| Date | Topics Reviewed | Learning Notes |
|---|---|---|
|---|---|---|

**Code Practice :**

---

## 0105. File.io

| Sub-Topics |
|---|
| File (open, write, read) |
| Reading and writing file text / CSV |

**Learning Log :**
>
| Date | Topics Reviewed | Learning Notes |
|---|---|---|
|---|---|---|

**Code Practice :**

---