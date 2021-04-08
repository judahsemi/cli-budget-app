import os
import time
import random
import math



class Budget():
    def __init__(self, name):
        # Ensure name is a string
        if not isinstance(name, str):
            msg = "Expected cat_name to be of type str, got '{}'."
            raise TypeError(msg.format(type(value)))
            
        self.name = name
        self.balance = 0.0

    def deposit_funds(self, amount):
        self.validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw_funds(self, amount):
        self.validate_amount(amount)
        if amount < self.balance:
            msg = "Transaction failed due to insufficient funds."
            raise ValueError(msg)
            
        self.balance -= amount
        return self.balance

    def transfer_funds(self, amount, to_cat):
        # Ensure to_cat is a Budget object
        if not isinstance(to_cat, Budget):
            msg = "Expected to_cat to be of type Budget, got '{}'."
            raise TypeError(msg.format(type(value)))
            
        self.withdraw_funds(amount)
        to_cat.deposit_funds(amount)
        return self.balance, to_cat.balance
    
    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, (int, float)):
            msg = "Expected amount to be of type int or float, got '{}'."
            raise TypeError(msg.format(type(value)))
            
        if amount < 0.0:
            msg = "Expected amount to greater than 0.0, got '{}'."
            raise ValueError(msg.format(amount))
    
    def __repr__(self):
        return "<Budget Catergory: {}, #{:.2f}>".format(self.name, self.balance)

