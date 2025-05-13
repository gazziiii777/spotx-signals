from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SpotXCreateSchema(BaseModel):
    token: str
    end_at: Optional[datetime]
