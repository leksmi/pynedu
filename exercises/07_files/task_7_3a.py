# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

file_data = 'CAM_table.txt'

with open(file_data, 'r') as f:
    result_list = []
    for line in f:
        if not line.strip():
            continue
        line_list = line.split()
        if line_list[0].isdigit(): # Если первый элемент число (номер влана) то используем эту строку
            line_list.pop(2)       # Удаляем лишнее поле
            result_list.append(line_list)

# Преобразуем первую колонку из str в int для дальнейшей сортировки:
for line in result_list:
    line[0] = int(line[0])

# Сортировка по первому элементу (по умолчанию метода) который теперь - число. Список заменяется новым !:
result_list.sort()

# Окончательный вывод через форматирование:
for line in result_list:
    print(f'{line[0]:<7} {line[1]:<20} {line[2]:<10}')
