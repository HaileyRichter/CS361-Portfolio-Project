print("Welcome to my wave simulator! Here you can choose between standing waves, longitudinal traveling waves, and transverse traveling waves. INSERT BACKGROUND INFO")
print("Here is an example of using this simulator.")
print("Which wave type would you like to simulate?")
print("standing")
print("Would you like to set initial conditions or use default values")
print("default")
with open('wave_info.txt', 'w', encoding="utf-8") as f:
    f.write("standing\ndefault")
#    f.write("default")
f.closed
