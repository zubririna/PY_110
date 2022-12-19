def task(number, char):

    for number, char in zip(number, char):
        print(f"{number}-{char}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    chars = ["a", "b", "c", "d", "e"]

    task(numbers, chars)
