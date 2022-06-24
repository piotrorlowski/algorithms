class Solution(object):
    def remove_duplicates(self, nums):
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        return left


solution = Solution()

print(solution.remove_duplicates([0, 1, 2, 2, 2, 3, 4]))
