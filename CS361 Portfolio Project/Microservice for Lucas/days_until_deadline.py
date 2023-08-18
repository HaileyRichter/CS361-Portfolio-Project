import time
# Import date class from datetime module
import datetime
from datetime import date

with open('microservice_communication.txt', 'r', encoding="utf-8") as f:
    # tutorial from Geeks4geeks on how to read word by word
    # Python program to read
    # file word by word
    # opening the text file
    input_or_output = True # boolean for determining input or output. True is input of deadline. False is output of days left
    # reading each line
    for line in f:
    # reading each word
        for word in line.split():
            if word == "deadline:":
                input_or_output = True
            if word == "days_left:":
                input_or_output = False
            elif input_or_output == True and word != "deadline:" and word != "days_left:": # idk why if the above ifs are run it runs the else but it does
                    # where we convert DDMMYY to something I can calculate the days left with
                    number = int(word)
                    year = number%10000
                    number = (number - year)/10000
                    month = number%100
                    number = (number - month)/100
                    day = number

                    # using now() to get current time
                    current_time = datetime.datetime.now()
                    current_year = current_time.year
                    current_month = current_time.month
                    current_day = current_time.day

                    days_left = 0 # default amount of dates and if date is in the past will return 0
                    # compare dates
                    deadline_date = date(int(year), int(month), int(day))
                    current_date = date(current_year, current_month, current_day)
                    difference = deadline_date - current_date
                    if difference.days > 0:
                        days_left = difference.days

            # else if input_or_output is False then do nothing
            elif input_or_output == False and word != "deadline:" and word != "days_left:":
                days_left = int(word)

    f.closed

with open('microservice_communication.txt', 'w', encoding="utf-8") as f:

    f.write("days_left: " + str(days_left))

    f.closed
# pause the check from communication to save CPU resources
time.sleep(5)