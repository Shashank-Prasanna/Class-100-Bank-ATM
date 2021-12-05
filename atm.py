from colorama import init, Fore, Back, Style
import json
init()

cardNumber = input(Fore.BLUE + 'Enter your card number: ')
pin = input(Fore.BLUE + 'Enter your pin: ')
print('\n')

class atm():
    def __init__(self, cardNumber, pin):
        print(Fore.BLUE + 'Hello! Welcome to the ATM')
        self.cardNumber = cardNumber
        self.pin = pin
        self.balanceEnquiry()

    def balanceEnquiry(self):
        print(Fore.GREEN + 'Getting Balance...')
        print(Style.RESET_ALL)
        f = open('Projects\Bank ATM\data.json')
        data = json.load(f)
        balance = data['customers'][cardNumber]['balance']
        balance = str(balance)
        print('Your balance is: $' + balance)

exampleATM = atm(cardNumber, pin)
exampleATM