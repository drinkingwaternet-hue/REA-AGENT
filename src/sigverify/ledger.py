import hashlib
import json
from datetime import datetime, timezone
from typing import List, Optional


class LedgerEntry:
    def __init__(self, data: dict, prev_hash: str, signature: Optional[str] = None):
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.data = data
        self.prev_hash = prev_hash
        self.signature = signature
        self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        payload = json.dumps({
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
        }, sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
            "hash": self.hash,
            "signature": self.signature,
        }


class Ledger:
    def __init__(self):
        self.chain: List[LedgerEntry] = []
        self._genesis()

    def _genesis(self):
        genesis = LedgerEntry(data={"msg": "GENESIS_BLOCK"}, prev_hash="")
        self.chain.append(genesis)

    def add(self, data: dict, signature: Optional[str] = None) -> LedgerEntry:
        prev = self.chain[-1]
        entry = LedgerEntry(data=data, prev_hash=prev.hash, signature=signature)
        self.chain.append(entry)
        return entry

    def verify(self) -> bool:
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.prev_hash != prev.hash:
                return False
            if curr.hash != curr._compute_hash():
                return False
        return True
