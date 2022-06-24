def find_smallest_num(nums):
    smallest_index = 0
    for i in range(1, len(nums)):
        if nums[smallest_index] > nums[i]:
            smallest_index = i
    return smallest_index


print(find_smallest_num([1234, 4, 5, 3, 2, 123, 41, 20, 17]))
