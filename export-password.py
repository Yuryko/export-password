#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# автор Козлов Юрий Евгеньевич git@github.com:Yuryko/export-password.git
# Скрипт должен распарсит заметку markdown на множетство шифрованных заметок
# внутри которы будет один единственный логин и пароль

import os
import re
import argparse

parser=argparse.ArgumentParser(
    description=''' Скрипт должен распарсит заметку markdown на множетство шифрованных заметок''',
    epilog=""" В результате работы скрипта будет сформирован каталог pass с заметками """)


# между первыми // и / находится сайт, который и будет заголовком 

def parce():
    if not os.path.exists('pass'):
        os.makedirs('pass')

    with open('pass.md') as file_new:
        lines = file_new.readlines()
        for line in lines:
            if '//' in line: # если содержит '//' делаем замету
                tmp = line                
                tmp = re.sub(r'(http).*?(//)', r'', tmp) # убираем преамбулу
                tmp = re.sub(r'www.', r'', tmp) # убираем преамбулу
                tmp = re.sub(r'/.*', r'.md', tmp) #убираем все, что после
                tmp = tmp.rstrip("\n")
                print(tmp)  
                # открываем новую заметку
                text = open('pass/{}'.format(tmp), "w")
                text.write(line)
                text.close() # закрываем последнюю заметку

parce()