def header_footer(some_func):  # TODO написать декоратор
    def wrapper():
        print("========")
        some_func()
        print("========")
    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
