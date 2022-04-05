# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:51:47 2022

@author: U268137
"""

result  = []
for num1 in range(1, 10):
    tmp = []
    for num2 in range(1, 10):
        tmp.append(f'{num1 * num2:2}')
    result.append(tmp)

for row in result:
    print(', '.join(row))