from bson import ObjectId
from pydantic import BaseModel, PrivateAttr, Field, schema
from typing import Any
from datetime import datetime
import random
import string
from bson.decimal128 import Decimal128
from base_common import settings


class DBBaseModel(BaseModel):
    # * https://pydantic-docs.helpmanual.io/usage/model_config/#change-behaviour-globally

    _db_id: ObjectId = PrivateAttr(Field(alias="_id", title="Mongo object id"))
    create_date: datetime = Field(
        default_factory=datetime.utcnow, hidden_from_schema=True, title="Creation date"
    )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str, Decimal128: str}


def field_schema(field: DBBaseModel, **kwargs: Any) -> Any:
    # * https://github.com/tiangolo/fastapi/issues/1378
    if field.field_info.extra.get("hidden_from_schema", False):
        raise schema.SkipField(f"{field.name} field is being hidden")
    else:
        return original_field_schema(field, **kwargs)


original_field_schema = schema.field_schema
schema.field_schema = field_schema


def random_string_generator(
    size=settings.app_entity_id_length,
    chars=string.ascii_lowercase + string.digits,
):
    """function which generates random string, 10 chars long to be used as general id for any object"""
    return "".join(random.choice(chars) for _ in range(size))
