def task(tuple_) -> list:
    return list(map(lambda x: (x*9/5)+32, tuple_))


if __name__ == "__main__":

    temp_tuple = (0, 36.6, 100)
    print(task(temp_tuple))
