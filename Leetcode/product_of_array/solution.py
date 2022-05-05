def productExceptSelf(nums):
    prefix = 1
    postfix = 1
    result = [1] * (len(nums))

    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    numLen = len(nums) - 1
    while numLen >= 0:
        result[numLen] *= postfix
        postfix *= nums[numLen]
        numLen -= 1

    return result
