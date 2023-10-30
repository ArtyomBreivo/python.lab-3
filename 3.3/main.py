#Сформировать (не программно) текстовый файл. В нём каждая
#строка должна описывать учебный предмет и наличие лекционных,
#практических и лабораторных занятий по предмету.
#Сюда должно входить и количество занятий. Необязательно,
#чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) 10(лаб)
#Физкультура: 30(пр)
#Пример словаря: {"Информатика": 170, "Физика": 40, "Физкультура":30}
# Откройте файл для чтения
# Откройте файл для чтения
with open('subjects.txt', 'r') as file:
    lines = file.readlines()
subject_data = {}
for line in lines:
    parts = line.split(':')
    if len(parts) == 2:
        subject = parts[0].strip()
        data = parts[1].split()
        total_lectures = 0
        total_practicals = 0
        total_lab = 0
        for item in data:
            if item.endswith('(lectures)'):
                total_lectures += int(item.split('(')[0])
            elif item.endswith('(practicals)'):
                total_practicals += int(item.split('(')[0])
            elif item.endswith('(labs)'):
                total_lab += int(item.split('(')[0])
        total_classes = total_lectures + total_practicals + total_lab
        subject_data[subject] = total_classes
print(subject_data)
