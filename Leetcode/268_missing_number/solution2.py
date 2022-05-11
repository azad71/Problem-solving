"""
  link: https://leetcode.com/problems/missing-number/
"""


def missingNumber(nums):

    s1 = (len(nums) * (len(nums) + 1)) / 2

    return s1 - sum(nums)


print(missingNumber([0, 1, 4, 3]))
