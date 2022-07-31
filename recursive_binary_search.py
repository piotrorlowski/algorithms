def recursive_binary_search(nums, target):
    """Return True if element is found in the list."""
    n = len(nums)
    if n == 0:
        return False
    mid = n // 2
    guess = nums[mid]
    if guess == target:
        return True
    if guess < target:
        pos = mid + 1
        return recursive_binary_search(nums[pos:], target)
    else:
        return recursive_binary_search(nums[:mid], target)


print(recursive_binary_search([-1, 0, 3, 5, 9, 12], 9))
