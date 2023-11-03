from random import randint

class Symbol:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def printSymbol(self):
        print(self.value, end=" ")

    def getValue(self):
        return self.value

symbol_list = [Symbol("!", 1), Symbol("@", 1.25), Symbol("#", 1.5), Symbol("%", 1.75), 
               Symbol("&", 2), Symbol("*", 2.5), Symbol("+", 3), Symbol("^", 4), Symbol("-", 5), Symbol("$", 10)]

class Slots:
    def __init__(self, symbols, balance):
        self.symbols = symbols
        self.balance = balance

    def Spin(self, bet):
        if bet <= 0 or bet > self.balance:
            print("Invalid bet. Please bet a positive amount within your balance.")
            return
        result = ["", "", ""]
        print("\n-----------")
        print("| ",end=" ")
        for i in range(len(result)):
            result[i] = self.symbols[randint(0, len(symbol_list)-1)]
            result[i].printSymbol()
        print(" |")
        print("-----------\n")

        if result[0].value == result[1].value == result[2].value:
            print("You won!")
            self.balance += bet * result[0].weight
        else:
            print("You lost.")
            self.balance -= bet

print("Welcome to the slot machine!")
run = True
Balance = 1000
    
while run:
    bet = int(input("How much would you like to bet?: $"))
    round = Slots(symbol_list, Balance)
    
    if Balance <= 0:
        print("You ran out of money. Thanks for playing!")
        run = False
        continue
    
    round.Spin(bet)
    if round.balance > 0:
        Balance = round.balance
        print("Your remaining balance is: $" + str(Balance))
        cont = input("Continue? (Y/N): ")
        if cont.lower() == "n":
            print("Thanks for playing.")
            run = False