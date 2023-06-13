import csv
import os
import smtplib

# Function to send an email
def send_email(subject, message, recipient):
    sender = "cedric@yahoo.com"  
    password = "H12tokyo404@"  

# Construct the email body
    body = "\r\n".join([
        "From: {}".format(sender),
        "To: {}".format(recipient),
        "Subject: {}".format(subject),
        "Content-Type: text/html",
        "",
        message
    ])

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  
# Replace with your email provider's SMTP server
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, body)
        print("Email sent successfully to", recipient)
    except Exception as e:
        print("Error sending email to", recipient, ":", str(e))
    finally:
        server.quit()

# Function to send emails to multiple recipients
def send_emails(csv_file, subject, message):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            recipient = row[0]  
# Assuming email addresses are in the first column of the CSV
            send_email(subject, message, recipient)

# Set the email subject and message
subject = "Tech, Crypto, NFT News"
message = """
<html>
<body>
<p>Dear Tech Enthusiast,</p>
<p>Join our platform today</p>
<ol>
  <li>It's as simple as <a href="https://cointelegraph.com/">clicking here</a>, signing up, and gaining access to a wide range of technological discoveries and events </li>
  <li>Are you ready to dive into the fascinating world of technology? We have some exciting news to share with you!
Cutting-Edge Gadgets: Discover the latest gadgets that are revolutionizing the tech scene. From smart home devices to futuristic wearables, explore the innovative technologies that are shaping our future.
Tech Trends: Stay ahead of the curve with our in-depth analysis of the latest tech trends. We'll keep you updated on breakthroughs in artificial intelligence, blockchain, cybersecurity, and more. Be prepared to geek out!
Exclusive Offers: As a valued member of our tech community, you'll gain access to exclusive offers and discounts on top tech products. Don't miss out on the chance to upgrade your tech arsenal at unbeatable prices.</li>
  <li>Quick and Secure Payments: No more waiting around. Once you reach the payout threshold, request your payment and receive your well-deserved rewards quickly and securely. Your earnings are just a click away.</li>
</ol>
<p>If you have any questions or need assistance, our dedicated support team is here to help. Simply reply to this email, and we'll be happy to assist you.</p>
</body>
</html>
"""

# Set the CSV file path
current_dir = os.path.dirname(os.path.abspath(__file__))  
# Get the current directory
csv_file = os.path.join(current_dir, "10kemails.csv")  
# Construct the CSV file path

# Send the emails
send_emails(csv_file, subject, message)