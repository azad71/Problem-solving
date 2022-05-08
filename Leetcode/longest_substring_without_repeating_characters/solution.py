"""
    link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    space: O(1), since characters are fixed
    time: O(n)
    hints: Sliding window
    tag: Array, Hashmap
"""


def longestSubstring(s):
    start = 0
    maxLength = 0
    visited = {}

    for i in range(len(s)):

        if s[i] in visited and start <= visited[s[i]]:
            start = visited[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        visited[s[i]] = i

    return maxLength


s = "abcabcbb"
print(longestSubstring(s))
