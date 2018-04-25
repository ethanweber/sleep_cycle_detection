#include <MPU9250_asukiaaa.h>
#include "DHT.h"

#define DHTPIN 2     // what digital pin we're connected to
#define DHTTYPE DHT11   // DHT 11

#ifdef _ESP32_HAL_I2C_H_
#define SDA_PIN 26
#define SCL_PIN 25
#endif

#define motorPWM1 10
#define motorPWM2 11


MPU9250 mySensor;

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

uint8_t sensorId;
float aX, aY, aZ, aSqrt, gX, gY, gZ, mDirection, mX, mY, mZ;

void write_command(float velocity) {
  int cmd = abs(int(velocity*1023));
  if (velocity >= 0) {
    analogWrite(motorPWM1, cmd);
    analogWrite(motorPWM2, LOW);
  }
  else {
    analogWrite(motorPWM1, LOW);
    analogWrite(motorPWM2, cmd);
  }
}

void setup() {
  while(!Serial);
  Serial.begin(115200);
//  Serial.println("started");

  dht.begin();

  analogWrite(motorPWM1, LOW);
  analogWrite(motorPWM2, LOW);

#ifdef _ESP32_HAL_I2C_H_ // For ESP32
  Wire.begin(SDA_PIN, SCL_PIN); // SDA, SCL
#else
  Wire.begin();
#endif

  mySensor.setWire(&Wire);
  mySensor.beginAccel();
  mySensor.beginGyro();
  mySensor.beginMag();

  // You can set your own offset for mag values
  // mySensor.magXOffset = -50;
  // mySensor.magYOffset = -55;
  // mySensor.magZOffset = -10;

  sensorId = mySensor.readId();
}

void loop() {
//  Serial.println("sensorId: " + String(sensorId));

  write_command(.5);

  mySensor.accelUpdate();
  aX = mySensor.accelX();
  aY = mySensor.accelY();
  aZ = mySensor.accelZ();
  aSqrt = mySensor.accelSqrt();
  Serial.print("acc_x:" + String(aX));
  Serial.print(",acc_y:" + String(aY));
  Serial.print(",acc_z:" + String(aZ));
//  Serial.println("accelSqrt: " + String(aSqrt));

  mySensor.gyroUpdate();
  gX = mySensor.gyroX();
  gY = mySensor.gyroY();
  gZ = mySensor.gyroZ();
  Serial.print(",gyro_x:" + String(gX));
  Serial.print(",gyro_y:" + String(gY));
  Serial.print(",gyro_z:" + String(gZ));

  mySensor.magUpdate();
  mX = mySensor.magX();
  mY = mySensor.magY();
  mZ = mySensor.magZ();
  mDirection = mySensor.magHorizDirection();
  Serial.print(",mag_x:" + String(mX));
  Serial.print(",mag_y:" + String(mY));
  Serial.print(",mag_z:" + String(mZ));
//  Serial.println("horizontal direction: " + String(mDirection));

//  Serial.println("at " + String(millis()) + "ms");
//  Serial.println(""); // Add an empty line

  float h = dht.readHumidity();
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(f)) {
    h = 0.0;
    f = 0.0;
  }
  Serial.print(",humid:" + String(h));
  Serial.println(",temp:" + String(f));



  delay(500);
}
