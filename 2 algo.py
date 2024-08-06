#1

def change_to_binary(n):
    if n >= 2:
        change_to_binary(n // 2)
    print(n % 2 , end='')

change_to_binary(5)

#2

def recurs_mult(a,b):
    if b == 0:
        return 0
    elif b > 0:
        return a + recurs_mult(a, b- 1)
    else:
        return -recurs_mult(a, -b)

result = recurs_mult(2,3)
print(f'Результат: {result}')


#3

def recurs_step(a,n):
    if n == 0:
        return 1
    elif n > 0:
        return a * recurs_step(a, n - 1)
    else:
        return 1 / recurs_step(a, -n)

result = recurs_step(3,4)
print(f'Возведя число в степень получим: {result}')