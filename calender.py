import calendar
import datetime

# Get the current date
today = datetime.date.today()
current_year = today.year
current_month = today.month
current_day = today.day

# Create a plain text calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
month_calendar = cal.formatmonth(current_year, current_month)

# Print the calendar
print(month_calendar)

# Highlight the current date
print(f"Today's date: {today}")
