def longest_common_prefix(strs):
    """Get thge longest common prefix among strings in the array."""
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


print(longest_common_prefix(["flower", "flow", "flight"]))
