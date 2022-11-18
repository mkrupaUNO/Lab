class Account:
    def __init__(self, name):
        self.account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if int(amount) > 0:
            self.__account_balance += int(amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        if (int(amount) <= self.__account_balance) and (int(amount) > 0):
            self.__account_balance -= int(amount)
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.account_name
