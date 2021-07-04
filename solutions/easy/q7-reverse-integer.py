"""
https://leetcode.com/problems/reverse-integer/
"""


def reverse(x: int) -> int:
    group = list(f"{x}")
    if len(group) == 1 or (len(group) == 2 and group[0] == "-"):
        return x
    if group[-1] == "0":
        return reverse(int("".join(group[:-1])))
    index = 1 if group[0] == "-" else 0
    reverse_group = group[index:]
    reverse_group.reverse()
    if index == 1:
        reverse_group = [group[0]] + reverse_group
    result = int("".join(reverse_group))
    return result if -2 ** 31 <= result <= (2 ** 31 - 1) else 0


print(reverse(-123))
print(reverse(901000))
print(reverse(8192))
