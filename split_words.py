def split_words(text, max_width):
    words = text.split(" ")
    arr = []
    for i in range(len(words)):
        line = "".join(words[i])
        arr.append(line)
        new_line = " ".join(arr)
        if len(new_line) <= max_width:
            print(len(new_line))
    return


print(
    split_words(
        (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat."
        ),
        10,
    )
)
