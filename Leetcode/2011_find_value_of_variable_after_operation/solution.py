"""
	link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations
	tag: Array, String
"""


def findValue(operations):
    # x = 0
    # for op in operations:
    #     if op == "++X" or op == "X++":
    #         x += 1
    #     elif op == "--X" or op == "X--":
    #         x -= 1
    # return x
    return len(operations) - str(operations).count('-')


print(findValue(["X++", "--X", "--X", "X--", "X++", "X++"]))
