"""
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        complement_index = hash_map.get(complement)
        if complement_index is not None:
            return [complement_index, i]
        hash_map[nums[i]] = i
    return []


ex1 = {
    "nums": [2, 7, 11, 15],
    "target": 9
}
ex2 = {
    "nums": [3, 2, 4],
    "target": 6
}
ex3 = {
    "nums": [3, 3],
    "target": 6
}
print(two_sum(**ex1), [0, 1])
print(two_sum(**ex2), [1, 2])
print(two_sum(**ex3), [0, 1])
