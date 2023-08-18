# function to ask and get wave type from user//maybe make it ask for all wave input from user.
# It puts wave information into wavetype.txt
import time

flag = False # flag for true or false information was valid so that I can prompt until valid response from user
flag2 = False # reset boolean for second while loop question
# home and exit during first loop will block second loop from executing
while(flag != True):
    # ask what wave they want
    prompt = input("Which wave type would you like to simulate? (options are standing, longitudinal, and transverse)\n")
    if prompt == 'standing' or prompt == 'longitudinal' or prompt == 'transverse':
        with open('wave_info.txt', 'w', encoding="utf-8") as f:
            f.write(prompt)
        f.closed
        flag = True

        while (flag2 != True):
            # ask what wave they want
            prompt = input(
                "Would you like to set your own initial conditions or use default values? (options are default or my own)\n")

            # print(prompt)
            if prompt == 'default':
                with open('wave_info.txt', 'w', encoding="utf-8") as f:
                    f.write(prompt)
                f.closed
                # save this wave
                with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                    f.write("add_entry")
                    time.sleep(2)
                    f.write(prompt + "\nend_file")
                f.closed
                flag2 = True

            elif prompt == 'initial conditions' or 'my own':
                # ask about necessary variable
                # STILL NEED TO DO
                with open('wave_info.txt', 'w', encoding="utf-8") as f:
                    f.write("custom")
                f.closed
                # save this wave
                with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                    f.write("add_entry")
                    time.sleep(2)
                    f.write(prompt + "\nend_file")
                f.closed
                flag2 = True

            elif prompt == 'home':
                with open('home.txt', 'w', encoding="utf-8") as f:
                    f.write(prompt)
                f.closed
                flag = True
                flag2 = True

            elif prompt == 'exit':
                with open('exit.txt', 'w', encoding="utf-8") as f:
                    f.write(prompt)
                f.closed
                flag = True
                flag2 = True

            else:
                print("Sorry, that was not an expected response. Please try again.")

    # the home and exit features
    elif prompt == 'home':
        with open('home.txt', 'w', encoding="utf-8") as f:
            f.write(prompt)
        f.closed
        flag2 = True
        flag = True

    else:
        print("Sorry, that was not an expected response. Please try again.")
