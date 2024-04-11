import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_number: str
    birthday: datetime.date
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
