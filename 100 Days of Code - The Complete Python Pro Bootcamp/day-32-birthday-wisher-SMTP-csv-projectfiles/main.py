##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

my_email = "undeadstarfish@gmail.com"
# get app password from gmail settings
password = "abc123"
letters = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
# print(year)

with open("birthdays.csv") as data:
    b_days = pandas.read_csv(data)

b_dict = b_days.to_dict(orient="records")
print(len(b_dict))

for entry in range(0,len(b_dict)):
    if b_dict[entry]["month"] == month and b_dict[entry]["day"] == day:
        letter = random.choice(letters)

        with open(letter) as file:
            orig = file.read()

        new_letter = orig.replace("[NAME]",b_dict[entry]["name"])
        print(new_letter)


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=b_dict[entry]["email"],
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )




# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




