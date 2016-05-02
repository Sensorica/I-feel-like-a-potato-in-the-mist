#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myMotor1 = AFMS.getMotor(2);// port M1
Adafruit_DCMotor *myMotor2 = AFMS.getMotor(1);// port M2
int motorSpeed[] = {120, 120};
int motorDirection[] = {FORWARD, BACKWARD};

const byte sensor0 = A0;
const byte sensor1 = 2;
const byte sensor2 = 3;



void setup() {

  pinMode(sensor0, INPUT_PULLUP);  
  pinMode(sensor1, INPUT_PULLUP);
  pinMode(sensor2, INPUT_PULLUP);
  
  
  cli();		
  PCICR =0x02;          // Enable PCINT1 interrupt
  PCMSK1 = 0b00000111;
  sei();		
  
  
  attachInterrupt(digitalPinToInterrupt(sensor1), stopM1, RISING);
  attachInterrupt(digitalPinToInterrupt(sensor2), stopM2, RISING);

  //initial motor speed
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz

  // Set the speed to start, from 0 (off) to 255 (max speed)
  myMotor1->setSpeed(motorSpeed[0]);
  myMotor2->setSpeed(motorSpeed[1]);

}

void loop() {
  //digitalWrite(ledPin, state);
}

ISR(PCINT1_vect)  {
  myMotor1->run(FORWARD);
  myMotor2->run(FORWARD);
}
void stopM1() {
  myMotor1->run(RELEASE);
}
void stopM2() {
  myMotor2->run(RELEASE);
}