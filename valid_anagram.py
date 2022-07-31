def valid_anagram(s, t):
    list_s = []
    list_t = []

    # separate letters into list of letters
    list_s[:0] = s

    # separate letters into list of letters
    list_t[:0] = t

    list_s.sort()
    list_t.sort()

    if len(list_t) == len(list_s):
        return all(list_s[i] == list_t[i] for i in range(0, len(list_s)))
    return False


print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("a", "ab"))
