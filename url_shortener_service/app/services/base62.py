from app.core.config import settings


def encode(n: int) -> str:
    """Encodes a number into a base62 string, padded to 7 chars."""
    if n == 0:
        encoded = settings.symbols[0]
    else:
        encoded = ""
        while n > 0:
            n, rem = divmod(n, settings.BASE)
            encoded = settings.symbols[rem] + encoded
    return encoded


def decode(s: str) -> int:
    """Decodes a base62 string back into a number."""
    decoded = 0
    for char in s:
        decoded = decoded * settings.BASE + settings.symbols.index(char)
    return decoded
