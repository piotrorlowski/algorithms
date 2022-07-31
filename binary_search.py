class Solution:
    def binary_search(self, nums, target):
        """Return position (index) of the target number in the list."""
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + r
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                r = mid - 1
            else:
                l = mid + 1
        return None


solution = Solution()
print(solution.binary_search([-1, 0, 3, 5, 9, 12], 9))


def binary_search(a, t):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = l + r
        guess = a[mid]
        if guess == t:
            return mid
        if guess > t:
            r = mid - 1
        if guess < t:
            l = mid + 1
    return None


print(binary_search([-1, 0, 3, 5, 9, 12], 9))
