import random
from faker import Faker
from data.data import Date, Person, Color


faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def genereted_persons():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() +
        " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(30000, 45000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),

    )


def generated_file():
    path = rf'D:\NewFile\testfile{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello world{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple",
                    "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]


    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )
