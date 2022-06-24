class Solution:
    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + high
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return None


solution = Solution()
print(solution.binary_search([-1, 0, 3, 5, 9, 12], 9))
