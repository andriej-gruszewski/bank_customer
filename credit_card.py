import random
import datetime
from account import Account
import unittest

class Credit_Card:
    def __init__(self, expiry_date: datetime, name: str, account: Account):
        self.expiry_date = expiry_date
        self.name = name
        self.account = account
        self.card_number = random.randint(1000000000, 9999999999)

    def pay(self, payment_value):
        result, value = self.account.withdraw_money(payment_value)
        return result, value


class UnitTest(unittest.TestCase):

    def test_pay(self):
        account1 = Account(100)
        today = datetime.datetime.today()
        credit_card1 = Credit_Card(today, "Andrzej Gruszewski", account1)
        pay = credit_card1.pay(50)
        self.assertTupleEqual((True, 50), pay)



