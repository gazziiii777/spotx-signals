from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class SpotXCreateSchema(BaseModel):
    token: str  
    start_at: Optional[datetime] 
    end_at: Optional[datetime]    