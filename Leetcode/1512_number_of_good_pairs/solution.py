"""
link: https://leetcode.com/problems/number-of-good-pairs/
tag: Array, Hashmap
memory: O(n) for extra dictionary
time: O(n)
"""


def goodPairs(nums):
    d = {}

    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    pairs = 0
    for key, value in d.items():
        if d[key] > 1:
            pairs += (value * (value - 1)) // 2
    return pairs


nums = [1, 2, 3, 1, 1, 3]

print(goodPairs(nums))
