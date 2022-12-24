import json


def task():
    filename = "input.json"
    with open(filename) as file:
        json_f = json.load(file)

    return sorted(json_f, key= lambda x: x['length'])  # TODO отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))


