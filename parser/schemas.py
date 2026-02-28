from pydantic import BaseModel
from typing import Any, Optional, Dict


class WbProductResponse(BaseModel):
    data: Dict[str, Any]

class WBProduct(BaseModel):
    id: int
    name: str
    price: int
    base_price: Optional[int] = None #без учета скидки

