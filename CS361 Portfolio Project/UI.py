# the python file in charge of asking the user questions and communicating to other files
import subprocess
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
import time

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
    prompt = input("Would you like to try another wave or take a quiz about wave types?(another, previous, quiz or neither)\n")
    if prompt == 'another':
        with open('home.txt', 'w', encoding="utf-8") as f:
            f.write('')
            f.closed
        subprocess.run(["python", "wave_type.py"])
    elif prompt == 'neither':
        prompt = input("If you want to exit this program, please type exit.\n")
        if prompt == 'exit':
            with open('storage.txt', 'w', encoding="utf-8") as f:
                f.write('')
            f.closed
            with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                f.write('')
            f.closed
            with open('wave_info.txt', 'w', encoding="utf-8") as f:
                f.write('')
            f.closed
            with open('home.txt', 'w', encoding="utf-8") as f:
                f.write('')
            f.closed
            with open('exit.txt', 'w', encoding="utf-8") as f:
                f.write('')
            f.closed
            flag = False
    elif prompt == 'quiz':
        subprocess.run(["python", "quiz.py"])

    elif prompt == 'previous':
        with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
            f.write('view_last_entry')
        f.closed

        subprocess.run(["python", "backlog_interface.py"])

        with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
            f.write('')
        f.closed

    else:
        print("Sorry, that was not an expected response. Please try again.")
