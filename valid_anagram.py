def valid_anagram_wrong(s, t):
    hash_s = set(s)
    hash_t = set(t)
    if len(s) == len(t):
        return all(i in hash_t for i in hash_s)
    return False


def valid_anagram_1(s, t):
    list_s = []
    list_t = []

    list_s[:0] = s
    list_t[:0] = t

    list_s.sort()
    list_t.sort()
    if len(list_t) == len(list_s):
        return all(list_s[i] == list_t[i] for i in range(0, len(list_s)))
    return False


print(valid_anagram_wrong("anagram", "nagaram"))
print(valid_anagram_wrong("a", "ab"))

print("---------------------------------------")

print(valid_anagram_1("anagram", "nagaram"))
print(valid_anagram_1("a", "ab"))
