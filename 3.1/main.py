with open('F1.txt', 'w') as f1:
    while True:
        data = input("Введите данные (пустая строка для завершения): ")
        if data == '':
           break
        f1.write(data + '\n')
with open('F1.txt', 'r')as f1, open('F2.txt', 'w') as f2:
    lines = f1.readlines()
k = int(input("Введите значение K (начиная с 0): "))
for i in range(k, min(k + 6, len(lines))):
    f2.write(lines[i])
    with open('F2.txt', 'r') as f2:
        data = f2.read()
vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in data if char in vowels)



