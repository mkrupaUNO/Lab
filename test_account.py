from account import *


class Test:
    def setup_method(self):
        self.a1 = Account("Bob")
        self.a2 = Account("Kristy")

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == "Bob"
        assert self.a1.get_balance() == 0

        assert self.a2.get_name() == "Kristy"
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(250) is True
        assert self.a1.get_balance() == 250.00
        assert self.a1.deposit(-5) is False
        assert self.a1.get_balance() == 250.00
        assert self.a1.deposit(15.75) is True
        assert self.a1.get_balance() == 265.75

        assert self.a2.deposit(2500) is True
        assert self.a2.get_balance() == 2500.00
        assert self.a2.deposit(-10) is False
        assert self.a2.get_balance() == 2500.00
        assert self.a2.deposit(10.75) is True
        assert self.a2.get_balance() == 2510.75

    def test_withdraw(self):
        self.a1.deposit(100)
        assert self.a1.withdraw(25.50) is True
        assert self.a1.get_balance() == 74.50
        assert self.a1.withdraw(-20) is False
        assert self.a1.get_balance() == 74.50
        assert self.a1.withdraw(75) is False
        assert self.a1.get_balance() == 74.50
        assert self.a1.withdraw(74.50) is True
        assert self.a1.get_balance() == 0.00

        self.a2.deposit(1000)
        assert self.a2.withdraw(250.50) is True
        assert self.a2.get_balance() == 749.50
        assert self.a2.withdraw(-20) is False
        assert self.a2.get_balance() == 749.50
        assert self.a2.withdraw(750) is False
        assert self.a2.get_balance() == 749.50
        assert self.a2.withdraw(749.50) is True
        assert self.a2.get_balance() == 0.00
