from bson import ObjectId
from pydantic import BaseModel as PydanticBaseModel
from typing import Optional
from pydantic import Field


class PyObjectId(ObjectId):
    """https://python.plainenglish.io/how-to-use-fastapi-with-mongodb-75b43c8e541d"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class DBBaseModel(PydanticBaseModel):
    """https://pydantic-docs.helpmanual.io/usage/model_config/#change-behaviour-globally"""

    id: Optional[PyObjectId] = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
