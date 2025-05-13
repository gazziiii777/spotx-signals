from tortoise.models import Model
from tortoise import fields
from datetime import datetime
from typing import Optional


class BaseModel(Model):
    id = fields.IntField(pk=True)
    start_at: Optional[datetime] = fields.DatetimeField(
        null=True)  # Можно явно установить или оставить None
    end_at: Optional[datetime] = fields.DatetimeField(null=True)

    class Meta:
        abstract = True
