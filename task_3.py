file = open("products.csv", "w")
file.write("Название,цена,количество\n")
file.write("Яблоко,100,50\n")
file.write("Бананы,80,30\n")
file.write("Молоко,120,20\n")
file.write("Хлеб,40,100\n")
file.close()

with open("products.csv", "r") as file:
    lines=file.readlines()
    for line in lines:
        line = line.strip()
        name, price, quantity = line.split(",")
        print(name, price, quantity)


#добавление нового товара
while True:
    new_name = input("Введите ваш товар: ")
    if new_name.lower() == "стоп":
        break
    new_price = int(input("Введите стоимость вашего товара: "))
    new_quanity = int(input("Введите количество вашего товара: "))

    new_line = f"{new_name},{new_price},{new_quanity}\n"

    lines.append(new_line)

    with open("products.csv", "w", encoding="UTF-8") as file:
        for line in lines:
            file.write(line)

    with open("products.csv", "r", encoding="UTF-8") as file:
        print(file.read())

#поиск товара
while True:
    search = input("Введите название товара: ")
    if search.lower() == "стоп":
        break
    found = False
    for line in lines:
        if search.lower() in line.lower():
            print("Найдено: ", line)
            found = True
    if not found:
        print("Товар не найден")


#общая стоимость товаров

total = 0
for line in lines[1:]:
    line = line.strip()
    name, price, quantity = line.split(",")

    price = int(price)
    quantity = int(quantity)

    total += price*quantity

print("Полная стоимость склада: ", total)