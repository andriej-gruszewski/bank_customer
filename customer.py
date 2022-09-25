import datetime
from account import Account
from credit_card import Credit_Card

class Customer:
    def __init__(self, first_name: str, second_name: str, email: str):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.account = Account(0)
        credit_card1 = Credit_Card(self.get_expiry_date(3), first_name + second_name, self.account)
        self.credit_card_list = [credit_card1]

    def get_expiry_date(self, years):
        today = datetime.datetime.today()
        expiry_date = today + datetime.timedelta(days = 365 * years)
        return expiry_date

    def get_account(self):
        return self.account

    def create_credit_card(self, expiry_years):
        credit_card2 = Credit_Card(self.get_expiry_date(expiry_years), self.first_name + self.second_name,
                                   self.account)
        self.credit_card_list.append(credit_card2)
        return self.credit_card_list



import unittest

class UnitTest(unittest.TestCase):

    def test_customer_operations(self):
        customer1 = Customer("Bob", "Smith", "357@hotmail.com")
        customer1.account.deposit_money(deposit_amount=500)
        customer1.create_credit_card(3)
        customer1.credit_card_list[0].pay(200)
        self.assertEqual(300, customer1.account.get_amount_of_money())
        customer1.credit_card_list[1].pay(100)
        self.assertEqual(200, customer1.account.get_amount_of_money())

