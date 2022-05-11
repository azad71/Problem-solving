def removeDuplicate(nums):
    currentVal = nums[0]
    currentIdx = 1

    for i in range(1, len(nums)):

        if nums[i] != currentVal:
            currentVal = nums[i]
            nums[currentIdx] = nums[i]
            currentIdx += 1

    return currentIdx


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1, 2]
# nums = [-10, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 1, 2, 2, 3, 3, 3, 3, 4]


print(removeDuplicate(nums))
