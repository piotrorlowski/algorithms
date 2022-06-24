class Solution:
    def two_sum_slow(self, nums, target):
        nums_range = range(0, len(nums))
        for i in nums_range:
            for j in nums_range:
                is_sum = nums[i] + nums[j] == target
                if i != j and is_sum:
                    return [i, j]

    def two_sum(self, nums, target):
        """Adding (key) number and (value) index to hash map (dict)
        and checking if the difference between target and
        current number is already in the dict. If it is, just return
        the index (value) of the number in the dict and index of currently
        checked number in the array.
        """
        hash_map = {}
        # iterate with index and element through array
        for i, num in enumerate(nums):
            # get the different with the current num from the target number
            difference = target - num
            # if difference is already in the hash_map, then we are done
            # and we just return the current index
            if difference in hash_map:
                return [hash_map[difference], i]
            # in any other case, just add the number
            # and it's index to the dict (hash_map)
            hash_map[num] = i


solution = Solution()
print(solution.two_sum_slow([0, 7, 5, 4], 9))
print(solution.two_sum([0, 7, 5, 4], 9))
