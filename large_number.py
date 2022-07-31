from functools import cmp_to_key


class Solution:
    def largest_number(self, nums):
        """Concatenate numbers as strings to get the largest number."""
        for i, n in enumerate(nums):
            # change numbers to strings
            nums[i] = str(n)

        # define a function that will compare strings
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        # create sorted array of the compared strings (numbers)
        nums = sorted(nums, key=cmp_to_key(compare))

        # return the largest number
        return str(int("".join(nums)))


solution = Solution()
print(solution.largest_number([3, 40, 340, 5, 9]))
