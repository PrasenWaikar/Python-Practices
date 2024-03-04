import calendar
from datetime import datetime

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

if __name__ == "__main__":
    # Print the current calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print("Current Calendar:")
    print(cal.formatmonth(datetime.now().year, datetime.now().month))

    # Print the current live time
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current Time: {current_time}")

    # Print the greeting message
    greeting = get_greeting()
    print(greeting)
