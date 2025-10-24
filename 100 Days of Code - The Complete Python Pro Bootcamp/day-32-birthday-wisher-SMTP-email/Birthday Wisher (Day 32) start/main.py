import smtplib

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

now = dt.datetime.now()

print(now)