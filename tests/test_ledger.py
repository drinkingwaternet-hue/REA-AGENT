import sys
from pathlib import Path

# เพิ่มโฟลเดอร์ src เข้าไปในเส้นทางค้นหาโมดูล
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from sigverify.ledger import Ledger


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
    # จำลองการแก้ไขข้อมูลย้อนหลัง
    ledger.chain[1].data["x"] = 999
    assert ledger.verify() is False
