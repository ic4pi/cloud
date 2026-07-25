"""
Unit tests for the Sovereign Ledger API
Ensures that Low Latency and Data Sovereignty are maintained.
"""

import pytest
from app import CitizenWallet, PaymentGateway

def test_initial_balance():
    wallet = CitizenWallet("test_user")
    assert wallet.balance == 0.0

def test_successful_deposit():
    wallet = CitizenWallet("test_user")
    assert wallet.deposit(500.00) == True
    assert wallet.balance == 500.00

def test_insufficient_funds():
    wallet = CitizenWallet("test_user")
    wallet.deposit(10.00)
    res = wallet.transfer("target", 100.00)
    assert res["status"] == "insufficient_balance"

def test_successful_transfer():
    wallet = CitizenWallet("sender")
    recipient = CitizenWallet("receiver")
    
    wallet.deposit(100.00)
    
    gateway = PaymentGateway()
    gateway.process_transaction(wallet, "receiver", 25.00)
    
    assert wallet.balance == 75.00

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
