from application.salary import calculate_salary
from application.db.people import get_employees

import datetime

today_date = str(datetime.datetime.now())[: str(datetime.datetime.now()).index(' ')]

if __name__ == "__main__":
    get_employees()
    calculate_salary()
    print(today_date)