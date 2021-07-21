from bson import ObjectId
from pydantic import BaseModel, PrivateAttr, Field, schema
from typing import Optional, Any
from datetime import datetime
import random
import string
from bson.decimal128 import Decimal128


class DBBaseModel(BaseModel):
    # * https://pydantic-docs.helpmanual.io/usage/model_config/#change-behaviour-globally

    _db_id: ObjectId = PrivateAttr(Field(alias="_id"))
    create_date: datetime = Field(
        default_factory=datetime.utcnow, hidden_from_schema=True
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


# function which generates random string, 10 chars long to be used as general id for any object
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
