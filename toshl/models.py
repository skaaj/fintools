from dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    id: str
    parent: Optional[str] = None
    name: Optional[str] = None
