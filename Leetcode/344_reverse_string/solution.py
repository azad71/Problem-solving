"""
  Link: https://leetcode.com/problems/reverse-string/
  Tag: string
"""


from typing import List


def reverse_string(s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp

        left += 1
        right -= 1
    return s


# s = ["h", "e", "l", "l", "o"]
# s = ["H", "a", "n", "n", "a", "h"]
s = ["a", "b"]

print(reverse_string(s))
