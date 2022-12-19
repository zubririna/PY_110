import itertools

def task():
    repeater = itertools.cycle(a)  # TODO бесконечно повторяем элементы кортежа
    for _ in range(10):
        print(next(repeater))

if __name__ == "__main__":
    a = (1, 2, 3)
    task()
