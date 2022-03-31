# twelve months seperated into 3 weeks. Each week had 10 days.
#each day was 10 hours, each hour was 100 minutes, each minute was 100 seconds.

def get_decimal_time(normal_hour,normal_minute,normal_second):
    #return decimal equivalent in HOUR:MIN:SEC format

    total_sec = (((normal_hour * 60) + normal_minute) * 60) + normal_second
    new_second = total_sec % 100
    remaining_sec = total_sec // 100
    new_minute = remaining_sec % 100
    new_hour = remaining_sec // 100

    return "{}:{}:{}".format(new_hour,new_minute,new_second)




def get_decimal_date(normal_month,normal_day,normal_year):
    #return string "[day] [month] [year], Decade [decade]"

    #month
    months_french = "Nivôse1Pluviôse2Ventôse3Germinal4Floréal5Prairial6Messidor7Thermidor8Fructidor9Vendémiaire10Brumaire11Frimaire12"
    if normal_month < 11:
        start_index = months_french.find(str(normal_month - 1)) + 1
    else:
        start_index = months_french.find(str(normal_month - 1)) + 2
    end_index = months_french.find(str(normal_month))
    ans_french_month = months_french[start_index:end_index]

    #year
    french_year = normal_year - 1792

    #decade:
    decade = 0
    if normal_day < 10:
        decade = 1
    elif normal_day < 20:
        decade = 2
    else:
        decade = 3

    return "{} {} Year {}, Décade {}".format(normal_day if normal_day >= 10 else "0" + str(normal_day),ans_french_month,french_year,decade)

def get_french_datetime(gregorian_str):
    """"
    split_datetime = gregorian_str.split()
    greg_time_str = split_datetime[0].split(":")
    greg_date_str = split_datetime[1].split("/")
    """
    #time
    hours = int(gregorian_str[:2])
    minutes = int(gregorian_str[3:5])
    seconds = int(gregorian_str[6:8])
    french_time = get_decimal_time(hours,minutes,seconds)

    #date
    month = int(gregorian_str[9:11])
    day = int(gregorian_str[12:14])
    year = int(gregorian_str[15:19])
    french_date = get_decimal_date(month,day,year)

    return french_time + "\n" + french_date

def main():

    gregorian_datetime = "16:07:46 03/22/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)

if __name__ == "__main__":
    main();