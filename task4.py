def fun(a, b, op):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a / b)
        else:
            print("Division by zero is not allowed")
    elif op == "%":
        if b != 0:
            print(a % b)
        else:
            print("Modulus by zero is not allowed")
    else:
        print("Invalid operator")

print("Enter the values of a & b:")
a = int(input())
b = int(input())
print("Enter the operator (+, -, *, /, %):")
op = input()
fun(a, b, op)
