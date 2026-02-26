def leap_year(year):
    """Function that determines if a year is a leap year or not."""
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False