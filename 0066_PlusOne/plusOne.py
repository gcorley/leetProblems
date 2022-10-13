def plus_one(digits: list[int]) -> list[int]:
    num = 0
    new_digits = []
    for i, digit in enumerate(digits):
        power = len(digits) - i - 1
        num += digit * pow(10, power)
    num += 1
    for d in str(num):
        new_digits.append(int(d))
    return new_digits
