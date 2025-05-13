from tortoise.models import Model
from tortoise import fields



class BaseModel(Model):
    id = fields.IntField(pk=True)


    class Meta:
        abstract = True
