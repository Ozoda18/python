from datetime import date
from datetime import timedelta
from datetime import datetime
from datetime import time
birthdate=date(1997,9,6)
todays_date=date.today()
year=todays_date.year-birthdate.year
month=todays_date.month-birthdate.month
day=todays_date.day-birthdate.day
print({year},{month},{day});

month = int(input("Enter your birth month"))
day = int(input("Enter your birth day"))
today = datetime.today()
birthday = datetime(today.year, month, day)
birthday = birthday + timedelta(days=(birthday < today) * 365)
days_left = (birthday - today).days
print("Days until your next birthday:", days_left);

now=datetime.now()
duration=time(2,15)
ending_hour=now.hour+duration.hour
ending_minute=now.minute+duration.minute
print('Hour=',ending_hour,'Minute=',ending_minute);

import pytz
local=datetime.now()
tz_Florida=pytz.timezone('America/Florida')
Florida_time=datetime.now(tz_Florida)
print(Florida_time);

user_input = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
try:
    target_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Invalid format. Please enter the date and time in the format YYYY-MM-DD HH:MM:SS.")
    exit()
print("Countdown started...\n")
while True:
    now = datetime.now()
    time_left = target_time - now
    if time_left.total_seconds() <= 0:
        print("\nCountdown complete!")
        break

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"\rTime remaining: {days}d {hours}h {minutes}m {seconds}s", end="")
    time.sleep(1)

import re
email = input("Enter your email address: ")
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

import re
phone = input("Enter a 10-digit phone number: ")
formatted = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", phone)
print(formatted);

import re
password = input("Enter your password: ")
length_pass = len(password) >= 8
lowercase_ok = re.search(r"[a-z]", password) is not None
uppercase_ok = re.search(r"[A-Z]", password) is not None
digit_ok = re.search(r"\d", password) is not None
if length_pass and lowercase_ok and uppercase_ok and digit_ok:
    print("✅ Strong password.")
else:
    print("❌ Weak password. Please make sure it has:")
    if not length_pass:
        print("- At least 8 characters")
    if not lowercase_ok:
        print("- At least one lowercase letter")
    if not uppercase_ok:
        print("- At least one uppercase letter")
    if not digit_ok:
        print("- At least one digit");

import re
text = """
Python is a powerful programming language. Many developers enjoy Python for its readability.
Python can be used for web development, data science, and automation.
"""
word = input("Enter the word to find: ")
matches = re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)
if matches:
    print(f"The word '{word}' was found")
else:
    print(f"The word '{word}' was not found");

import re
text = input("Enter text with dates in it: ")
pattern = r'\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b'
dates = re.findall(pattern, text)
if dates:
    print("Dates found:")
    for date in dates:
        print("-", date)
else:
    print("No dates found.")






