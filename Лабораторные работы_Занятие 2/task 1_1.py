def task(list_) -> int:
    return max(len(i) for i in list_)  # TODO записать выражение-генератор


if __name__ == "__main__":
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    print(task(list_words))
