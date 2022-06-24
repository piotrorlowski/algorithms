class Solution:
    def three_sum(self, nums):
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            # avoid duplicate results by not checking two same adjacent numbers
            if i > 0 and nums[i - 1] == num:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                # if sum is bigger than 0, move right pointer to the left
                # (array is sorted and bigger numbers are on the right)
                if sum > 0:
                    right -= 1
                # if sum is smaller than 0, move left pointer to the right
                # (array is sorted and smaller numbers are on the left)
                elif sum < 0:
                    left += 1
                else:
                    # if sum equals to 0 just add the combination
                    # but look further for other combinations
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    # if left pointer is the same as right pointer
                    # we want to skip it, so we don't have duplicates
                    # but left pointer should not overtake right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


solution = Solution()
print(solution.three_sum([0, 0, 0, 0]))
