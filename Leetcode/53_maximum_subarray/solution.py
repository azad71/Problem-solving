def findMaximumSubArray(nums):
    maxSum = nums[0]
    runningSum = 0

    for n in nums:
        if runningSum < 0:
            runningSum = 0
        runningSum += n
        maxSum = max(maxSum, runningSum)
    return maxSum


print(findMaximumSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
