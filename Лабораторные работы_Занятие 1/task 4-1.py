from itertools import count

def task(counter):
    for i in range(10):
        print (next(counter))


if __name__ == "__main__":
    counter = count(100, 10)

    task(counter)
