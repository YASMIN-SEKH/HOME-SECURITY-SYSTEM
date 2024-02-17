import serial
import smtplib
import time

# Configure the Arduino's serial port (change the port name as needed)
arduino_port = 'COM5'  # Replace with the correct port name for your Arduino
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)

# Email configuration
gmail_user = 'NAME@EXAMPLE.com' #ENTER VALID EMAIL ADDRESS FROM WHICH YOU WANT TO SEND EMAIL
gmail_password = 'XXXX XXXX XXXX XXXX'  # Use an application-specific password if required 
to_email = 'RECIEVER@EXAMPLE.com' #ENTER VALID EMAIL ADDRESS OF THE RECEIVER

while True:
    arduino_data = ser.readline().decode('utf-8').strip()
    if "Motion detected!" in arduino_data:
        subject = "Motion Detected"
        body = "Motion was detected by your Arduino!"

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(gmail_user, to_email, message)
            server.quit()
            print("Email sent.")
        except Exception as e:
            print("Error sending email:", str(e))
    time.sleep(1)
