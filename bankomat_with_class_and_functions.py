'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

import decimal
import random

MIN_DIVIDER = 50
TAKE_OFF_TAX = 1.5 / 100
MAGIC_NUM = 3
EVERY_THIRD_TAX = 3 / 100
WEALTH = 5_000_000
WEALTH_TAX = 10 / 100

class ATM:

    count = 0

    def __init__(self, amount):
        self.amount = amount

    def take_wealth_tax(self):
        if self.amount > WEALTH:
            self.amount -= WEALTH_TAX * self.amount
    
    def every_third(self, summa):
        if self.count == MAGIC_NUM:
            self.amount += EVERY_THIRD_TAX * summa

    
    def take_off(self, summa: decimal) -> str:
        self.take_wealth_tax()
        self.every_third(summa)
        if summa % MIN_DIVIDER != 0:
            return f'Enter sum multiple to {MIN_DIVIDER}'
        elif summa > self.amount:
            return f'You have no enough money, on your account {self.amount} only'
        else: 
            if summa * TAKE_OFF_TAX > 600:
                self.amount -= summa + 600
            elif summa * TAKE_OFF_TAX < 30:
                self.amount -= summa + 30
            else:
                self.amount -= summa * (1 + TAKE_OFF_TAX)
            self.count += 1
            return f'You take off {summa}; now there is {self.amount} on your account'
        
    def put_on(self, summa: decimal) -> str:
        self.take_wealth_tax()
        self.every_third(summa)
        if summa % MIN_DIVIDER != 0:
            return f'Enter sum multiple to {MIN_DIVIDER}'
        else:
            self.amount += summa
            self.count += 1
            return f'You put on {summa}; now there is {self.amount} on your account'
        
    def user_choose_action(self) -> int:
        choice = int(input('''choose action:
                1- take off money
                2 - put on money
                3 - show the balance
                0 - exit
                '''))
        return choice
    
    def choosen_action (self, choice: int)-> None:
        match choice:
            case 1:
                summa = float(input('Enter sum you want to take off: '))
                print(self.take_off(summa))
            case 2:
                summa = float(input('Enter sum you want to put on: '))
                print(self.put_on(summa))
            case 3:
                print(f'There is {self.amount} on your account')
            




if __name__ == '__main__':
    atm_seanse = ATM(random.randint(5_000, 100_000))
    print(atm_seanse.count)
    
    while True:
        choice = atm_seanse.user_choose_action()
        if choice == 0:
            break
        else:
            atm_seanse.choosen_action(choice)
        
        



