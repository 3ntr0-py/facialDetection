#include <Servo.h>
Servo servo0;
Servo servo1;
Servo servo2;
int pos0 = 0;
int pos1 = 0;
int pos2 = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
servo0.attach(3);
servo1.attach(5);
servo2.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:

  //servo 0
  for(pos0 = 0; pos0 <= 180; pos0 += 1){
      servo0.write(pos0);
      delay(5);
    }
  for(pos0 = 180; pos0 >= 0; pos0 -= 1){
      servo0.write(pos0);
      delay(5);
    } 
  //servo 1 
  for(pos1 = 0; pos1 <= 180; pos1 += 1){
      servo1.write(pos1);
      delay(5);
    }
  for(pos1 = 180; pos1 >= 0; pos1 -= 1){
      servo1.write(pos1);
      delay(5);
    } 
  //servo 2
  for(pos2 = 0; pos2 <= 180; pos2 += 1){
      servo2.write(pos2);
      delay(5);
    }
  for(pos2 = 180; pos2 >= 0; pos2 -= 1){
      servo2.write(pos2);
      delay(5);
    } 
}