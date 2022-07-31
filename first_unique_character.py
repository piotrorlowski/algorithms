def first_unique_char(s):
    hash_dict = {}
    for char in s:
        if char not in hash_dict:
            hash_dict[char] = True
        else:
            hash_dict[char] = False
    for key, value in hash_dict.items():
        if value:
            return s.index(key)
    else:
        return -1


print(first_unique_char("aabb"))
