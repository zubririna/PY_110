INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as file_1:
        with open(OUTPUT_FILE, 'w') as file_2:
            for line_upp in map(str.upper, file_1):
                file_2.write(line_upp)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")



with open("test.txt", 'r') as f_src:
    with open("test_new.txt", "w") as f_dst:
        for line in f_src:
            f_dst.write(line)