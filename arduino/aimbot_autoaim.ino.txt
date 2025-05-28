#include <Mouse.h>

String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  Mouse.begin();
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
      break;
    } else {
      inputString += inChar;
    }
  }

  if (stringComplete) {
    int commaIndex = inputString.indexOf(',');
    if (commaIndex > 0) {
      int dx = inputString.substring(0, commaIndex).toInt();
      int dy = inputString.substring(commaIndex + 1).toInt();
      Mouse.move(dx, dy, 0);
    }
    inputString = "";
    stringComplete = false;
  }
}
