from typing import Any, Optional
from pydantic import BaseModel


class ResponseModel(BaseModel):
    response: Any
    message: Optional[str]
