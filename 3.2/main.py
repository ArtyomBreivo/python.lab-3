with open('flowers.txt', 'r') as file:
    lines = file.readlines()
expensive_flowers = []
total_cost = 0
for line in lines:
    parts = line.split()
    if len(parts) == 2:
        flower_name = parts[0]
        cost = int(parts[1])
        total_cost += cost
        if cost > 10:
            expensive_flowers.append(flower_name)
print("Цветы дороже 10 рублей:")
for flower in expensive_flowers:
    print(flower)
average_cost = total_cost / len(lines)
print(f"Средняя стоимость всех цветов: {average_cost} рублей")
