from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class EditProfileDto:
    username: str
    first_name: str
    last_name: str
    birth_date: date
    email: str
    bio: str
    country: Optional[str]
