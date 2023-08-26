from __future__ import annotations
from typing import TYPE_CHECKING
from django.db import transaction
from core.models import Country
from core.models import User

if TYPE_CHECKING:
    from core.business_logic.dto import EditProfileDto


def edit_profile(data: EditProfileDto, user: User) -> None:
    country = Country.objects.get(name=data.country)
    User.objects.filter(id=user.id).update(
        username = data.username,
        first_name = data.first_name,
        last_name = data.last_name,
        bio = data.bio,
        email = data.email,
        birth_date = data.birth_date,
        country = country
    )
  