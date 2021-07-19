months_lengths_mod_7 = {1: 3, 2: 0, 3: 3, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 2, 10: 3, 11: 2, 12: 3}

def has_leap_year_in_last_year(day, month, year):
    if year % 4 == 1 and ((year - 1) % 100 != 0 or (year - 1) % 400 == 0):
        if month <= 2:
            return True
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if month > 2 or (month == 2 and day == 29):
            return True
    else:
        return False

def get_day(day, month, year):
    if day == 1 and month == 1 and year == 1900:
        return 1
    if has_leap_year_in_last_year(day, month, year) and year > 1900:
        return (get_day(day, month, year - 1) + 2) % 7
    elif year > 1900:
        return (get_day(day, month, year - 1) + 1) % 7
    elif month > 1:
        return (get_day(day, month - 1, year) + months_lengths_mod_7[month - 1]) % 7
    elif day > 1:
        return day % 7


def main():
    counter = 0
    for month in range(1,13):
        for year in range(1901, 2001):
            if get_day(1, month, year) == 0:
                counter += 1
    print(counter)

if __name__ == "__main__":
    main()
