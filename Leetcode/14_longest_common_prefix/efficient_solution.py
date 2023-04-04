def longestCommonPrefis(s):
    result = ""

    s.sort()
    l = min(len(s[0]), len(s[-1]))

    for i in range(l):
        if s[0][i] != s[-1][i]:
            return result
        result += s[0][i]

    return result
