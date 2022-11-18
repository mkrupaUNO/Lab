class Account:
    """
    A class representing details for an account class
    """
    def __init__(self, name):
        """
        Constructor to create initial state of an account
        :param name: Person's first name
        """
        self.__account_name = name
        self.__account_balance = 0.00

    def deposit(self, amount):
        """
        Function to deposit money into account
        :param amount: the amount of money to deposit
        :return: True if the amount is greater than 0
        :return: False if the amount is less than 0
        """
        if float(amount) > 0:
            self.__account_balance += float(amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        """
        Function to withdraw money from account
        :param amount: the amount wanted to withdraw
        :return: True if amount is greater than 0 and less than the account balance
        :return: False if amount is less than 0 or greater than the account balance
        """
        if (float(amount) <= self.__account_balance) and (float(amount) > 0):
            self.__account_balance -= float(amount)
            return True
        else:
            return False

    def get_balance(self):
        """
        Function to return the account balance
        :return: The account's balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Function to return the account name
        :return: The account's name
        """
        return self.__account_name
