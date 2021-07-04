"""
https://leetcode.com/problems/roman-to-integer/
"""


def roman_to_int(s: str) -> int:
    hashmap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    to_minus = ["IV", "IX", "XL", "XC", "CD", "CM"]
    count = 0
    prev = None
    for char in s[-1::-1]:
        if f"{char}{prev}" in to_minus:
            count -= hashmap[char]
        else:
            count += hashmap[char]
        prev = char
    return count


print(roman_to_int("MCMXCIV"), 1994)
print(roman_to_int("LVIII"), 58)
