#lesson 3
1

animal = input('Вид вашего питомца:')
animal_id = input('Как вы его называете?:')
animal_age = input('А сколько ему годков?:')
print(f'Это{animal} по кличке {animal_id}.Возоаст:{animal_age}')

2

a = 'Dryopitecus'
b = 'Australopithecus'
c = 'Homo_erectus'
d = 'Homo_sapiens'
print('Этапы эволюции человека:')
print(a,b,c,d,sep=' => ')

#lesson 4

1


a = float(input('Первая сторона прямоугольника:'))
b = float(input('Вторая сторона прямоугольника:'))
x = (a + b)*2
y = (a * b)
print('Периметр прямоугольника равен:',x)
print('Площадь прямоугольника равна:',y)

#  ИЛИ
def Perimetr(a:int,b:int):
    return (a + b) * 2

def Square(a:int,b:int):
    return (a * b)
a = int(input(f'ВВедите первое число:'))
b = int(input(f'ВВедите второе число:'))
print(Perimetr(a,b))
print(Square(a,b))

2

a,b,c,d,e = map(int,input('Ваши пять чисел:').split())
fin_result = (d ** e) * c // (a-b)
print(float(fin_result))


#lesson#5

1

a = int(input(':'))

if a > 0 and a % 2 == 0:
    print('Положительное четное число')
elif a < 0 and a % 2 == 0:
    print('Отривательное четное число')
elif a > 0 and a % 2 != 0:
    print('Положительное нечетное число')
elif a < 0 and a % 2 != 0:
    print('Отрицательно нечетное число')
else:
    print('Это ведь ноль')

2

glas = ['а','е','я','о','ю','и','у']

glas_check = str(input(':'))
if glas_check in glas:
    print('True')
else:
    print('False')

3
mai = 10
iva = 6
game = 7

if mai > game and iva > game:
    print('2')
elif mai < game and iva > game:
    print('Иван')
elif mai > game and iva < game:
    print('Майкл')
if mai < game and iva < game:
    print('0')
else:
    print('1')


#lesson 6

#1,2 = unexpected

3

for i in range(a,b):
    if a < b and i % 2 == 0:
        print(i)

#lesson 7

1

n = int(input(':'))
b = []

for i in range(n):
    g = int(input(':'))
    b.append(g)
b.reverse()
print(b)


2

fir = int(input(':'))
sec = []

for i in range(fir):
    thr = int(input(':'))
    sec.append(thr)
print(sec[-1],sec[-2],sec[-3])







