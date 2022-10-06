def longest_substring(s: str) -> int:
    substring_final = ''
    for i in range(len(s)):
        substring_temp = ''
        remaining = len(s) - i
        if remaining <= len(substring_final):
            break
        for c in s[i:]:
            if c not in substring_temp:
                substring_temp += c
            else:
                break
        if len(substring_temp) > len(substring_final):
            substring_final = substring_temp

    return len(substring_final)
