Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))
Operator = input("Enter operator (+ - * /): ")
match Operator:
    case "+":
        print(f"{Num1} + {Num2} = {Num1 + Num2:.2f}") 
    case "-":
        print(f"{Num1} - {Num2} = {Num1 - Num2:.2f}")
    case "*":
        print(f"{Num1} * {Num2} = {Num1 * Num2:.2f}")
    case "/":
        if Num2 != 0:
            print(f"{Num1} / {Num2} = {Num1 / Num2:.2f}")
        else:
            print("Error: cannot divide by zero")
    case _:
        print("Error: unknown operator")

