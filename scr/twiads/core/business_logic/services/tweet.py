from __future__ import annotations
from typing import TYPE_CHECKING

from django.db.models import Count


if TYPE_CHECKING:
    from core.business_logic.dto import AddTweetDTO

from core.models import Tweet


def create_tweet(data: AddTweetDTO) -> None:
    Tweet.objects.create(content=data.content, likes_count=data.likes_count, retweets_count=data.retweets_count, 
                         comments_count=data.comments_count, parent_tweet=data.parent_tweet, author=data.author, tag=data.tag)
    