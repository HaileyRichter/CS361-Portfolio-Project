# This feature adds and prints items for the storage.txt file. It also reads commands from the storage_pipeline.txt
while True:
    with open('storage_pipeline.txt', 'r', encoding="utf-8") as f:
        file_contents = f.read()
        split_into_words = file_contents.split()
        first_word = ""
        if len(split_into_words) > 0:
            first_word = split_into_words[0]
            data = ""
            for i in range(len(split_into_words)):
                if i != 0:
                    data = data + str(split_into_words[i]) + "\n"
        f.closed

        if first_word == 'add_entry':
            # add file with barrier of stars to storage.txt
            with open('storage.txt', 'r', encoding="utf-8") as f:
                storage_contents = f.read()
            f.closed
            with open('storage.txt', 'w', encoding="utf-8") as f:
                f.write(storage_contents + "\n********************\n" + data)
            f.closed
            with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                f.write('close_program')
            f.closed
            first_word = ""

        elif first_word == 'view_last_entry':
            entry = ''
            with open('storage.txt', 'r', encoding="utf-8") as f:
                for line in f:
                    for word in line.split():
                        if word == '********************':
                            entry = ''
                        else:
                            entry = entry + word + "\n"
            f.closed
            # default values
            amplitude = 'A'
            wave_num = 'k'
            angular_frequency = 'w'
            # user values
            arr = []
            # opening the text file
            entry = entry.split()
            for i in range(len(entry)):
                if i == 0:
                    continue
                if entry[i] == 'default':
                    continue
                else:
                    arr.append(entry[i])

            if len(arr) == 3:
                amplitude = arr[0]
                wave_num = arr[1]
                angular_frequency = arr[2]
            print("Here is the wave equation for this wave: y(x,t) = " + str(amplitude) + "cos(" + str(wave_num) + "*x - " + str(angular_frequency) + "*t)")

            with open('storage_pipeline.txt', 'w', encoding="utf-8") as f:
                f.write('close_program')
            f.closed

        elif first_word == 'close_program':
            break
