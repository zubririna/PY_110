import json


def task():
    filename = "input.json"
    with open(filename) as file:
        json_f = json.load(file)     # TODO считать содержимое JSON файла

    gen_exr = (i["contains_improvement_appeals"]  for i in json_f)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
