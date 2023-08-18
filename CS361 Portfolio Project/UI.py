# the python file in charge of asking the user questions and communicating to other files
import subprocess
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
import time

# start the backlog running in the background
subprocess.run(["make"])

# welcome message and example
subprocess.run(["python", "welcome.py"])
subprocess.run(["python", "standing.py"])
with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
    f.write("add_entry")
    time.sleep(2)
    f.write("standing\ndefault"+ "\nend_file")
f.closed

print("To go the home menu, type home in the terminal window at any of the questions. To exit the program, go home and then type exit.")

# ask if they want to make another simulation
flag = True # continue playing
while(flag == True):
    prompt = input("Would you like to try another?(yes or no)\n")
    if prompt == 'yes':
        with open('home.txt', 'w', encoding="utf-8") as f:
            f.write('')
            f.closed
        subprocess.run(["python", "wave_type.py"])
        with open('home.txt', 'r', encoding="utf-8") as f:
            read_data = f.read()
            if read_data == '':
                subprocess.run(["python", "standing.py"]) #NEED TO CHANGE SOME DAY
                print("Here is the wave equation for this wave: PRINT SOMETHING LATER")
            f.closed
    elif prompt == 'no':
        prompt = input("If you want to exit this program, please type exit.\n")
        if prompt == 'exit':
            flag = False
    else:
        print("Sorry, that was not an expected response. Please try again.")
