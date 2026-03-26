from datetime import datetime

with open("calculator.log", "r") as file:
    lines = file.readlines()
    for line in lines[-5:]:
        line = line.strip()
        print(line)

#запрос первого числа
while True:
    try:
        a = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Это не число. Попробуйте снова.")

#запрос второго числа
while True:
    try:
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Это не число. Попробуйте снова.")

print(f"Вы ввели числа: {a} и {b}")

#выбор операции
while True:
    operation = input("Выберите одну из операций: + - * / : ")
    if operation in ("+","-","*","/"):
        break
    else:
        print("Возможно вы выбрали не ту операцию. Попробуйте заново")

if operation == '+':
    result=a+b
    print(f'{a} + {b} = {result}')


elif operation == '-':
    result=a-b
    print(f'{a}-{b}={result}')


elif operation == '*':
    result=a*b
    print(f'{a}*{b}={result}')

elif operation == '/':
    if b == 0:
        print('Делить на ноль нельзя!')
    else:
        result=a/b
        print(f' {a}/{b}={result}')

#логирование
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

log_line = (f"[{timestamp}] {a} {operation} {b} = {result}")
print(log_line)

with open("calculator.log", "a", encoding="UTF-8") as file:
    file.write(log_line + "\n")

while True:
    clear_log = input("Хотите очистить лог? (да/нет): ").lower()
    if clear_log == "да":
        open("calculator.log", "w", encoding="UTF-8").close()
        print("Лог очищен.")
        break
    elif clear_log == "нет":
        print("Лог оставлен без изменений.")
        break
    else:
        print("Пожалуйста, введите только да или нет.")