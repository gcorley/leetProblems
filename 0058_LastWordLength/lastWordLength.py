def last_word_length(s: str) -> int:
    arr = s.strip().split()
    return len(arr[-1])
