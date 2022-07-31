from copy import deepcopy


def hourglass_sum(arr):
    """From hackerrank. Hourglass:
    333
     3
    333
    In 6x6 array are 16 hourglasses.
    Finds them all and sum
    """
    cols = len(arr[0])
    rows = len(arr)
    parts = []

    for row in range(0, rows):
        for col in range(1, cols - 1):
            parts.append([arr[row][col - 1], arr[row][col], arr[row][col + 1]])

    copied_parts = deepcopy(parts)

    objs = [parts[i] for i in range(len(parts) - 8)]

    for i in range(0, len(objs)):
        objs[i] += copied_parts[i + 4]

    for i in range(0, len(objs)):
        objs[i] += copied_parts[i + 8]

    for obj in objs:
        del obj[3]
        del obj[4]

    sums = [sum(obj) for obj in objs]

    return max(sums)


print(
    hourglass_sum(
        [
            [0, -4, -6, 0, -7, -6],
            [-1, -2, -6, -8, -3, -1],
            [-8, -4, -2, -8, -8, -6],
            [-3, -1, -2, -5, -7, -4],
            [
                -3,
                -5,
                -3,
                -6,
                -6,
                -6,
            ],
            [-3, -6, 0, -8, -6, -7],
        ]
    )
)
