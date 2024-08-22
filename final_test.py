# pytest final_test.py do this check if it passes all test cases
import pytest
from unittest.mock import patch, mock_open, MagicMock
from test_finalw2024 import Account, Customer, ATM



def test_account_initialization():
    acc = Account(balance=100, accountNumber=12345678)
    assert acc.getAccountNumber() == 12345678
    assert acc.getBalance() == 100

def test_account_initialization_random_account_number():
    acc = Account(balance=100)
    assert 10000000 <= acc.getAccountNumber() <= 99999999

def test_account_initialization_balance_as_string():
    acc = Account(balance="100")
    assert acc.getBalance() == 100

def test_account_deposit():
    acc = Account(balance=100)
    acc.deposit(50)
    assert acc.getBalance() == 150

def test_account_withdraw():
    acc = Account(balance=100)
    acc.withdraw(50)
    assert acc.getBalance() == 50

def test_account_withdraw_insufficient_funds():
    acc = Account(balance=100)
    acc.withdraw(150)
    assert acc.getBalance() == 100

def test_account_transactions():
    acc = Account(balance=100)
    acc.deposit(50)
    acc.withdraw(30)
    assert acc.getTransactions() == ["Deposited 50", "Withdrew 30"]

# Test Customer class
def test_customer_initialization():
    cust = Customer(name="John Doe", balance=100)
    assert cust.getName() == "John Doe"
    assert 1000 <= cust.getPin() <= 9999

def test_customer_pin_creation():
    cust = Customer(name="John Doe", balance=100)
    old_pin = cust.getPin()
    cust.createPin()
    assert old_pin != cust.getPin()

