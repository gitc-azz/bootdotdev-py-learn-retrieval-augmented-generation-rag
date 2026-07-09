import json
import string


def load_and_preprocess(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.read().splitlines()


STOP_WORDS: list[str] = load_and_preprocess("./data/stopwords.txt")


def is_match(pattern: list[str], data: list[str]) -> bool:
    for p in pattern:
        for d in data:
            if p in d:
                return True
    return False


def without_punctuation(s: str) -> str:
    """map every punctutation to None"""
    d: dict[str, str | None] = {}
    for c in string.punctuation:
        d[c] = None
    table = str.maketrans(d)
    ret = s.translate(table)
    return ret


def tokenized(s: str) -> list[str]:
    ret = []
    for t in s.split(" "):
        if len(t) > 0:
            ret.append(t)
    return ret


def without_stopwords(tokens: list[str]) -> list[str]:
    ret = []
    for t in tokens:
        if t in STOP_WORDS:
            continue
        ret.append(t)
    return ret


def preprocess_text(s: str) -> list[str]:
    ret = s.lower()
    ret = without_punctuation(ret)
    ret = tokenized(ret)
    ret = without_stopwords(ret)
    return ret


def search(json_file_path: str, pattern: str) -> list[str]:
    with open(json_file_path, "r") as json_file:
        movies = json.load(fp=json_file)

        pattern_tokens = preprocess_text(pattern)

        ret: list[str] = []
        for movie in movies["movies"]:
            if is_match(pattern_tokens, preprocess_text(movie["title"])):
                ret.append(f"{len(ret) + 1}. {movie['title']}")
            if len(ret) == 5:
                break
        return ret
