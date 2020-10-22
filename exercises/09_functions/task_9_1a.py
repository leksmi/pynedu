# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт:
* ввести дополнительный ПАРАМЕТР, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Пример вызова функции:
print(generate_access_config(access_mode_template, access_config))
print(generate_access_config(access_mode_template, access_config, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


def generate_access_config(intf_vlan_mapping, access_template, *args, psecurity='None'):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_mode_template = []
    for intf in intf_vlan_mapping:
        access_mode_template.append('interface ' + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                access_mode_template.append('{} {}'.format(command, intf_vlan_mapping[intf]))
            else:
                access_mode_template.append(command)
        # if psecurity != 'None':                   # Проверка флага для необходимости добавить port-security команды
        if args:  # Если args не пустой, формируется кортеж
            for command in args[0]:  # Берем нулевой элемент кортежа (это переданный список) и берем его элементы
                access_mode_template.append(command)
    return access_mode_template


# Вызов функции как с двумя аргументами, так и с тремя (*args принимает на себя все, что после указанных параметров, формируя КОРТЕЖ)
# result = generate_access_config(access_config, access_mode_template)
result = generate_access_config(access_config, access_mode_template, port_security_template)

# Проверка (вывод) результата (списка):
for command in result:
    if command.startswith('interface'):
        print(f'\n{command}')
    else:
        print(command)
