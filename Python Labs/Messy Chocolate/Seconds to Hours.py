                               #Seconds to Hours

seconds = input("Enter the number of seconds: ")
seconds = int(seconds)

hours = int(seconds/3600)
seconds = int(seconds%3600)
minutes = int(seconds/60)
seconds = int(seconds%60)

print(hours, "hours,")
print(minutes, "minutes, and")
print (seconds, "seconds!")

input("Press any key to leave this screen.")


