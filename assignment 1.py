op = input("please select your operation(+ , - , * , / , sin , cos , tan , cot , ! , sqrt ): ")



import math

if op == "+":
    num1 = float(input("enter num1: "))
    num2 = float(input("enter num2: "))
    result = num1 + num2

if op == "-":
    num1 = float(input("enter num1: "))
    num2 = float(input("enter num2: "))
    result = num1 - num2

if op == "*":
    num1 = float(input("enter num1: "))
    num2 = float(input("enter num2: "))
    result = num1 * num2

if op == "/":
    num1 = float(input("enter num1: "))
    num2 = float(input("enter num2: "))
    if num2 == 0:
        result = "undefined"
    else:
        result = num1 / num2
        

if op == "sin":
    num1 = int(input("enter angle(in drgrees): "))
    x = math.radians(num1)
    result = math.sin(x)


if op == "cos":
    num1 = int(input("enter angle(in drgrees): "))
    x = math.radians(num1)
    result = math.cos(x)
 
if op == "tan":
    num1 = int(input("enter angle(in drgrees): "))
    x = math.radians(num1)
    result = math.tan(x)

if op == "cot":
    num1 = int(input("enter angle(in drgrees): "))
    x = math.radians(num1)
    y = math.tan(x)

    if y == 0:
        result = "undefined"
    else:
        result = 1 / math.tan(num1)

if op == "!":
    num1 = int(input("enter your number: "))
    result = math.factorial(num1) 

if op == "sqrt":
   num1 = float(input("enter num1: "))

   if num1 < 0:
        result = "undefined"
   else:
        result = math.sqrt(num1)







print(result)                  

