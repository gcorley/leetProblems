def roman_to_int(s) -> int:
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    romans = s.upper()
    for i, roman in enumerate(romans):
        try:
            if i != 0 and numerals[roman] > numerals[romans[i-1]]:
                # verify valid prefix
                if numerals[roman] <= (numerals[romans[i-1]] * 10):
                    # subtract the number previously added; add the bigger number; subtract the smaller number
                    number = number - numerals[romans[i-1]] + numerals[roman] - numerals[romans[i-1]]
                else:
                    # print(f"Invalid prefix: {romans[i-1]}{roman}")
                    return 0
            else:
                number += numerals[roman]
        except KeyError:
            # print(f"Invalid number: {roman}")
            return 0
    return number
