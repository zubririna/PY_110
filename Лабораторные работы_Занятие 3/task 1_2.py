OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as file:
        for star in range(10):
            file.write(f"{(star+1)*'*' :>10}\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
