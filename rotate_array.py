class Solution(object):
    def rotate_array_slow(self, nums, k):
        while k:
            num = nums.pop()
            nums.insert(0, num)
            k -= 1
        return nums

    def rotate_array_return_new_array(self, nums, k):
        return nums[-k:] + nums[:-k]

    def rotate_array_in_place(self, nums, k):
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        return nums

    def rotate(self, nums, k) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


solution = Solution()
print(solution.rotate_array_slow([1, 2, 3, 4, 5, 6, 7], 3))
print(solution.rotate_array_return_new_array([1, 2, 3, 4, 5, 6, 7], 3))
print(solution.rotate_array_in_place([1, 2, 3, 4, 5, 6, 7], 3))
print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))
