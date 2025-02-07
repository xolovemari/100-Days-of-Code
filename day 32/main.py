import pandas
import smtplib
import os
import datetime as dt
from random import choice

# opening and reading the csv file 
df = pandas.read_csv("day 32/birthdays.csv")

# calculate day
today = dt.datetime.now()
month = today.month
day = today.day
date = (month, day)

# check if today matches a birthday
birthdays = df[(df["month"] == month) & (df["day"] == day)]

# picking a random letter
def letter_template(name):
    folder = "day 32/letter_templates"
    letters = [letter for letter in os.listdir(folder) if letter.endswith(".txt")]
    random_letter = choice(letters)

    letter_path = os.path.join(folder, random_letter)

    with open(letter_path, "r") as file:
        old_letter = file.read()

    new_letter = old_letter.replace("[NAME]", name)

    return new_letter

# sending letter
my_email = "example@gmail.com"
password = "example"

def send_email(email, letter):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )

data = birthdays.to_dict(orient="records")
if not birthdays.empty:
    for person in data:
        name = person["name"]
        email = person["email"]
        chosen_letter = letter_template(name)
        send_email(email, chosen_letter)
else:
    print("There aren't any birthdays today.")