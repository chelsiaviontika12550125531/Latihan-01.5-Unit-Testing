class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner                  #nama nasabah
        self.balance = balance              #saldo nasabah

    def deposit(self, amount):              #ketika memasukkan uang
        if amount > 0:          
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be greater than zero")

    def withdraw(self, amount):             #ketika menarik saldo
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):                  #mengecheck saldo
        return self.balance
    
# unit testing
import unittest
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("chelsia", 100000)
        self.account2 = BankAccount("viontika", 50000)

    def test_deposit(self):
        self.account1.deposit(50000)
        self.account2.deposit(2500)

        self.assertEqual(self.account1.balance, 150000)
        self.assertEqual(self.account2.balance, 52500)

    def test_withdraw(self):
        self.account1.withdraw(40000)
        self.account2.withdraw(500)

        self.assertEqual(self.account1.balance, 60000)
        self.assertEqual(self.account2.balance, 49500)

    def test_get_balance(self):
        self.assertEqual(self.account1.get_balance(), 100000)
        self.assertEqual(self.account2.get_balance(), 50000)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(-100)

    def test_withdraw_invalid(self):
        with self.assertRaises(ValueError):
            self.account2.withdraw(100000)


if __name__ == "__main__":
    unittest.main()