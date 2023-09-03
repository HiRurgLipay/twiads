from core.models import User, Tweet

from django.db.models import QuerySet


def get_sorted_tweets_and_retweets(user: User, sort_by: str) -> QuerySet:
    tweets = Tweet.objects.filter(author=user)
    if sort_by == 'Newest':
        return tweets.order_by('-created_at')
    elif sort_by == 'Likes':
        return tweets.order_by('-likes_count')
    else:
        return tweets.order_by('-created_at')
