from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except KeyError:
                hash_table[i] = 0
        return hash_table.popitem()[0]

    def single_number_xor(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            print(f"a = {a}, i = {i}, a ^ i = {a ^ i}")
            a = a ^ i
        return a


solution = Solution()

print(
    solution.single_number(
        [
            1,
            2,
            2,
            1,
            3,
            4,
            4,
            5,
            5,
            6,
            6,
        ]
    )
)

print(
    solution.single_number_xor(
        [
            1,
            2,
            2,
            1,
            3,
            4,
            4,
            5,
            5,
            6,
            6,
        ]
    )
)
