import string


symbols = string.ascii_letters + string.digits


def encode(n: int) -> str:
    """Encodes a number into a base62 string."""
    if n == 0:
        return symbols[0]

    base = len(symbols)
    encoded = []

    while n > 0:
        n, rem = divmod(n, base)
        encoded.append(symbols[rem])

    return ''.join(reversed(encoded))


def decode(s: str) -> int:
    """Decodes a base62 string back into a number."""
    base = len(symbols)
    decoded = 0

    for char in s:
        decoded = decoded * base + symbols.index(char)

    return decoded


def main():
    i = 500_000_000
    encoded = encode(i)
    print(f"{i} -> {encoded}")
    print(f"{encoded} -> {decode(encoded)}")


if __name__ == "__main__":
    main()
