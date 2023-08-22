from __future__ import annotations

from dataclasses import dataclass
from core.models import Tag, User, Tweet 
from typing import Optional



@dataclass
class AddTweetDTO:
    content : str
    tags : str
    author : Optional['User'] 
    parent_tweet : Tweet | None
    