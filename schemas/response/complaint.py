from schemas.base import ComplaintBase
from datetime import datetime
from models import State


class ComplaintOut(ComplaintBase):
    id: int
    created_at: datetime
    status: State
