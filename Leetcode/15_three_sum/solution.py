from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i, value in enumerate(nums):
        if i > 0 and value == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1

        while j < k:
            s = value + nums[j] + nums[k]
            if s == 0:
                result.append([value, nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif s < 0:
                j += 1
            else:
                k -= 1
    return result


n = [0, 0, 0, 0]

result = three_sum(n)

print(result)
