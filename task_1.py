file = open("text.txt", "w")
file.write(input("Напишите первую строку:\n") + "\n")
file.write(input("Напишите вторую строку:\n") + "\n")
file.write(input("Напишите третью строку:\n") + "\n")
file.write(input("Напишите четвёртую строку:\n") + "\n")
file.write(input("Напишите пятую строку:\n") + "\n")
file.close()

with open ("text.txt", "r") as file:
    lines = len(file.readlines())

with open ("text.txt", "r") as file:
    text = file.read()
words = text.split()
words_count = len(words)
longest_word = max(words, key=len).strip()


print("Количество строк в файле: ", lines)
print("Количество слов в файле: ", words_count)
print("Самую длинную строку: ", longest_word)