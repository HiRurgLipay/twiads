from __future__ import annotations
from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from core.business_logic.dto import AddTweetDTO

from core.models import Tweet, User


def create_tweet(data: AddTweetDTO) -> None:
    Tweet.objects.create(content=data.content, tag=data.tag)

