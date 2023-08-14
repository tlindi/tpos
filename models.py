from sqlite3 import Row
from typing import Optional

from fastapi import Query
from pydantic import BaseModel


class CreateTposData(BaseModel):
    wallet: Optional[str]
    name: Optional[str]
    currency: Optional[str]
    tip_options: Optional[str]
    tip_wallet: Optional[str]
    withdrawlimit: Optional[str]
    withdrawpin: Optional[str]
    withdrawamt: Optional[str]

class TPoS(BaseModel):
    id: str
    wallet: str
    name: str
    currency: str
    tip_options: Optional[str]
    tip_wallet: Optional[str]
    withdrawlimit: Optional[str]
    withdrawpin: Optional[str]
    withdrawamt: Optional[str]

    @classmethod
    def from_row(cls, row: Row) -> "TPoS":
        return cls(**dict(row))

class TPoSClean(BaseModel):
    id: str
    name: str
    currency: str
    tip_options: Optional[str]

    @classmethod
    def from_row(cls, row: Row) -> "TPoSClean":
        return cls(**dict(row))
    
class PayLnurlWData(BaseModel):
    lnurl: str
