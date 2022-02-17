"""
* prefix sum add previous values with current values at current index
"""


def prefix_sum(nums):
    if len(nums) == 0 or len(nums) == 1:
        return
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


print(prefix_sum([1, 2, 3, ]))
