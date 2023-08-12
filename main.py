class User:
    def __init__(self,name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance+=amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self
    def display_user_balance(self):
        print (f"User:{self.name},solde:{self.account_balance}")
        return self
    def transfer_money(self, amount,user):
        self.account_balance-=amount
        user.account_balance+=amount
        self.display_user_balance()
        user.display_user_balance()
        return self
guido = User ("guido van rossum")
#guido.make_deposit(3000)
#guido.make_withdrawal(150)
#guido.display_user_balance()
monty=User("mounty van rossum")
#guido.transfer_money(500,monty)
guido.make_deposit(2000).make_withdrawal(200).display_user_balance().transfer_money(500,monty)