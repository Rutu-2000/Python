class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
       self.name = name
       self.power = power

    def attack(self):
        print('attacking with power of{self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
       self.name = name
       self.num_arrows = num_arrows
    
    def attack(self):
       print('attacking with power of{self.arrows}')

Wizard1 = Wizard('Marline',60)
print(isinstance(Wizard1,Wizard))