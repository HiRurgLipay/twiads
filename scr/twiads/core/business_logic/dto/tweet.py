from dataclasses import dataclass
from django.core.files.uploadedfile import InMemoryUploadedFile
from core.models import Tweet, User, Tag
from typing import Optional

@dataclass
class AddTweetDTO:
    content = str
    likes_count = int
    retweets_count = int
    comments_count = int
    parent_tweet = Optional['Tweet']
    author = Optional['User']
    tag = Optional['Tag']
