class User:
    counter = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=.02, balance=0)
        User.counter += 1
    # adding the deposit method

    # takes an argument that is the amount of the deposit, then increments the balance by that amount
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # takes an argument that is the amount of the withdrawl, then deincrements the balance by that amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):  # takes no argument, self is implied
        # Checks if the user is overdrafted
        # Then prints the respective user's balance
        if self.account_balance >= 0:
            print(f"{self.name}'s balance is: {self.account_balance}")
        else:
            print(f"{self.name} has overdrafted. Balance is: {self.account_balance}")
        return self
    # takes 2 arguments: one for the user who receives the money, another for the amount

    def transfer_money(self, other_user, amount):
        # calls the withdrawl function for the user who is transferring; then calls the deposit function for the other user - both by the amount
        if User.counter > 1:
            User.make_withdrawal(self, amount)
            User.make_deposit(other_user, amount)
        else:
            print("Cannot transfer: there is only one User instance.")
        return self


class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        else:
            print("Balance is negative")
        return self


# instantiate two
john = BankAccount(int_rate=.08)
jason = BankAccount()
# test methods on both accounts
john.deposit(10).deposit(20).deposit(30).withdraw(
    10).yield_interest().display_account_info()
jason.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(
    25).withdraw(25).yield_interest().display_account_info()
# Create three instances
john = User("John Doe", "johnDoe@doeDomain.com")
jason = User("Jason Doe", "jasonDoe@doeDomain.com")
julie = User("Julie Doe", "julieDoe@doeDoamin.com")
# Make three deposits, one withdrawl, then display balance
john.make_deposit(45).make_deposit(5).make_deposit(
    15).make_withdrawal(3).display_user_balance()
# Second user makes 2 deposits, 2 withdrawls, then displays balance
jason.make_deposit(100).make_deposit(100).make_withdrawal(
    5).make_withdrawal(10).display_user_balance()
# Third user makes 1 deposit, 3 withdrawls, then displays balance
julie.make_deposit(100).make_withdrawal(40).make_withdrawal(
    50).make_withdrawal(60).display_user_balance()
# Second user transfers money to the third user, prints both balances
jason.transfer_money(julie, 50).display_user_balance()
julie.display_user_balance()
