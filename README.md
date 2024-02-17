**Home Security Device Description:**


This home security device is a sophisticated system that integrates an Arduino Uno, PIR motion sensor, buzzer, and SIM900A GSM module. The device serves as an autonomous security solution for monitoring and alerting when motion is detected, indicating potential intrusion.



**Key Features:**


[1] Motion Detection: 

•	The PIR sensor is utilized to detect human motion within its range. When the sensor detects movement, the system triggers a series of actions to notify you of potential activity.


[2] Alert Mechanisms:

•	SMS Notification: The device sends an SMS alert to a predefined phone number, providing instant notification of detected motion.

•	Buzzer Activation: An audible alert is triggered by activating a buzzer, providing an additional layer of alerting within the premises.


[3] Communication with GSM Module:

•	The SIM900A GSM module facilitates communication with mobile networks, enabling SMS notifications to be sent to the designated recipient's phone.
User-Friendly Setup:

•	The system is designed to be user-friendly, with straightforward setup and configuration. The recipient's phone number can be easily configured in the code.
Security Integration:

•	The device contributes to home security by offering real-time alerts in the event of unauthorized movement, enhancing the overall safety of the premises.


[4] Arduino-based Control:

•	The use of an Arduino Uno as the microcontroller provides a flexible and programmable platform for implementing custom security logic and handling sensor data.


[5] Automation and Technology:

•	The device represents a technological advancement in home security, replacing traditional methods such as watchmen with an automated, efficient, and responsive system.


[6] Integration with Email:

•	it's important to note that the Gmail API integration might require additional configuration and is not fully implemented in the provided script.



**Considerations:**

•	Ensure proper power supply for prolonged operation.

•	Test the system thoroughly in different scenarios to validate its reliability.

•	Adjust sensitivity and delay parameters for the PIR sensor to suit the environment.

•	Implement secure practices for storing and handling sensitive information, such as phone numbers and credentials.


**Code Explanation:**


[1] Arduino Motion Detection with Email Notification:

•	This script uses an Arduino and a PIR motion sensor to detect motion.

•	When motion is detected, it sends an email notification using a specified Gmail account through the Gmail SMTP server.

•	The Arduino communicates with the computer through a serial port, and the script continuously monitors the Arduino's output for the "Motion Detected!" message.



[2] Gmail API Authentication and Label Listing:

•	This script demonstrates how to authenticate with the Gmail API using OAuth 2.0.

•	It retrieves and prints the list of labels (folders) in the authenticated user's Gmail account.

•	The OAuth 2.0 client credentials and token management are handled using the google-auth library.


[3] Google Cloud Project OAuth 2.0 Client Credentials:

•	This JSON configuration provides OAuth 2.0 client credentials for a Google Cloud project.

•	It includes details such as client ID, project ID, authorization and token endpoints, client secret, and redirect URIs.

•	These credentials are intended for authenticating and authorizing your application when interacting with Google APIs.


[4] Home Security Device with GSM Module and PIR Sensor:

•	This Arduino sketch interfaces with a SIM900A GSM module and a PIR motion sensor.

•	When motion is detected, it sends an SMS alert to a specified phone number and activates a buzzer for an audible alert.

•	The SIM900A GSM module is initialized, and AT commands are sent to set up SMS text mode. Motion detection triggers the SMS sending and buzzer activation.

•	The code continuously monitors the PIR sensor for motion in the main loop.
