class Transport:
    def __int__(self,name,max_speed,capacity,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = 50

def identity(self):
    print(f'Названание автомобиля', self.name,'его максимальная скорость',self.max_speed,'км/ч','пробег',self.mileage,'км.')
def seating_capacity(self,capacity):
    print(f'Вместимость одного автобуса',self.name,':',capacity,'пассажиров')

Autobus = Transport('Renault Logan',180,120000, 50)
identity(Autobus)


#2

seating_capacity('Renault LOgan, 50')
