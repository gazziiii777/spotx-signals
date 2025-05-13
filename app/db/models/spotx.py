from tortoise import fields
from app.db.models.base import BaseModel

class SpotX(BaseModel):
    token = fields.CharField(max_length=255, unique=True)