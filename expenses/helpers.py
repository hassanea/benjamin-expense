import datetime as d

months = {
    1  : "January",
    2  : "February",
    3  : "March",
    4  : "April",
    5  : "May",
    6  : "June",
    7  : "July",
    8  : "August",
    9  : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

# calculates the dates for the "Next" and "Previous" buttons on the homepage
# see the 'index' view
def calculate_date_links(year, month):
    prev_month = (month - 2) % 12 + 1
    next_month = month % 12 + 1
    prev_year = year
    next_year = year
    if (month == 1):
        prev_year -= 1
    elif (month == 12):
        next_year += 1
    return (prev_year, prev_month, next_year, next_month)

# Given a start date and a number of occurrences for an expense
# determine the last date on which the expense will occur
def calculate_end_date(start_date, recurrences):
    month = (start_date.month + recurrences) % 12
    year  = start_date.year + recurrences // 12
    return d.datetime(year, month, start_date.day)

