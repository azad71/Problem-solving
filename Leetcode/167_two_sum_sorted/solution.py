def twoSum(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        s = nums[i] + nums[j]

        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            return [i, j]


print(twoSum([2, 7, 11, 15], 130))
