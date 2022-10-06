def longest_common_prefix(strs: list[str]) -> str:
    for i in range(len(strs)):
        strs[i] = strs[i].lower()
    match = ''
    s1 = strs[0]
    for c in s1:
        match += c
        for word in strs:
            if not word.startswith(match):
                return match[:len(match)-1]
    return match
