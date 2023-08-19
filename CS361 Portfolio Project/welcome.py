print("\nWelcome to my wave simulator! Here you can choose between standing waves,"
      " longitudinal traveling waves, and transverse traveling waves. \nBy running several animations"
      " of different wave types and changing the variable of their wave equations, you will hopefully "
      "deepen \nyour understanding of waves."
      "\n\n"
      "A standing waves are stationary waves meaning that there are some areas along the wave that never "
      "move up or down but stay fixed at a \nspecific x and y coordinate. Their amplitudes can change. "
      "Standing waves are seen in nature through guitar strings with both ends fixed. "
      "\n\n"
      "Traveling waves cause their respective mediums to move about space while standing waves only move in time."
      " A transverse wave moves the \nmedium perpendicular to the direction the wave is actually traveling. "
      "An example of a transverse wave is ripples on the surface of water. \nLongitudinal waves cause their medium to move"
      " parallel to the waves movement like tsunami or sound waves.\n")

print("Here is an example of using this simulator.")
print("Which wave type would you like to simulate?")
print("standing")
print("Would you like to set initial conditions or use default values")
print("default")
with open('wave_info.txt', 'w', encoding="utf-8") as f:
    f.write("standing\ndefault")
#    f.write("default")
f.closed
