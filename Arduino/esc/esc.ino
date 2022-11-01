#include <Servo.h>
byte servoPin = 9;
byte servoPin1 = 5;
Servo servo;
Servo servo1;

const int trigPin = 11;
const int echoPin = 10;
int iteration = 0;
int sensor_counter = 0;
// defines variables
long duration;
int distance;

void setup() {
  // Initialize Serial communication to see printed values
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600);

  servo.attach(servoPin);
  servo1.attach(servoPin1);

  servo.writeMicroseconds(1500); // send "stop" signal to ESC (Electronic Speed Controller).
  servo1.writeMicroseconds(1500);

  delay(7000); // delay to allow the ESC to recognize the stopped signal
}


void loop() {
  // put your main code here, to run repeatedly:
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance= duration*0.034/2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);
  if (distance < 100 && iteration > 100) {
    if (sensor_counter > 10) {
      while (true) {
        servo.writeMicroseconds(1500);
        servo1.writeMicroseconds(1500);
      }
    } else {
      sensor_counter++;
    }
  } else {
    sensor_counter = 0;
  }
  if (iteration < 101) {
    iteration++;
  }
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int servoVal = data[0] - 48;

    int pwmVal = 0;
    for (int i = 1; i < data.length(); i++) {
      if (data[i] == '.') {
        break;
      }
      pwmVal = pwmVal * 10 + (data.charAt(i) - 48); 
    }
    
    if (servoVal == 0) {
      servo.writeMicroseconds(pwmVal);
    } else {
      servo1.writeMicroseconds(pwmVal);
    }
   
    Serial.println("Port: " + String(servoVal) + " PWM: " + String(pwmVal));
    Serial.println(" ");

    // delay for 3 seconds to test
    //delay(3000);
    
  }
}
