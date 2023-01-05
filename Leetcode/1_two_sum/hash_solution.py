"""
title: Hashmap solution
link: https://leetcode.com/problems/two-sum
space: O(n), for extra dictionary
time: O(n), for one pass
"""


def twoSum(nums, target):
    # edge case
    if len(nums) == 2 and nums[0] + nums[1] == target:
        return [0, 1]

    # define new hashmap
    numsMap = {}

    for i in range(0, len(nums)):
        # check if target - nums[i] exists in hashmap
        # if not, simply add it to hashmap like this, key(nums[i]) = value(nums index)
        temp = target - nums[i]

        if temp in numsMap:
            return [numsMap[temp], i]
        numsMap[nums[i]] = i
    return []


print(twoSum([2, 7, 11, 15], 13))

"""
Let's simulate 

We have a nums array [2,7,11,15] and target sum = 13

numsMap = {}

pass 1: 
    i = 0, temp = target - nums[0] = 13 - 2 = 9
    9 in numsMap = false, add 2 to numsMap, numsMap = {2: 0}

pass 2:
    i = 1, temp = target - nums[1] = 13 - 7 = 5
    5 in numsMap = false, add 7 to numsMap, numsMap = { 2: 0, 7: 1}
    
pass 3:
    i = 2, temp = target - nums[2] = 13 - 11 = 2
    2 in numsMap = true, return [numsMap[2], i(2)]
"""
