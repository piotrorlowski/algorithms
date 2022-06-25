def length_of_longest_substring(s):
    """Get the length of unique sequence of characters."""
    # get length of the string
    n = len(s)
    # create a set for keeping unique chars
    charSet = set()
    # left side of the moving window
    left = 0
    # result that will keep the length of the unique string
    res = 0
    # go through indexes of strings
    for right in range(n):
        # while character is in charSet
        while s[right] in charSet:
            # remove that char in the set
            charSet.remove(s[left])
            # increase left index
            left += 1
        # add charSet to the index
        charSet.add(s[right])
        # calculate the length of the unique string by
        # substracting left index + 1 from the right index
        res = max(res, right - left + 1)
    return res


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("au"))
print(length_of_longest_substring("aab"))
