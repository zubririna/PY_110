def task(list_: list) -> list:
    return list(map(int, list_))

if __name__ == "__main__":

    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,  # шестнадцатеричное представление
        0b1010101010  # бинарное представление представление
    ]

    print(task(num_list))
