# -*- coding: utf-8 -*-
"""
Задание 9.2

Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

У функции должны быть такие ПАРАМЕТРЫ:
- intf_vlan_mapping: ожидает как АРГУМЕНТ словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как АРГУМЕНТ шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_mode_template.
В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config и списка команд trunk_mode_template.
Если предыдущая проверка прошла успешно, проверить работу функции еще раз на словаре trunk_config_2
и убедится, что в итоговом списке правильные номера интерфейсов и вланов.


Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

# Итоговый список команд для заполнения:
config_trunk = []


def generate_trunk_config(intf_vlan_mapping, trunk_template):  #
    # Перебираем интерфейсы (элементы словаря пары имя_интерфейса + вланы в нем)
    for intf in intf_vlan_mapping:
        config_trunk.append(f'interface {intf}')
        # Перебираем команды для интерфейса
        for command in trunk_template:
            # Проверка на необходимость подставить список вланов
            if command.endswith('allowed vlan'):
                # Так как в задании вланы в словаре заданы списком из int, преобразовываем его в str:
                vlans = str(intf_vlan_mapping[intf]).strip('[]')
                config_trunk.append(f'{command} {vlans}')
            else:
                config_trunk.append(command)

    return config_trunk


# Проверка работы:
result = generate_trunk_config(trunk_config_2, trunk_mode_template)

for command in result:
    if command.startswith('interface'):
        print(f'\n{command}')
    else:
        print(command)
