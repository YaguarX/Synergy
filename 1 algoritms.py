#1
Ответ на вопрос: Да, можно не с самого начала или не до конца. Для этого создадлим новую переменную, вот пример

import random

n = 10

arr = list()

for i in range(n):
    number = random.randint(1,20)
    arr.append(number)
print('not sorted', arr)

sub_arr = arr[2:6]

for i in range(n):
    for j in range(n-1):
        left = arr[j]
        right = arr[j+1]
    if left > right:
        arr[j] = right
        arr[j+1] = left
print('sorted', sub_arr)

#2

Добавим переменную-счетчик, при уже сделанной сортировке, она обнулится, так и поймем, была ли сортировка

import random

n = 10

arr = list()

for i in range(n):
    number = random.randint(1,20)
    arr.append(number)
print('not sorted', arr)

sub_arr = arr[2:6]

was_sorted = 1
if was_sorted > 0:
    for i in range(n):
        for j in range(n-1):
            left = arr[j]
            right = arr[j+1]
        if left > right:
            arr[j] = right
            arr[j+1] = left
    print('sorted', sub_arr)
    was_sorted = was_sorted - 1
else:
    print('already_sorted')