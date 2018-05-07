/*
  Analog input, analog output, serial output

  Reads an analog input pin, maps the result to a range from 0 to 255 and uses
  the result to set the pulse width modulation (PWM) of an output pin.
  Also prints the results to the Serial Monitor.

  The circuit:
  - potentiometer connected to analog pin 0.
    Center pin of the potentiometer goes to the analog pin.
    side pins of the potentiometer go to +5V and ground
  - LED connected from digital pin 9 to ground

  created 29 Dec. 2008
  modified 9 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogInOutSerial
*/

// These constants won't change. They're used to give names to the pins used:
const int left = A3;  // Analog input pin that the potentiometer is attached to
const int right = A5; // Analog output pin that the LED is attached to

void setup() {
  // initialize serial communications at 9600 bps:
  while(!Serial);
  Serial.begin(115200);
}

void loop() {
  // read the analog in value:
  float leftValue = analogRead(left);
  float rightValue = analogRead(right);

  // print the results to the Serial Monitor:
  Serial.print("left:" + String(leftValue));
  Serial.println(",right:" + String(rightValue));

  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(40);
}
