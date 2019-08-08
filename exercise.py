def numbers(number):

    if number == 1:
        return str(number) + "st"
    elif number == 2:
        return str(number) + "nd"
    elif number == 3:
        return str(number) + "rd"
    elif number <= 20:
        return str(number) + "th"
