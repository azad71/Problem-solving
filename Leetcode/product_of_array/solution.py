def productExceptSelf(nums):
    temp = 1

    output = [1] * len(nums)

    for i in range(len(nums)):
        output[i] = temp
        temp *= nums[i]
    l = len(output)-1

    print(output, l)

    temp = 1
    while l >= 0:
        output[l] *= temp
        temp *= nums[l]
        l -= 1
    print(output)
    return output


productExceptSelf([1, 2, 3, 4])
