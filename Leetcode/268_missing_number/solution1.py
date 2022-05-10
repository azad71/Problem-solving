def missingNumber(nums):

    return list(set([i for i in range(0, len(nums)+1)]).difference(nums))[0]


# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missingNumber([0, 2]))
