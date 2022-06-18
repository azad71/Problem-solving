def isAnagram(s, t):

    if len(s) != len(t):
        return False

    alphabets = [0] * 26

    for i, _ in enumerate(s):
        print(i, s[i], t[i])
        alphabets[ord(s[i]) - ord('a')] += 1
        alphabets[ord(t[i]) - ord('a')] -= 1

    print(alphabets)
    for i in alphabets:
        if i != 0:
            return False

    return True


print(isAnagram("anagram", "nagaram"))
# print(isAnagram("rat", "car"))
# print(isAnagram("ac", "bb"))
