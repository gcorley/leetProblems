def is_valid(s: str) -> bool:
    stack = []
    valid = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in valid.values():
            stack.append(c)
        elif c in valid.keys() and stack and valid[c] == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack
