def leap_year(year):
    """Function that determines if a year is a leap year or not."""
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)