def task(list_words) -> str:

    return min(list_words, key=len)

if __name__ == "__main__":
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    print(task(list_words))
