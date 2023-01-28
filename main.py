import json
import random
import faker
from conf import MODEL


def get_title() ->str:
    """
    Функция считывает из файла название книги
    :return: наименовани книги из файла
    """
    with open("books.txt", encoding='utf-8') as f:
        f_t=random.choice(f.readlines())
    return f_t


def get_year() ->int:
    """
    Функция рандомно формирует год из заданного диапозона
    :return: год написания произведения
    """
    x=random.randint(1700,2022)
    return x


def get_pages() ->int:
    """
    Функция рандомно формирует количество страниц из заданного диапозона
    :return: количество страниц книги
    """
    x = random.randint(10, 400)
    return x


def get_isbn13():
    """
    Функция берет isbn13  из faker
    :return: isbn13 для заданной книги
    """
    fake=faker.Faker("ru")
    return fake.isbn13()


def get_rating() ->float:
    """
    Функция рандомно формирует рейтинг книги из заданного диапозона
    :return: рейтинг книги
    """
    x = random.uniform(0, 5)
    return x


def get_price() ->float:   # рандомно формирует стоимость из заданного диапозона
    """
    Функция рандомно формирует стоимость книги из заданного диапозона
    :return: стоимость книги
    """
    x = random.uniform(100, 2000)
    return x


def get_author() ->list:
    """
    Функция берет автора из faker, отдельно имя и фамилию, чтобы оформить в список
    :return: имя и фамилия автора книги списком
    """
    fake = faker.Faker("ru")
    fio = [fake.first_name_male(), fake.last_name_male()]
    return fio


def book_gen(start_pk=1):
    """
    Функция формирует характеристику книги
    :param start_pk: начальный счетчик книги
    :yield: словарь с характеристиками книги
    """
    dict_book = {
        "model": MODEL,
        "pk": start_pk,
        "fields": {
            "title": get_title(),
            "year": get_year(),
            "pages": get_pages(),
            "isbn13": get_isbn13(),
            "rating": get_rating(),
            "price": get_price(),
            "author": get_author()
        }
    }
    start_pk+=1
    yield dict_book


def main():
    """
    Функция формирует список из 100 словарей с характеристиками книг
    :return:список из 100 книг
    """

    dict_list=[]
    pk_=1
    gen = book_gen(pk_)
    for i in range(100):
        cur_book = next(gen)
        dict_list = dict_list.append(cur_book)
        pk_+=1
    with open('itog.json', "w", encoding='utf-8') as file:
        dict_list=json.load(file)
    return dict_list


if __name__ == "__main__":
    result = main()
    print (result)
