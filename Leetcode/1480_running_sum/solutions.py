def runningSum(nums):
    s = nums[0]

    for i in range(1, len(nums)):
        s += nums[i]
        nums[i] = s

    return nums


print(runningSum([1, 2, 3, 4]))
