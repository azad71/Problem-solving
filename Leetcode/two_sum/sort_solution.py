"""
title: Sort solution
link: https://leetcode.com/problems/two-sum
space: O(1) if sorting is inplace or O(n)
time: O(nlogn) for sorting + O(n)
"""


def twoSum(nums, target):
    if len(nums) == 2 and nums[0] + nums[1] == target:
        return [0, 1]

    nums.sort()
    print(nums)

    start = 0
    end = len(nums) - 1

    while start < end:
        if nums[start] + nums[end] > target:
            end -= 1
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            break

    return [start, end]


print(twoSum([2, 11, 7, 15, 1, 0, 9], 13))

"""
  Explanantion
  
  we have nums = [2, 11, 7, 15, 1, 0, 9] and target sum is 13
  
  after sorting, array will be [0, 1, 2, 7, 9, 11, 15]
  
  # When array is sorted, we have
    - lowest element on left
    - highest element on right
  
  # Initiate two variable, 
    # 'start' starter point from left
    # 'end' starter point from right
    
  # if nums[start] + nums[end] < target - this means current sum is lower, we have to move left index to get a higher sum
    # increment start by one
  # if nums[start] + nums[end] > target - this means current sum is higher we have to move right index to get a lower sum
    # decrement end by one
  
  # Above conditions left out only condition when nums[start] + nums[end] = target, on this condition we will break out of loop
  # and return [start, end]
"""
