import datetime

def astrological_sign(month, day):
    if isinstance(month, str):
        try:
            month = int(month)
        except: 
            month = month.lower()
    if month == "january" or month == 1:
        return "Capricorn" if (day < 20) else "Aquarius"
    elif month == "february" or month == 2: 
        return "Aquarius" if (day < 19) else "Pisces"
    elif month == "march" or month == 3:
        return "Pisces" if (day < 21) else "Aries"
    elif month == "april" or month == 4:
        return "Aries" if (day < 20) else "Taurus"
    elif month == "may" or month == 5:
        return "Taurus" if (day < 21) else "Gemini"
    elif month == "june" or month == 6:
        return "Gemini" if (day < 21) else "Cancer"
    elif month == "july" or month == 7:
        return "Cancer" if (day < 23) else "Leo"
    elif month == "august" or month == 8:
        return "Leo" if (day < 23) else "Virgo"
    elif month == "september" or month == 9:
        return "Virgo" if (day < 23) else "Libra"
    elif month == "october" or month == 10:
        return "Libra" if (day < 23) else "Scorpio"
    elif month == "november" or month == 11:
        return "Scorpio" if (day < 22) else "Sagittarius"
    elif month == "december" or month == 12:
        return "Sagittarius" if (day < 22) else "Capricorn"
    else:
        return "Invalid month"
        