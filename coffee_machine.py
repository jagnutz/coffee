class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_bean = 120
        self.disposable_cup = 9
        self.money = 550
        self.status = True

    def mode(self):
        while self.status:
            mode = input('Write action (buy, fill, take, remaining, exit): \n')
            if mode == 'exit':
                self.status = False
            elif mode == 'buy':
                mode = input('What do you want to buy? 1 - espresso, 2 - latte,'
                             ' 3 - cappuccino, back - to main menu: \n')
                if mode == '1':
                    self.espresso()
                elif mode == '2':
                    self.latte()
                elif mode == '3':
                    self.cappuccino()
                elif mode == 'back':
                    pass
            elif mode == 'fill':
                self.refill()
            elif mode == 'take':
                self.withdraw()
            elif mode == 'remaining':
                self.supplies()

    def supplies(self):
        print('\nThe coffee machine has: ')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_bean} of coffee beans')
        print(f'{self.disposable_cup} of disposable cups')
        print(f'${self.money} of money\n')

    def espresso(self):
        if self.water < 250:
            print('Sorry, not enough water! \n')
        elif self.coffee_bean < 16:
            print('Sorry, not enough coffee bean! \n')
        elif self.disposable_cup < 1:
            print('Sorry, not enough disposable cups! \n')
        else:
            print('I have enough resources, making you a coffee! \n')
            self.water -= 250
            self.coffee_bean -= 16
            self.disposable_cup -= 1
            self.money += 4

    def latte(self):
        if self.water < 350:
            print('Sorry, not enough water! \n')
        elif self.milk < 75:
            print('Sorry, not enough milk! \n')
        elif self.coffee_bean < 20:
            print('Sorry, not enough coffee bean! \n')
        elif self.disposable_cup < 1:
            print('Sorry, not enough disposable cups! \n')
        else:
            print('I have enough resources, making you a coffee! \n')
            self.water -= 350
            self.milk -= 75
            self.coffee_bean -= 20
            self.disposable_cup -= 1
            self.money += 7

    def cappuccino(self):
        if self.water < 200:
            print('Sorry, not enough water! \n')
        elif self.milk < 100:
            print('Sorry, not enough milk! \n')
        elif self.coffee_bean < 12:
            print('Sorry, not enough coffee bean! \n')
        elif self.disposable_cup < 1:
            print('Sorry, not enough disposable cups! \n')
        else:
            print('I have enough resources, making you a coffee! \n')
            self.water -= 200
            self.milk -= 100
            self.coffee_bean -= 12
            self.disposable_cup -= 1
            self.money += 6

    def refill(self):
        self.water += int(input('Write how many ml of water do you want to add: \n'))
        self.milk += int(input('Write how many ml of milk do you want to add: \n'))
        self.coffee_bean += int(input('Write how many grams of coffee beans do you want to add: \n'))
        self.disposable_cup += int(input('Write how many disposable cups of coffee do you want to add: \n'))

    def withdraw(self):
        print(f'I gave you ${self.money} \n')
        self.money = 0


coffee = CoffeeMachine()
coffee.mode()
