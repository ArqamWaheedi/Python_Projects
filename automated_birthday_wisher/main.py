# Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import random
my_email = "arqam4361@gmail.com"
password = "lafarlggskucrrqe"

# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthday_dict = {(row.month, row.day): row for (index, row) in df.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filepath) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        # connection.set_debuglevel(debuglevel=1)  # see the transaction details
        connection.starttls()  # encrypt following SMTP commands
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="arqam.waheedi@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{new_contents}")
