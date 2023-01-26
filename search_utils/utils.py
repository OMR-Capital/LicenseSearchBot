import string


def normalize(text: str) -> str:
    text = text.lower()
    text = text.strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text