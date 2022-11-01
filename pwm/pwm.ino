#include <Servo.h>
byte servoPin = 9;
byte servoPin1 = 5;
Servo servo;
Servo servo1;

void setup() {
  // Initialize Serial communication to see printed values
  Serial.begin(9600);

  servo.attach(servoPin);
  servo1.attach(servoPin1);

  servo.writeMicroseconds(1500); // send "stop" signal to ESC (Electronic Speed Controller).
  servo1.writeMicroseconds(1500);

  //change back to 7
  //delay(1000); // delay to allow the ESC to recognize the stopped signal
}


void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    int pwmVal1 = 0;
    int i = 0;
    while (data[i] != '|') {
      pwmVal1 = pwmVal1 * 10 + ((int)data.charAt(i) - 48);
      i++;
    }
    
    i++;

    int pwmVal2 = 0;
    while (i < data.length()) {
      pwmVal2 = pwmVal2 * 10 + ((int)data.charAt(i) - 48);
      i++;
    }
    
    servo.writeMicroseconds(pwmVal1);
    servo1.writeMicroseconds(pwmVal2);

    //Serial.println(dat:a);
    Serial.println("PWM1: " + String(pwmVal1) + " PWM2: " + String(pwmVal2));
    //Serial.println(" ");

    // delay for 3 seconds to test
    //delay(3000);
    
  }
}