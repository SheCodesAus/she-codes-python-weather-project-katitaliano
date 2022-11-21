import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

"""Takes a temperature and returns it in string format with the degrees
    and celcius symbols.

Args:
    temp: A string representing a temperature.
Returns:
    A string contain the temperature and "degrees celcius."
"""

def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    date_str = date.strftime("%A %d %B %Y")
    return f"{date_str}"

"""Converts and ISO formatted date into a human readable format.

Args:
    iso_string: An ISO date string..
Returns:
    A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
"""

def convert_f_to_c(temp_in_farenheit):
    temp = (float(temp_in_farenheit) - 32.0) * (5.0/9.0)
    return round(temp, 1)
    
"""Converts an temperature from farenheit to celcius.

Args:
    temp_in_farenheit: float representing a temperature.
Returns:
    A float representing a temperature in degrees celcius, rounded to 1dp.
"""

def calculate_mean(weather_data):
    total = 0
    count = len(weather_data)
    for item in range(0, count):
        total = float(total) + float(weather_data[item])
    mean = total/count
    return mean

"""Calculates the mean value from a list of numbers.

Args:
    weather_data: a list of numbers.
Returns:
    A float representing the mean value.
"""

def load_data_from_csv(csv_file):
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        list = []
        for line in reader:
            if line:
                sublist = []
                sublist.append(line[0])
                sublist.append(int(line[1]))
                sublist.append(int(line[2]))
                list.append(sublist)
        return list

"""Reads a csv file and stores the data in a list.

Args:
    csv_file: a string representing the file path to a csv file.
Returns:
    A list of lists, where each sublist is a (non-empty) line in the csv file.
"""
    
def find_min(weather_data):
    if (weather_data):
        mini = min(weather_data)
        minindex = 0
        for index in range(len(weather_data)):
            item = weather_data[index]
            if item == mini:
                minindex = index
        return float(mini), minindex
    return ()

"""Calculates the minimum value in a list of numbers.

Args:
    weather_data: A list of numbers.
Returns:
    The minium value and it's position in the list.
"""

def find_max(weather_data):
    if (weather_data):
        maxi = max(weather_data)
        maxindex = 0
        for index in range(len(weather_data)):
            item = weather_data[index]
            if item == maxi:
                maxindex = index
        return float(maxi), maxindex
    return ()

"""Calculates the maximum value in a list of numbers.

Args:
    weather_data: A list of numbers.
Returns:
    The maximum value and it's position in the list.
"""

def generate_summary(weather_data):
    min_list = []
    max_list = []
    date_list = []
    days = len(weather_data)
    for sublist in weather_data:
                date_list.append(convert_date(sublist[0]))
                min_list.append(convert_f_to_c(sublist[1]))
                max_list.append(convert_f_to_c(sublist[2]))
    mini = find_min(min_list)
    output_min = format_temperature(mini[0])
    min_index = mini[1]
    output_min_date = date_list[min_index]
    maxi = find_max(max_list)
    output_max = format_temperature(maxi[0])
    max_index = maxi[1]
    output_max_date = date_list[max_index]
    sum_lows = round((sum(min_list)), 1)
    count_lows = len(min_list)
    ave_low = format_temperature(round(sum_lows / count_lows, 1))
    sum_highs = round((sum(max_list)))
    count_highs = len(max_list)
    ave_high = format_temperature(round(sum_highs / count_highs, 1))
    summary = (f"{days} Day Overview\n  The lowest temperature will be {output_min}, and will occur on {output_min_date}.\n  The highest temperature will be {output_max}, and will occur on {output_max_date}.\n  The average low this week is {ave_low}.\n  The average high this week is {ave_high}.\n"
    )
    return summary.format(weather_data)

"""Outputs a summary for the given weather data.

Args:
    weather_data: A list of lists, where each sublist represents a day of weather data.
Returns:
    A string containing the summary information.
"""

def generate_daily_summary(weather_data):
    sum_list =[]
    for line in weather_data:
        date = convert_date(line[0])
        min_temp = format_temperature(convert_f_to_c(line[1]))
        max_temp = format_temperature(convert_f_to_c(line[2]))
        form_sum = (f'''---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n''')
        sum_list.append(form_sum)
    daily_sum_str = ""
    for ele in sum_list:
        daily_sum_str += ele
    return daily_sum_str      
        
"""Outputs a daily summary for the given weather data.

Args:
    weather_data: A list of lists, where each sublist represents a day of weather data.
Returns:
    A string containing the summary information.
"""

