
num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /, //, %, ^): ")
num2 = float(input("Введите второе число: "))

if operation == "+":
    print("Результат:", num1 + num2)

elif operation == "-":
    print("Результат:", num1 - num2)

elif operation == "*":
    print("Результат:", num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", num1 / num2)

elif operation == "//":
    if num2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", num1 // num2)

elif operation == "%":
    if num2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", num1 % num2)

elif operation == "^":
    print("Результат:", num1 ** num2)

else:
    print("Ошибка: неизвестная операция!")