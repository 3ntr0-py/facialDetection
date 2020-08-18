#include <Servo.h>
Servo servo0;
Servo servo1;
int pos0 = 0;
int pos1 = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
servo0.attach(3);
servo1.attach(5);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(pos0 = 0; pos0 <= 180; pos0 += 1){
      servo0.write(pos0);
      delay(5);
    }
  for(pos0 = 180; pos0 >= 0; pos0 -= 1){
      servo0.write(pos0);
      delay(5);
    }  
  for(pos1 = 0; pos1 <= 180; pos1 += 1){
      servo1.write(pos1);
      delay(5);
    }
  for(pos1 = 180; pos1 >= 0; pos1 -= 1){
      servo1.write(pos1);
      delay(5);
    }  
}