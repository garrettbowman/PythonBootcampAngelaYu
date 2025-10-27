import smtplib
import pandas

my_email = "undeadstarfish@gmail.com"
# get app password from gmail settings
password = "abc123"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user= my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs=my_email,
#     msg="Subject:Hello\n\nThis is the body."
# )
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg="Subject:Hello\n\nThis is the body."
#     )


import datetime as dt
import random

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(year)

# date_of_birth = dt.datetime(year=2000, month=3,day=4)


with open("quotes.txt") as data:
    quotes = data.readlines()

if day_of_week == 5:
    quote = random.choice(quotes)

    print(quote)



# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg=f"Subject:Your quote for motivation\n\n{quote}"
#     )