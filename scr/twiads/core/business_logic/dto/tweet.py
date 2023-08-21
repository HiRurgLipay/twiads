from dataclasses import dataclass
from core.models import Tag, User 
from typing import Optional

@dataclass
class AddTweetDTO:
    content = str
    tag = Optional['Tag'] | None
    author = Optional['User']
    