import re


def valid_palindrome(s):
    if len(s) > 1:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        middle = len(s) // 2
        l_side = s[:middle]
        r_side = s[(middle + 1) :]
        if len(s) % 2 == 0:
            r_side = s[(middle):]
        l_side_arr = [char for char in l_side]
        r_side_arr = [char for char in r_side]
        arr = l_side_arr + r_side_arr
        l, r = 0, len(arr) - 1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True
    else:
        return True


print(valid_palindrome("dcbbcd"))
