from pprint import pprint
from datetime import datetime
from os import listdir
import os

# Задача 1
with open ('recipes.txt', 'r', encoding= 'utf8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        quantity = int(file.readline().strip())
        lines = []
        for item in range(quantity):
            data = file.readline().strip().split('|')
            ingridients = {}
            for d in data:
                ingridients['ingredient_name'] = data[0]
                ingridients['quantity'] = data[1]
                ingridients['measure'] = data[2]
            lines.append(ingridients)
        cook_book[dish_name] = lines
        file.readline()

    pprint(cook_book)

# Задача 2
def get_shop_list_by_dishes(dishes, persons=int):
    shopping = {}
    for dish in dishes:
        for item in (cook_book[dish]):
            items_list = dict([(item['ingredient_name'],
                                {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
            if shopping.get(item['ingredient_name']):
                extra_item = (int(shopping[item['ingredient_name']]['quantity']) +
                              int(items_list[item['ingredient_name']]['quantity']))
                shopping[item['ingredient_name']]['quantity'] = extra_item
            else:
                shopping.update(items_list)

    pprint(shopping)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задача 3
directory = 'sorted'
files = os.listdir(directory)
data = {}
list = []
for d in files:
    with open (os.path.join(directory,d), encoding='utf8') as name:
        data [d] = name.readlines()
        l = d, len(data[d]), data[d]

    list.append(l)

def sort_key(e):
    return e[1]
sorted_list = sorted(list, key = sort_key)

# my_res = ("\n".join(map(str, sorted_list)))

resulted_file = open("result.txt", 'w', encoding='utf8')
for item in sorted_list:
    for el in item:
        resulted_file.write(f"{el}\n")