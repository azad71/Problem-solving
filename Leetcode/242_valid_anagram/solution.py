def isAnagram(s, t):
    if len(s) != len(t):
        return False

    sd = {}
    td = {}

    for idx, _ in enumerate(s):
        sd[s[idx]] = 1 + sd.get(s[idx], 0)
        td[t[idx]] = 1 + td.get(t[idx], 0)

    for idx in sd:
        if sd[idx] != td.get(idx, 0):
            return False

    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("ac", "bb"))
