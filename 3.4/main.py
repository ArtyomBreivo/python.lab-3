#Создать вручную и заполнить несколькими строками текстовый файл,
#в котором каждая строка будет содержать данные о фирме: название, форма собственности,выручка, издержки.
#Пример строки файла: firm 1 000 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
#а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
#а также словарь со средней прибылью. Если фирма получила убытки,
#также добавить её в словарь (со значением убытков).
#Пример списка: [{"firm 1": 5000, "firm 2": 3000, "firm 3": 1000},
#{"average profit»: 2000}].
#Итоговый список сохранить в виде json-обьекта в соответствующий файл.
#Пример json-обьекта: [{"firm 1": 5000, "firm 2": 3000, "firm 3": 1000},
#{"average profit»: 2000}]
#Подсказка: использовать менеджер контекста.
import json
with open('companies.txt', 'r') as file:
    lines = file.readlines()
company_data = []
total_profit = 0
count_profitable_companies = 0
for line in lines:
    parts = line.split()
    if len(parts) == 4:
        company_name = parts[0]
        revenue = int(parts[2])
        costs = int(parts[3])
        profit = revenue - costs
        company_data.append({company_name: profit})
        if profit > 0:
            total_profit += profit
            count_profitable_companies += 1
average_profit = total_profit / count_profitable_companies if count_profitable_companies > 0 else 0
company_data.append({"average_profit": average_profit})
print(company_data)
with open('company_data.json', 'w') as json_file:
    json.dump(company_data, json_file)
