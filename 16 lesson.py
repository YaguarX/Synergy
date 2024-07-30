#1

class Cash:
    def __init__(self,initial_amount):
        self.balance = initial_amount

    def grow_up(self,amount):
        self.balance += amount

    def count_1000(self):
        return self.balance // 1000

    def take(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Недостаточно денег в касе')


cash_register = Cash(5000)
print(cash_register.count_1000())
cash_register.grow_up(4000)
print(cash_register.count_1000())
cash_register.take(7000)
print(cash_register.balance)


#2

class Turtle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print('Невозможно уменьшить s до значения меньше или равного 0')

    def count_moves(self,x2,y2):
        x_diff = abs(x2 - self.x)
        y_diff = abs(y2 = self.y)
        return (x_diff + y_diff) / self.s

t = Turtle(0,0,1)
t.go_up()
t.go_right()
print(t.x,t.y)
t.evolve()
print(t.s)
t.count_moves(3,4)

