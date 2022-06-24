from typing import List


class Solution(object):
    def contains_duplicate(self, nums: List[int]) -> bool:
        """Create a hash (set) and iterate through array.
        Check if number is already in the set, if it is, then
        return True. If it's not, add it to the set. If the loop
        is finished return False. Set can not contain duplicates.
        So if the value is already in the set it means that it was
        duplicated in the array.
        """
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


solution = Solution()

print(solution.contains_duplicate([1, 2, 3, 4, 5, 1]))
