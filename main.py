# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import pandas as pd
import datetime as dt
from random import randint
import smtplib
import os 

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


#--DATA HANDLING--
data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)

now = dt.datetime.now()
month = now.month
day = now.day
for person in data_dict:
    birth_day = person["day"]
    birth_month = person["month"]
    if birth_day == day and birth_month == month:
        letter_choice = randint(1,3)
        with open(f"./letter_templates/letter_{letter_choice}.txt") as f:
            data = f.read()
            edited_letter = data.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:

        # Encryption service
        connection.starttls()

        # login
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        # send mail
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{person["email"]}",
                            msg=f"Subject:Happy Birthday\n\n{edited_letter}")

