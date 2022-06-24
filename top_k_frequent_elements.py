from itertools import groupby


def top_k_frequent_elements(nums, k):
    """Use grouped elements, duplicates and singles to rearrange
    elements and then return the most frequent ones."""
    # group the same elements in the list into serpate arrays
    groups = [list(val) for key, val in groupby(sorted(nums))]

    # initialize duplicates array
    duplicates = []

    # append arrays that have duplicates into duplicates array
    for i in groups:
        if len(i) > 1:
            duplicates.append(i)

    # initialize singles array
    singles = []

    # append singles into singles array
    for i in groups:
        if i not in duplicates:
            singles.append(i)

    # sort duplicates by their length ascending
    duplicates.sort(key=len)

    # reverse order of duplicates to descending order
    duplicates = duplicates[::-1]

    # create new array where most frequent numbers are first
    # and less frequent are last
    new_groups = duplicates + singles

    # return the most frequent numbers by k elements
    return [new_groups[i][0] for i in range(len(new_groups)) if i + 1 <= k]


print(
    top_k_frequent_elements(
        [
            5,
            1,
            -1,
            -8,
            -7,
            8,
            -5,
            0,
            1,
            10,
            8,
            0,
            -4,
            3,
            -1,
            -1,
            4,
            -5,
            4,
            -3,
            0,
            2,
            2,
            2,
            4,
            -2,
            -4,
            8,
            -7,
            -7,
            2,
            -8,
            0,
            -8,
            10,
            8,
            -8,
            -2,
            -9,
            4,
            -7,
            6,
            6,
            -1,
            4,
            2,
            8,
            -3,
            5,
            -9,
            -3,
            6,
            -8,
            -5,
            5,
            10,
            2,
            -5,
            -1,
            -5,
            1,
            -3,
            7,
            0,
            8,
            -2,
            -3,
            -1,
            -5,
            4,
            7,
            -9,
            0,
            2,
            10,
            4,
            4,
            -4,
            -1,
            -1,
            6,
            -8,
            -9,
            -1,
            9,
            -9,
            3,
            5,
            1,
            6,
            -1,
            -2,
            4,
            2,
            4,
            -6,
            4,
            4,
            5,
            -5,
        ],
        7,
    )
)
