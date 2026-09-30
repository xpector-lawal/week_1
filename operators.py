
#SIMPLE CALCULATOR

print("====CALCULATOR====")

num1 = float(input("Enter first value: "))
operators =input("Enter operator(+, -, *, %, /): ")
num2 = float(input("Enter second value: "))

if operators == "+":
    result = num1 + num2
elif operators == "-":
    result = num1-num2
elif operators == "*":
    result = num1*num2
elif operators == "%":
    result = num1%num2
elif operators == "/":
    if num2 !=0:
        result = num1/num2
    else:
        print("Error cannot divide by zero.")
        result = None
else:
    print("Invalid operator.")
    result = None
if result is not None:
    print("Result:", result)
