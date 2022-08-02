def implement_strstr(haystack, needle):
    if not needle:
        return 0
    # haystack - hell o
    # needle - ll
    # substract len of needle from len of haystack and add 1
    # to cut unnecessary checks
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1


print(implement_strstr("mississippi", "issip"))
