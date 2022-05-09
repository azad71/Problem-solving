"""
  link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
  tag: Array, String
"""


def maximumWordInSentence(sentences):
    maxWord = 0

    for sentence in sentences:
        maxWord = max(maxWord, len(sentence.split()))

    return maxWord


print(maximumWordInSentence(["alice and bob love leetcode",
      "i think so too", "this is great thanks very much"]))
