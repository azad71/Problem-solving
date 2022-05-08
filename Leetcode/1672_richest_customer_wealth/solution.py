"""
  link: https://leetcode.com/problems/richest-customer-wealth/submissions/
	memory: O(1)
	time: O(n * m), row * column
	tag: Array, Matrix
"""

accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]


def maximumWealth(accounts):
    s = 0
    for i in range(0, len(accounts)):
        t = 0
        for j in range(0, len(accounts[i])):
            t += accounts[i][j]
        s = max(s, t)

    return s


print(maximumWealth(accounts))
