# questions to ask user

num_correct = 0

prompt = input("1. A node is the location in a standing wave where the wave is fixed with no up or down movement? (True or False)\n")
if prompt == 'True':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("2. Waves can transport materials and energy? (True or False)\n")
if prompt == 'False':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("3. The largest wave ever recorded measured over 1,700 feet? (True or False)\n")
if prompt == 'True':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("4. Omega is the symbol used to represent angular frequency when calculating properties about waves? (True or False)\n")
if prompt == 'True':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("5. Light is a longitudinal wave? (True or False)\n")
if prompt == 'False':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("6. The speed of sound in air is about 767 miles per hour? (True or False)\n")
if prompt == 'True':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("7. The speed of sound in air is about 3,345 miles per hour? (True or False)\n")
if prompt == 'True':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("8. Wavelength is the distance between a wave crest and its closest trough? (True or False)\n")
if prompt == 'False':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("9. Standing waves travel distances? (True or False)\n")
if prompt == 'False':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

prompt = input("10. Wave height and wave amplitude are the same thing? (True or False)\n")
if prompt == 'False':
    print("Correct")
    num_correct = num_correct + 1
else:
    print("Incorrect")

# give user a score
print("You got " + str(num_correct) + " correct out of 10!")