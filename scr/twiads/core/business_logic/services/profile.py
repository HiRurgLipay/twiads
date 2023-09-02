from __future__ import annotations
from typing import TYPE_CHECKING
from core.models import Country
from core.models import User
from core.business_logic.services.common import replace_file_name_to_uuid

if TYPE_CHECKING:
    from core.business_logic.dto import EditProfileDto


def edit_profile(data: EditProfileDto, user: User) -> None:
    data.avatar = replace_file_name_to_uuid(file=data.avatar)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA DATA.AVATAR", data.avatar)
    country = Country.objects.get(name=data.country)
    User.objects.filter(id=user.id).update(
        avatar = data.avatar,
        username = data.username,
        first_name = data.first_name,
        last_name = data.last_name,
        bio = data.bio,
        email = data.email,
        birth_date = data.birth_date,
        country = country
    )
    return None