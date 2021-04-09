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
        user.counter += 1
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        if user.counter > 1:
            print("hi")
        else:
            print("Cannot transfer: there is only one User instance.")


jon = User("Jon Doe", "jonDoe@doeDomain.com")
print(jon.name)
