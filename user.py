# For this assignment, we'll add some functionality to the User class:
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    counter = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        User.counter += 1
    # adding the deposit method

    # takes an argument that is the amount of the deposit, then increments the balance by that amount
    def make_deposit(self, amount):
        self.account_balance += amount

    # takes an argument that is the amount of the withdrawl, then deincrements the balance by that amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):  # takes no argument, self is implied
        # Checks if the user is overdrafted
        # Then prints the respective user's balance
        if self.account_balance >= 0:
            print(f"{self.name}'s balance is: {self.account_balance}")
        else:
            print(f"{self.name} has overdrafted. Balance is: {self.account_balance}")

    # takes 2 arguments: one for the user who receives the money, another for the amount
    def transfer_money(self, other_user, amount):
        # calls the withdrawl function for the user who is transferring; then calls the deposit function for the other user - both by the amount
        if User.counter > 1:
            User.make_withdrawal(self, amount)
            User.make_deposit(other_user, amount)
        else:
            print("Cannot transfer: there is only one User instance.")


# Create three instances
john = User("John Doe", "johnDoe@doeDomain.com")
jason = User("Jason Doe", "jasonDoe@doeDomain.com")
julie = User("Julie Doe", "julieDoe@doeDoamin.com")
# Make three deposits, one withdrawl, then display balance
john.make_deposit(45)
john.make_deposit(5)
john.make_deposit(15)
john.make_withdrawal(3)
john.display_user_balance()
# Second user makes 2 deposits, 2 withdrawls, then displays balance
jason.make_deposit(100)
jason.make_deposit(100)
jason.make_withdrawal(5)
jason.make_withdrawal(10)
jason.display_user_balance()
# Third user makes 1 deposit, 3 withdrawls, then displays balance
julie.make_deposit(100)
julie.make_withdrawal(40)
julie.make_withdrawal(50)
julie.make_withdrawal(60)
julie.display_user_balance()
# Second user transfers money to the third user, prints both balances
jason.transfer_money(julie, 50)
jason.display_user_balance()
julie.display_user_balance()
