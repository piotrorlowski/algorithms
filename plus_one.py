def plus_one(digits):
    if digits[-1] == 9:
        j = len(digits) - 1
        while j >= 0:
            if digits[j] == 9:
                digits[j] = 0
                if j == 0:
                    digits.insert(0, 1)
                j -= 1
            else:
                digits[j] += 1
                j -= 1
                return digits
        return digits
    digits[-1] += 1
    return digits


def plus_one_slower(digits):
    strs = [str(i) for i in digits]
    res = str(int("".join(strs)) + 1)
    return [int(i) for i in res]


print(plus_one([1, 2, 3]))
print(plus_one([1, 0, 0]))
print(plus_one([9]))
print(plus_one([1, 9, 9]))
print(plus_one([9, 9]))
print(plus_one([9, 8, 9]))

print("---------------")

print(plus_one_slower([1, 2, 3]))
print(plus_one_slower([1, 0, 0]))
print(plus_one_slower([9]))
print(plus_one_slower([1, 9, 9]))
print(plus_one_slower([9, 9]))
print(plus_one_slower([9, 8, 9]))
