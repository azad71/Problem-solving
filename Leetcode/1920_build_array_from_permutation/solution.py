import math


def buildArray(nums):
    n = len(nums)
    for i in range(0, n):
        nums[i] = nums[i] + n * (nums[nums[i]] % n)
    for i in range(0, n):
        nums[i] = math.floor(nums[i] / n)
    print(nums)


buildArray([0, 2, 1, 5, 3, 4])
