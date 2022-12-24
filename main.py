import json
import random
import faker


def get_model() ->str:    # считывает из файла поле model
    with open("conf.py", encoding='utf-8') as f:
        f_m=f.readline()
    return f_m


def get_title() ->str:   # считывает из файла название книги
    with open("books.txt", encoding='utf-8') as f:
        f_t=f.readline()
    return f_t
# нужно сделать выбор рандомным


def get_year() ->int:    # рандомно формирует год из заданного диапозона
    x=random.randint(1700,2022)
    return x


def get_pages() ->int:    # рандомно формирует номер страницы из заданного диапозона
    x = random.randint(10, 400)
    return x


def get_isbn13():   # берет isbn13  из faker
    fake=faker.Faker("ru")
    fake.seed(0)
    return fake.isbn13()


def get_rating() ->float:   # рандомно формирует рейтинг из заданного диапозона
    x = random.uniform(0, 5)
    return x


def get_price() ->float:   # рандомно формирует стоимость из заданного диапозона
    x = random.uniform(100, 2000)
    return x


def get_author() ->list:   # берет автора из faker, отдельно имя и фамилию, чтобы оформить в список
    fake = faker.Faker("ru")
    fake.seed(3)
    fio = [fake.first_name_male(), fake.last_name_male()]
    return fio


def main():
    model_ = get_model()
    pk=1
    dict_list=[]
    with open('itog.json', "w", encoding='utf-8') as file:
        for i in range(100):
            dict_book = {
                "model": model_,
                "pk": pk,
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
            dict_list=dict_list.append(dict_book)
            pk+=1
        dict_list=json.load(file)
    return dict_list


if __name__ == "__main__":
    result = main()
    print (result)
