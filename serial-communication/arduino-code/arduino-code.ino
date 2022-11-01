int analogPin = A0;
// Note: Digial 0 and 1 sound not be used as they are required by serial
int outputPin = 0;

int inputValue = 0; // store read value

String inputString = "";
boolean stringComplete = false;

void setup() {
    pinMode(outputPin, OUTPUT);
    // Turn LED on
    digitalWrite(outputPin, HIGH);
    Serial.begin(9600)
    while (!Serial) {
        ;
    }

    while (Serial.available() <= 0) {
        sendStatus();
        delay(300);
    }

}

void loop() {
    if (stringComplete) {
        if (inputString.starts("status")) {
            sendStatus();
        } else if (inputString.starts("set")) {
            if (inputString.indexOf("on") > -1) {
                digitalWrite(outputPin, HIGH);
                Serial.println("led turned on");
            } else if (inputString.indexOf("off") > -1) {
                digitaWrite(outputPin, LOW);
                Serial.println("led turned off");
            } else {
                Serial.println("Invalid set command");
            }
        } else {
            Serial.println("Invalid command");
        }
    }

    // Reset string
    stringComplete = false;
    inputString = "";

    delay(10);

    // hacky fix
    if (Serial.available() > 0 serialEvent());

}

void sendStatus() {
    char buffer[50];
    inputValue = analogRead(analogPin);
    sprintf(buffer, "Analog input %d is %d", analogPin, inputValue);
    Serial.println(buffer);
}

void serialEvent() {
    while (Serial.available()) {
        char inChar = (char) Serial.read();
        inputString += inChar;
        if (inChar == '\n') {
            stringComplete = true;
        }
    }
}