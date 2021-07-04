"""
https://leetcode.com/problems/valid-parentheses/
"""


def is_valid(s: str) -> bool:
    hashmap = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []
    for bracket in s:
        close_bracket = hashmap.get(bracket)
        if not close_bracket or len(stack) == 0:
            stack.append(bracket)
        elif close_bracket != stack.pop():
            return False
    return len(stack) == 0


print(is_valid("()[]{}"), True)
