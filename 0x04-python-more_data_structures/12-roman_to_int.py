#!/usr/bin/python3
def roman_to_int(rs):
    result = 0
    prev_value = 0
    current_value = 0
    rn = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if rs and isinstance(rs, str):
        for letter in reversed(rs):
            current_value = rn[letter]
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            prev_value = current_value

    return result
