from datetime import datetime, timedelta, date


users = [
    {
        "name": "Vitaliy Gritsenko",
        "birthday": datetime(year=2002, month=12, day=28),
    },
    {
        "name": "Vitaliy Ivanov",
        "birthday": datetime(year=1988, month=5, day=10),
    },
    {
        "name": "Vladislav Zaets",
        "birthday": datetime(year=1996, month=6, day=9),
    },
    {
        "name": "Vadim Shinkarev",
        "birthday": datetime(year=1995, month=5, day=10),
    },
    {
        "name": "Dmitro Rozhko",
        "birthday": datetime(year=2000, month=3, day=25),
    },
    {
        "name": "Yevgen Shinkarev",
        "birthday": datetime(year=2003, month=4, day=24),
    },
    {
        "name": "Yura Zhovtobrukh",
        "birthday": datetime(year=1998, month=7, day=30),
    },
    {
        "name": "Lera Beskrovnaya",
        "birthday": datetime(year=1995, month=12, day=20),
    },
    {
        "name": "Danilo German",
        "birthday": datetime(year=2003, month=7, day=25),
    },
    {
        "name": "Olesya Ivanova",
        "birthday": datetime(year=1970, month=8, day=3),
    },
    {
        "name": "Katya Sidorenko",
        "birthday": datetime(year=1970, month=8, day=4),
    },
    {
        "name": "Marina Kuznetsova",
        "birthday": datetime(year=2023, month=7, day=31),
    },
]


def get_birthdays_per_week(birthday_list: list) -> None:
    current_date = date.today()

    users_day = {weekday: [] for weekday in range(7)}

    end_date = current_date + timedelta(days=7)

    if current_date.weekday() == 0:
        current_date = current_date - timedelta(days=2)

    for user in users:
        bd = user["birthday"].replace(year=current_date.year)

        if current_date <= bd.date() < end_date:
            weekday = bd.weekday()
            if weekday in [5, 6]:
                users_day[0].append(user["name"])
            if weekday not in [5, 6]:
                users_day[bd.weekday()].append(user["name"])

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Субота", "Неділя"]

    for weekday, list in users_day.items():
        weekday = days[weekday]
        if len(list) >= 1:
            print(f'{weekday}: {", ".join(list)}')


get_birthdays_per_week(users)
