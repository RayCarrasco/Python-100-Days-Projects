# import smtplib
# import os
# my_email = "example@gmail.com"
# my_password = "123:"
#
# test_email = "example@yahoo.com"
# test_password = "123"
#
# # For google
# # with smtplib.SMTP("smtp.gmail.com") as connection:
#
# # For yahoo, port 587 is recomended in yahoo, otherwise it won't work
# with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=test_email, password=test_password)
#     connection.sendmail(
#         from_addr=test_email,
#         to_addrs=my_email,
#         msg="subject:Hello from yahoo\n\n "
#             "This is the body of my email"
#     )

import datetime as dt
now = dt.datetime.now()
year = now.year

# days starts from 0 for monday and so on
week_day = now.weekday()

print(week_day)
day_of_birth = dt.datetime(year=1994, month=11, day=18, hour=4)

print(day_of_birth)
