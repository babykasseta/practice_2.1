with open("calculator.log", "r") as file:
    lines = file.readlines()
    for line in lines[-5:]:
        line = line.strip()
#запрос первого числа
while True:
    try:
        num1 = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Это не число. Попробуйте снова.")

#запрос второго числа
while True:
    try:
        num2 = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Это не число. Попробуйте снова.")

print(f"Вы ввели числа: {num1} и {num2}")

#выбор операции
while True:
    try:
        operation = input("Выберите одну из операций: + - * /"):
        break
    except ValueError:
        print("Возможно вы выбрали не ту операцию. Попробуйте заново")