import datetime
from random import randrange


class Person:

    def __init__(self, birthday: datetime.date):
        self.birthday = birthday


def random_birthday() -> datetime.date:
    days = randrange(0, 100 * 365)
    return datetime.date.today() - datetime.timedelta(days=days)


def same_birthday(p1: Person, p2: Person) -> bool:
    return p1.birthday.month == p2.birthday.month and p1.birthday.day == p2.birthday.day


if __name__ == "__main__":
    people = [Person(birthday=random_birthday()) for i in range(100)]
