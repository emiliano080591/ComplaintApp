from pydantic import BaseModel
from schemas.base import UserBase
from models import RoleType


class BaseUser(BaseModel):
    pass


class UserLoginOut(BaseUser):
    pass


class UserOut(UserBase):
    id: int
    first_name: str
    last_name: str
    phone: str
    role: RoleType
    iban: str
