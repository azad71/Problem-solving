"""
link: https://leetcode.com/problems/contains-duplicate/
author: Azad Mamun
"""

# sort and then iterate and compare approach
# time complexity sort = O(nlog2n) and loop = O(n), total = O(nlog2n) + O(n)
# space O(1)
# this approach takes much execution time and less memory

# def containDuplicate(nums):
#     if len(nums) == 1:
#         return False

#     nums.sort()
#     print(nums)

#     for i in range(0, len(nums)-1):
#         if nums[i] == nums[i+1]:
#             return True

#     return False

# check if item in map,
# if yes, then there's a duplicate
# time complexity loop = O(n), map lookup = O(1), total = O(n) + O(1)
# space complexity for extra map O(n)
# this approach consumes more memory and less execution time

# def containDuplicate(nums):
#     if len(nums) == 1:
#         return False

#     d = {}
#     for i in nums:
#         if d.get(i) is not None:
#             return True
#         d[i] = i

#     return False


# convert list to set and compare set length with original list
# this approach is short, simple and easy to understand
def containDuplicate(nums):
    return len(set(nums)) < len(nums)


print(containDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(containDuplicate([1, 4, 3, 2, 90, 0, -1]))
print(containDuplicate([1, 2, 3, 4, 1, 2]))
print(containDuplicate([3, 1]))
print(containDuplicate([1, 2, 3, 1]))
