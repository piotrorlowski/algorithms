from functools import cmp_to_key


class Solution:
    def largest_number(self, nums):
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))


solution = Solution()
print(solution.largest_number([3, 40, 340, 5, 9]))
