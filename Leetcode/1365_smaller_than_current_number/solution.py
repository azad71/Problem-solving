

def smallerThanCurrentNumber(nums):

    newNums = sorted(nums)
    numLen = len(nums)

    output = [0] * numLen

    d = {}

    for n in range(numLen):
        if newNums[n] in d:
            continue
        else:
            d[newNums[n]] = n

    for i in range(numLen):
        output[i] = d[nums[i]]

    return output


# nums = [8, 1, 2, 2, 3]
nums = [6, 5, 4, 8]
# [4, 5, 6, 8]
print(smallerThanCurrentNumber(nums))
