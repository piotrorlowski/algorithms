class Solution:
    def two_sum(self, nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            index = i + 1
            difference = target - num
            if difference in hash_map:
                return [hash_map[difference], index]
            hash_map[num] = index

    def two_sum_l_r(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left + 1, right + 1]


solution = Solution()
print(solution.two_sum([2, 7, 11, 15], 9))
print(solution.two_sum_l_r([2, 7, 11, 15], 9))
