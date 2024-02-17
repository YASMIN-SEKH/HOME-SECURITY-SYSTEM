#include <SoftwareSerial.h>

SoftwareSerial SIM900(0, 1); // RX, TX for SIM900L GSM module
int pirPin = 2;              // PIR sensor output pin
int buzzerPin = 3;           // Buzzer control pin

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(buzzerPin, OUTPUT); // Set the buzzer pin as an output
  Serial.begin(9600);  // Initialize the serial monitor for debugging
  SIM900.begin(9600);  // Initialize the SIM900 module
  delay(20000);        // Wait for the SIM900 module to initialize (adjust as needed)
  SIM900.println("AT"); // Send AT command to check communication with the module
  delay(1000);
  SIM900.println("AT+CMGF=1"); // Set SMS text mode
  delay(1000);
}

void loop() {
  int pirState = digitalRead(pirPin);

  if (pirState == HIGH) {
    Serial.println("Motion detected!");
    sendSMS("Security Alert: Motion detected!");
    activateBuzzer(); // Activate the buzzer
    delay(1000); // Delay to prevent multiple notifications in a short time (adjust as needed)
    deactivateBuzzer(); // Deactivate the buzzer
  }

  delay(500);
}

void sendSMS(String message) {
  SIM900.println("AT+CMGF=1"); // Set SMS text mode
  delay(1000);
  SIM900.print("AT+CMGS=\"+919898953299\"\r"); // Replace with the recipient's phone number
  delay(1000);
  SIM900.print(message); // Send the message
  delay(1000);
  SIM900.write(26); // Send Ctrl+Z to end the SMS
  delay(1000);
}

void activateBuzzer() {
  digitalWrite(buzzerPin, HIGH); // Turn on the buzzer (active HIGH)
}

void deactivateBuzzer() {
  digitalWrite(buzzerPin, LOW); // Turn off the buzzer
}
