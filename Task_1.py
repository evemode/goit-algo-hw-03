from datetime import datetime
from typing import Optional

def get_days_from_today(date:str) -> Optional[int]:
    '''Calculate the number of days between a given date (YYYY-MM-DD) and today'''
    try:
        set_date = datetime.strptime(date, '%Y-%m-%d').date() #convert input string to a date object using the specified format
        current_date = datetime.today().date() #gets today's date
        days_between = (current_date - set_date).days #calculate the number of days between the two dates
        return days_between
    except ValueError: #Handle invalid date format
        print("Invalid date format. Please use 'YYYY-MM-DD'")

print(get_days_from_today('2025-06-23'))
