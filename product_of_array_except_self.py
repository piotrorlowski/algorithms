def product_of_array_except_self(nums):
    """Get product of array elements except the element being iterated.
    E.g. given [1, 2, 3, 4] array, in the first iteration it will be
    2*3*4 = 24. In the second iteration it will be 1*3*4 = 12 and so on.
    """
    n = len(nums)
    # create results array that contains n arrays with 1.
    res = [1] * n

    # set prefix to 1
    prefix = 1
    for i in range(n):
        res[i] = prefix
        # multiply prefix by the currently iterated number in nums
        prefix *= nums[i]

    # set postfix to 1
    postfix = 1
    # go from the end
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        # multiply postfix by the currently iterated number in nums
        postfix *= nums[i]
    return res


print(product_of_array_except_self([1, 2, 3, 4]))
