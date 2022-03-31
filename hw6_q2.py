# twelve months seperated into 3 weeks. Each week had 10 days.
#each day was 10 hours, each hour was 100 minutes, each minute was 100 seconds.

def get_decimal_time(normal_hour,normal_minute,normal_second):
    #return decimal equivalent in HOUR:MIN:SEC format
    #16:07:46 = 5:80:66

    return "{}:{}:{}".format(normal_hour,normal_minute,normal_second)




def get_decimal_date(normal_month,normal_day,normal_year):
    #return string "[day] [month] [year], Decade [decade]"

    return "{} {} Year {}, Décade {}".format(normal_day if normal_day >= 10 else "0" + str(normal_day),normal_month,normal_year,"[decade]")

def get_french_datetime(gregorian_str):
    split_datetime = gregorian_str.split()
    greg_time_str = split_datetime[0].split(":")
    greg_date_str = split_datetime[1].split("/")

    #time
    hours = int(greg_time_str[0])
    minutes = int(greg_time_str[1])
    seconds = int(greg_time_str[2])
    french_time = get_decimal_time(hours,minutes,seconds)
    #date
    month = int(greg_date_str[0])
    day = int(greg_date_str[1])
    year = int(greg_date_str[2])
    french_date = get_decimal_date(month,day,year)

    return french_time + "\n" + french_date

def main():
    decimal_time = get_decimal_time(16, 7, 46)
    print(decimal_time)
    decimal_date = get_decimal_date(3,22,2022)
    print(decimal_date)
    print("")

    gregorian_datetime = "16:07:46 03/22/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)

main()