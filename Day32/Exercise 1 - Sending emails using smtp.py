# SMTP = simple mail transfer protocol with the following flow:

# - a sender
# - a recipient
# - the sender sends an email to the recipient, the recipient's mail server keeps the email until the user logs in and downloads it

import smtplib

MY_EMAIL_GMAIL = "appbreweryinfo@gmail.com"
MY_EMAIL_YAHOO = "appbrewerytesting@yahoo.com"
MY_PASSWORD = "abcd1234()"
SMTP_INFO = "smtp.gmail.com"

with smtplib.SMTP(SMTP_INFO) as connection:
    # encrypt the msj for security reasons
    connection.starttls()
    # login
    connection.login(user=MY_EMAIL_GMAIL, password=MY_PASSWORD)
    # send the email
    connection.sendmail(from_addr=MY_EMAIL_GMAIL,
                        to_addrs=MY_EMAIL_YAHOO, msj="Subject:Hello\n\nThis is the body of my email.")
    # close the connection only when we did not use the with keyword
    # connection.close()
