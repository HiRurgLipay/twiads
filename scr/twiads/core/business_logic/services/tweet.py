from __future__ import annotations
from typing import TYPE_CHECKING, Any
from django.db import transaction
from core.business_logic.dto import AddTweetDTO
import logging
import re

from core.models import Tweet, Tag

logger = logging.getLogger(__name__)


def create_tweet(data: AddTweetDTO) -> None:
    with transaction.atomic():
        tags: list[str] = data.tags.split("\r\n")
        tags_list: list[Tag] = []
        for tag in tags:
            try:
                tag_from_db = Tag.objects.get(name=tag.lower())
            
            except Tag.DoesNotExist as err:
                logger.warning("Tag does not exist", extra={"Tag": tag}, exc_info=err)
                tag_from_db = Tag.objects.create(name=tag.lower())
                logger.info("Handled error and successfully created tag in db", extra={'tag': tag})
            tags_list.append(tag_from_db)
            
        created_tweet = Tweet.objects.create(author=data.author, content=data.content, parent_tweet=data.parent_tweet)
        created_tweet.tags.set(tags_list)
        if data.parent_tweet:
            replied_tweet = Tweet.objects.get(id=data.parent_tweet)
            replies_counter = replied_tweet.reply_counter()
            replies_counter += 1
            replied_tweet.reply_counter = replies_counter
            replied_tweet.save()
        logger.info("Successfully created tweet", extra={"author":data.author, 'content':data.content, 'parent_tweet':data.parent_tweet})
            

