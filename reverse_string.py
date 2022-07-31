def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s) - 1
    while l < r:
        char_1 = s[l]
        char_2 = s[r]
        s[l] = char_2
        s[r] = char_1
        l += 1
        r -= 1
    print(s)


reverseString(["h", "e", "l", "l", "o"])
