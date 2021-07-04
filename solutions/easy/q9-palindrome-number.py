"""
https://leetcode.com/problems/palindrome-number/
"""


def is_palindrome(x: int) -> bool:
    group = list(f"{x}")
    group.reverse()
    if len(group) == 1:
        return True
    if group[0] == "0" or group[-1] == "-":
        return False
    return int("".join(group)) == x


print(is_palindrome(-123))
print(is_palindrome(121))
print(is_palindrome(10))
