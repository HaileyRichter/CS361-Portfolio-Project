# Asks the user for wave information and sends it to wave_info.txt, and storage_pipeline.txt and runs the relevant wave python file when asked
import subprocess
from subprocess import call

flag = False # flag for true or false information was valid so that I can prompt until valid response from user
flag2 = False # reset boolean for second while loop question
# home and exit during first loop will block second loop from executing
while(flag != True):
    # ask what wave they want
    prompt_type = input("Which wave type would you like to simulate? (options are standing, longitudinal, and transverse)\n")
    if prompt_type == 'standing' or prompt_type == 'longitudinal' or prompt_type == 'transverse':
        flag = True

        while (flag2 != True):
            # ask what wave they want
            prompt_values = input("Would you like to set your own initial conditions or use default values? (options are default or my own)\n")

            if prompt_values == 'default':
                with open('wave_info.txt', 'w', encoding="utf-8") as f:
                    f.write(prompt_type+'\n'+prompt_values)
                f.closed

                with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                    f.write('add_entry\n'+prompt_type+'\n'+prompt_values)
                f.closed

                subprocess.run(["python", "backlog_interface.py"])
                subprocess.run(["python", prompt_type+".py"])
                flag2 = True

            elif prompt_values == 'my own':
                # ask about necessary variable
                with open('wave_info.txt', 'w', encoding="utf-8") as f:
                    amplitude = input("What would you like to set the amplitude as?\n")
                    wave_num = input("What would you like to set the wave number as?\n")
                    angular_frequency = input("What would you like to set the angular frequency as?\n")
                    f.write(prompt_type+'\n'+amplitude+'\n'+wave_num+'\n'+angular_frequency)
                f.closed

                with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                    f.write('add_entry\n'+prompt_type+'\n'+amplitude+'\n'+wave_num+'\n'+angular_frequency)
                f.closed

                subprocess.run(["python", "backlog_interface.py"])
                subprocess.run(["python", prompt_type+".py"])
                flag2 = True

            elif prompt_values == 'home':
                with open('home.txt', 'w', encoding="utf-8") as f:
                    f.write('home')
                f.closed
                flag = True
                flag2 = True

            else:
                print("Sorry, that was not an expected response. Please try again.")

    # the home and exit features
    elif prompt_type == 'home':
        with open('home.txt', 'w', encoding="utf-8") as f:
            f.write('home')
        f.closed
        flag2 = True
        flag = True

    else:
        print("Sorry, that was not an expected response. Please try again.")
