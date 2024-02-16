import serial
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = 'sender@example.com'  # Replace with your email
receiver_email = 'receiver@example.com'  # Replace with recipient's email
password = 'entervalidpassword'  # Replace with your email password
smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server

# Arduino serial port
arduino_port = 'COM5    '  # Replace with your Arduino's serial port
baud_rate = 9600

# Create message container
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Motion Detected!'

# Email content
body = 'Motion has been detected by the Arduino.'
message.attach(MIMEText(body, 'plain'))

# Function to send email
def send_email():
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, 587)  # Gmail SMTP port is 587
        server.starttls()

        # Login to your email accountP
        server.login(sender_email, password)

        # Send email
        server.send_message(message)
        print('Email sent successfully!')

        # Quit SMTP server
        server.quit()
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Main code to read from serial port
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line == "Motion Detected!":
            send_email()
except KeyboardInterrupt:
    pass
finally:
    ser.close()
