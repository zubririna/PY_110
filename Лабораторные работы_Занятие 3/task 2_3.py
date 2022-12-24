import json


def task():
    filename = "input.json"
    with open (filename) as file:
        json_f = json.load(file)        # TODO считать содержимое JSON файла

    return max(json_f, key=lambda x: x["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
