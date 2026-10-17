import pytest
from src.sigverify.ledger import Ledger


def test_ledger_starts_with_genesis():
    ledger = Ledger()
    assert len(ledger.chain) == 1
    assert ledger.chain[0].data["msg"] == "GENESIS_BLOCK"


def test_add_entry():
    ledger = Ledger()
    entry = ledger.add({"amount": 100, "to": "alice"})
    assert len(ledger.chain) == 2
    assert entry.data["amount"] == 100


def test_verify_valid():
    ledger = Ledger()
    ledger.add({"a": 1})
    ledger.add({"b": 2})
    assert ledger.verify() is True


def test_verify_tampered():
    ledger = Ledger()
    ledger.add({"x": 1})
    ledger.chain[1].data["x"] = 999  # แก้ไขข้อมูลย้อนหลัง
    assert ledger.verify() is False
