import smtplib
import datetime as dt
from random import choice

# calculate day
today_date = dt.datetime.now()
day_of_week = today_date.weekday()

# email info
my_email = "example@gmail.com"
password = "sgnzhqqmhreynqyh"

# checks the day
if day_of_week == 3:
    # open file
    with open("day 32/quote_task/quotes.txt", "r") as file_quotes:
        all_quotes = [name.strip() for name in file_quotes.readlines()]
        quote = choice(all_quotes)

    # send quote    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="example@myyahoo.com",
            msg=f"Subject:Motivational Thursday\n\n{quote}"
        )