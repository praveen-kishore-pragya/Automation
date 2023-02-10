def isSubsequence(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)