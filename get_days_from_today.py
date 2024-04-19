from datetime import datetime

def get_days_from_today(date):

    input_date = datetime.strptime(date,'%Y-%m-%d')

    current_date = datetime.today()

    delta = current_date - input_date

    return delta.days

date = '2020-10-09'
print(get_days_from_today(date))
