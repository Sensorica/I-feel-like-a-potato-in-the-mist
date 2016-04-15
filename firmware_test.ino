#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"



Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myMotor1 = AFMS.getMotor(1);// port M1
Adafruit_DCMotor *myMotor2 = AFMS.getMotor(2);// port M2
int motorSpeed[] = {150, 200};
int motorDirection[] = {FORWARD, FORWARD};
boolean  Motor1Boolean ;
boolean Motor2Boolean ;
int Sensor0 ; // Sensor0 connected to this digital pin number
int Sensor1 ; // Sensor1 connected to this digital pin number
int Sensor2 ; // Sensor1 connected to this digital pin number
int PrevSensor0, PrevSensor1, PrevSensor2;
char inChar;
int counterM1; 
int counterM2;

void setup() {
  // initialize things
  Motor1Boolean = false;
  Motor2Boolean = false;

  // set SENSOR pins as digital in
  Sensor0 = 5; // Sensor0 connected to this digital pin number
  Sensor1 = 6; // Sensor1 connected to this digital pin number
  Sensor2 = 7; // Sensor1 connected to this digital pin number
  pinMode(Sensor0, INPUT); // Define Sensor0 as a digital in pin
  pinMode(Sensor1, INPUT); // Define Sensor2 as a digital in pin
  pinMode(Sensor2, INPUT); // Define Sensor2 as a digital in pin

  

  Serial.begin(9600);
  
  //initial motor speed
  initializeShield();
  
}

// the loop function runs over and over again forever
void loop() {
  PrevSensor0 = readSensor(Sensor0);//HIGH;
  PrevSensor1 = readSensor(Sensor1);//LOW;
  PrevSensor2 = readSensor(Sensor2);

//Serial.println (PrevSensor0);
//Serial.println (PrevSensor1);
//Serial.println (PrevSensor2);  

  if (PrevSensor0 == HIGH && readSensor(Sensor0) == LOW) // if hole
  {

    PrevSensor0 = readSensor(Sensor0);
    Motor1Boolean = true;
    Motor2Boolean = true;

    moveMotor(myMotor1, FORWARD, motorSpeed[1]); // move Motor1
    moveMotor(myMotor2, BACKWARD, motorSpeed[0]); // move Motor2
    counterM1 = millis();
    counterM2 = counterM1;
  }

  if ( Motor1Boolean == true)
  {
    if (PrevSensor1 == LOW && readSensor(Sensor1) == HIGH) // if hole
    {
      if (millis() - counterM1 >= 240){ 
        Motor1Boolean = false;
        stopMotor(myMotor1); // stop Motor1
      }
    }
  }

  if ( Motor2Boolean == true)
  {
    if (PrevSensor2 == LOW && readSensor(Sensor2) == HIGH) // if hole
    {
     long runTime = millis() - counterM2; 
      if (runTime >= 240)
      {
        Motor2Boolean = false;
        stopMotor(myMotor2); // stop Motor2
      }
      else {
        Serial.println (runTime);
      }
    }
  }
}
int readSensor(int sensor) {

  return digitalRead(sensor);

}
void moveMotor(Adafruit_DCMotor *myMotor, int directionFB, uint8_t speed) {
  myMotor->setSpeed(speed);
  myMotor->run(directionFB);
}

void moveMotor(Adafruit_DCMotor *myMotor, int directionFB) {
  moveMotor(myMotor, directionFB, motorSpeed[0]); // this needs to be assigned to the correct motor
}

void stopMotor(Adafruit_DCMotor *myMotor) {
  myMotor->run(RELEASE);
}

void initializeShield() {
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz

  // Set the speed to start, from 0 (off) to 255 (max speed)
  myMotor1->setSpeed(motorSpeed[0]);
  myMotor2->setSpeed(motorSpeed[1]);

  //myMotor->run(FORWARD);
  // turn on motor
  //myMotor->run(RELEASE);
}
void initializeMotor() {

}
