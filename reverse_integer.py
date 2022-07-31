def reverse_integer(x):
    x = str(x)
    x = [i for i in x]
    minus = ""
    if "-" in x:
        minus = x.pop(x.index("-"))
    l, r = 0, len(x) - 1
    while l < r:
        char_1 = x[l]
        char_2 = x[r]
        x[l] = char_2
        x[r] = char_1
        l += 1
        r -= 1
    if minus:
        x.insert(0, minus)
    x = int("".join(x))
    if x not in range(-(2 ** 32), 2 ** 32):
        return 0
    return x


print(reverse_integer(1534236469))
print(reverse_integer(123))
print(reverse_integer(-123))
