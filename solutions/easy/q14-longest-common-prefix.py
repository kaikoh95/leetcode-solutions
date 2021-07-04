"""
https://leetcode.com/problems/longest-common-prefix/
"""


def longest_common_prefix(strs: list[str]) -> str:
    strs.sort(key=len)
    lcp = ""
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if strs[j][i] == strs[0][i]:
                j += 1
            else:
                return lcp
        lcp += strs[0][i]
    return lcp


print(longest_common_prefix(["flower", "flow", "flight"]), "fl")
print(longest_common_prefix(["dog", "racecar", "car"]), "")
