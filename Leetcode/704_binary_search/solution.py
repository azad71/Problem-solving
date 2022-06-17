
def search(nums, target):

    left = 0
    right = len(nums)

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    return -1


# print(search([2, 5], 5))
# print(search([2, 5, 9, 10, 14], 5))
# print(search([2, 5, 7, 8, 9, 10], 10))
# print(search([-1, 0, 5], 5))
