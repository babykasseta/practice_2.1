file = open("students.txt" , "w")
file.write("Иванов Иван:5,4,3,5 \n")
file.write("Петров Петр:4,3,4,4 \n")
file.write("Сидорова Мария:5,5,5,5 \n")
file.close()

with open("students.txt", "r") as file:
    lines=file.readlines()

best_name = ""
best_avg = 0

with open("result.txt", "w") as result_file:
    for line in lines:
        line=line.strip()
        name, grades = line.split(":")
        grades_list = grades.split(",")
        grades_nums = list(map(int,grades_list))
        sr_bal = sum(grades_nums) / len(grades_nums)

        if sr_bal >4.0:
            result_file.write(f"{name}: {sr_bal}\n")

        if sr_bal > best_avg:
            best_name = name
            best_avg = sr_bal
print(f"Лучший студент: {best_name}, со средним баллом: {best_avg}")


