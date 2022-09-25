import unittest

class Account:
    def __init__(self, amount_of_money: int):
        self.amount_of_money = amount_of_money

    def get_amount_of_money(self):
        return self.amount_of_money

    def set_amount_of_money(self, money):
        self.amount_of_money = money
        return self.amount_of_money

    def deposit_money(self, deposit_amount):
        new_account_value = self.get_amount_of_money() + deposit_amount
        account_value = self.set_amount_of_money(new_account_value)
        return account_value

    def withdraw_money(self, withdraw_money):
        if self.get_amount_of_money() < withdraw_money:
            print("Not enough balance")
            return False, self.get_amount_of_money()
        else:
            withdraw_value = self.get_amount_of_money() - withdraw_money
            account_value = self.set_amount_of_money(withdraw_value)
            return True, account_value



class UnitTest(unittest.TestCase):

    def test_deposit_money(self):
        account1 = Account(100)
        deposit = account1.deposit_money(100)
        self.assertEqual(200, account1.get_amount_of_money())

    def test_withdraw_money_positive(self):
        account2 = Account(100)
        result, withdraw = account2.withdraw_money(50)
        self.assertTupleEqual((True, 50), (result, withdraw))

    def test_withdraw_money_negative(self):
        account3 = Account(100)
        result, withdraw = account3.withdraw_money(200)
        self.assertTupleEqual((False, 100), (result, withdraw))

    def test_withdraw_money_equal(self):
        account4 = Account(100)
        result, withdraw = account4.withdraw_money(100)
        self.assertTupleEqual((True, 0), (result, withdraw))