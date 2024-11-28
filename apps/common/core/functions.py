import hashlib


def generate_md5_hash(value: str) -> str:
    """
    Generate an MD5 hash for the given value.
    """
    return hashlib.md5(value.encode('utf-8')).hexdigest()
