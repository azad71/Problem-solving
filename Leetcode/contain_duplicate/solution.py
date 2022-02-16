def containDuplicate(nums):
    if len(nums) == 1:
        return False
    if len(nums) == 2 and nums[0] == nums[1]:
        return True

    print(len(nums))

    for i in range(1, len(nums)-1):
        if nums[i] == nums[i-1] or nums[i] < nums[i-1]:
            return True
    return False


# print(containDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# print(containDuplicate([1, 2, 3, 4, 1, 2]))
print(containDuplicate([3, 1]))
