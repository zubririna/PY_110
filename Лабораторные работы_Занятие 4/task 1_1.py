import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"""####\s+(?P<position>\d{1,2})\.\s+\[(?P<book>.+?)\]\((?P<book_url>https:.+?)\)\s+by\s+(?P<author>\w+?)\s+\((?P<recommended>\d{1,2}\.\d+%)\s+recommended\)\s+!\[\]\((?P<cover_url>https:.+?)\)\s+\"(?P<description>.+?)\"\s+\[.*?\]\(https:.*?\)"""

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))

    print(sorted(f, key = lambda x: x['recommended']))

if __name__ == '__main__':
    task()

