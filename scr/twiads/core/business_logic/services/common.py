from __future__ import annotations
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from django.core.files import File


def replace_file_name_to_uuid(file: File) -> File:
    file_extansion = file.name.split(".")[-1]
    file_name = str(uuid.uuid4())
    file.name = file_name + "." + file_extansion
    return file