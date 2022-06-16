import smtplib
import getpass

# Get email ID and password from user
email = input("Enter Motaz ID: ")
password = getpass.getpass("Enter password: ")

# Set SMTP host and port
if "gmail" in email:
    host = "smtp.gmail.com"
    port = 587
else:
    print("Invalid email ID, please try again")
    exit(0)

# Create SMTPLib object and contact server
server = smtplib.SMTP(host, port)
check = server.ehlo()
if check[0] == 250:
    print("Successfully contacted mail server")
else:
    print("Unable to contact server")
    exit(0)

# Start TLS encryption (only to be done if conencting to port 587 i.e. TLS)
server.starttls()

# Logging into the server
try:
    server.login(email, password)
    print("Login successful")
except smtplib.SMTPAuthenticationError as ex:
    print("Exception:", ex)
    exit(0)

# Get email details from user
sender_mail = email
receiver_email = input("Enter receiver's email: ")
subject = input("Enter email subject: ")
content = input("Enter email content: ")
# Create email body by merging emails object and content
body = "Subject: " + subject + "\n" + content

# Send the mail
output = server.sendmail(sender_mail, receiver_email, body)
if not len(output):
    print("Send mail successfully")
else:
    print("Unable to send mail, please try again")
    exit(0)
