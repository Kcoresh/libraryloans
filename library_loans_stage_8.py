# === Stage 8: Генерация идентификаторов ===
# Project: LibraryLoans
import uuid
import re

PROJECT_PREFIX = "LL"


def generate_unique_id():
    counter = 0
    while True:
        candidate = f"{PROJECT_PREFIX}-{uuid.uuid4().hex[:8]}-{counter:03d}"
        if not _is_duplicate(candidate):
            return candidate
        counter += 1


def _is_duplicate(candidate):
    return any(existing for existing in _existing_ids if existing == candidate)


def register_id(candidate):
    _existing_ids.add(candidate)
    return candidate


_existing_ids = set()


def reset_ids():
    _existing_ids.clear()


def validate_prefix(text):
    return isinstance(text, str) and len(text) >= 3 and text[:1].isalpha()
