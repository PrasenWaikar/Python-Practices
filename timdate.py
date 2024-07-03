import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", current_time)
