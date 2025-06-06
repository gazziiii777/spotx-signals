from tortoise import fields
from app.db.models.base import BaseModel
from datetime import datetime
from typing import Optional


class SpotX(BaseModel):
    token = fields.CharField(max_length=255, unique=True)
    end_at: Optional[datetime] = fields.DatetimeField(null=True)
