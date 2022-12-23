INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as file:  # TODO открыть указатель на файл
        for obj in file:
            print(obj, end='')  # TODO файл является итератором, который работает с циклом for в построчном режиме


if __name__ == "__main__":
    task()
