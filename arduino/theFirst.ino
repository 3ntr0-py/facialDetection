#include <Servo.h>

int fromPi = 0;

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
servo2.attach(6);
}

void loop() {

  fromPi = Serial.read();

  // put your main code here, to run repeatedly:
  if(fromPi = 'A'){

    pos0 -= 1
    servo0.write(pos0)

    pos1 += 1
    servo1.write(pos1)

    pos2 -= 1
    servo2.write(pos2)

  }

  if(fromPi = 'B'){

    pos0 += 1
    servo0.write(pos0)

    pos1 += 1
    servo1.write(pos1)

    pos2 -= 1
    servo2.write(pos2)

  }

  if(fromPi = 'C'){

    pos0 -= 1
    servo0.write(pos0)

    pos1 += 1
    servo1.write(pos1)

    pos2 -= 1
    servo2.write(pos2)

  }

  if(fromPi = 'D'){

    pos0 += 1
    servo0.write(pos0)

    pos1 += 1
    servo1.write(pos1)

    pos2 -= 1
    servo2.write(pos2)

  }


  if(fromPi = 'W'){
    
    pos1 += 1
    servo1.write(pos1)

    pos2 -= 1
    servo2.write(pos2)

  }

  if(fromPi = 'X'){

    pos0 -= 1
    servo0.write(pos0)

  }

  if(fromPi = 'Y'){

    pos0 += 1
    servo0.write(pos0)

  }


  if(fromPi = 'Z'){
    
    pos1 -= 1
    servo1.write(pos1)

    pos2 += 1
    servo2.write(pos2)

  }

  if(fromPi = 'O'){
    servo0.write(pos0)
    servo1.write(pos1)
    servo2.write(pos2)
  } 
}