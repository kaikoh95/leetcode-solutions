"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


def remove_duplicates(nums: list[int]) -> int:
    count = 0
    if len(nums) == 0:
        return count
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            count += 1
            nums[count] = nums[i + 1]
    return count + 1


print(remove_duplicates([1, 1, 2, 3]), 3)
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
