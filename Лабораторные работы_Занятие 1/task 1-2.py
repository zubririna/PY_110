def task(words: list) -> int:
    return max(map(len, words))

if __name__ == "__main__":

    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(task(list_words))
