#1

def natural(natur:int):
     if natur > 0:
          return natur
     else:
          print('Attention')



import collection

def factorial(natur):
     if natur == 1:
          return natur
     else:
          return natur * factorial(natur-1)

for nat in range(1,(1+natural(int(input(':'))))):
     if nat == 1:
         print('1')
     else:
         print(factorial(nat))


