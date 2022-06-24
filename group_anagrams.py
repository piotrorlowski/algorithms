class Solution:
    def group_anagrams(self, strs):
        """Use dictionary to store same anagrams.
        VERY IMPORTANT LESSON.
        """
        # create a dictionary
        dictionary = {}
        # iterate through array of strings
        for s in strs:
            # create sorted string so it can be used as a dict key
            # sorted key will be always the same 'cat', 'tac' - 'act'
            # so it can be used as a dict key for holding arrays
            sorted_s = "".join(sorted(s))
            # check if the sorted string already exists as a key in dict
            if sorted_s not in dictionary:
                # if it does't exist, add it as a key and assign the current
                # string as an array with the current string
                dictionary[sorted_s] = [s]
            else:
                # otherwise concatenate the array with the current string to
                # already existing array
                dictionary[sorted_s] += [s]
        # return array of 'grouped' anagrams
        return [dictionary[k] for k in dictionary.keys()]


solution = Solution()
print(solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
