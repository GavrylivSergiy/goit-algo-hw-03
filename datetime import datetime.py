from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Check if the birthday falls on a weekend
            if congratulation_date.weekday() >= 5:  # Saturday (5) or Sunday (6)
                # If so, move the congratulations to the next Monday
                days_until_monday = (7 - congratulation_date.weekday()) + 1
                congratulation_date += timedelta(days=days_until_monday)

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "Jack Li", "birthday": "2024.04.18"},
    {"name": "John Doe", "birthday": "2024.04.25"},
    {"name": "Jane Smith", "birthday": "2024.04.28"},
    {"name": "Julia Harrison", "birthday": "2024.05.03"}
]

print(get_upcoming_birthdays(users))