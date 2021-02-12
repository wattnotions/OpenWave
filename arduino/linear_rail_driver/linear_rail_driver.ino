/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  This example code is in the public domain.
 */

// Pin 13 has an LED connected on most Arduino boards.
// Pin 11 has the LED on Teensy 2.0
// Pin 6  has the LED on Teensy++ 2.0
// Pin 13 has the LED on Teensy 3.0
// give it a name:
int led = 13;
byte data[1500];
char nbyte;

#define END_STOP digitalRead(12) // 1 is not pressed 0 is pressed
#define OFF 1
#define ON 0


// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  // h bridge signals
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  //end stop
  pinMode(12,INPUT_PULLUP);

  Serial.begin(9600);
  Serial1.begin(115200);
  
}

// the loop routine runs over and over again forever:

int step_count,i;
unsigned long start_time, end_time, delta;
void loop() {

  while(1){
    ser_test();
  }
 

  

  go_home(2000);
  stepper_off();
  while(1){}
  
}

void ser_test(void){
  Serial1.println("a");
  Serial.println("sent a , waiting for resp");
  while(Serial1.available() == 0){}
  Serial.println("resp received");
  nbyte = Serial1.read();
  Serial.println(nbyte);
}

void go_home(int ms_delay){
  
  while(END_STOP == OFF){  //go down until the endstop is pressed
    down(ms_delay);
  }


  while(END_STOP == ON){ //go up just until the end stop is released
    up(ms_delay);
  }

  step_count = 0;
}

void stepper_off(void) { //puts all h bridge signal pins low to prevent current draw by stepper
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
}

void down(int delay_us){
  digitalWrite(2, HIGH);   
  digitalWrite(3, LOW);  
  delayMicroseconds(delay_us); 
  step_count--;
  
  digitalWrite(4, HIGH);   
  digitalWrite(5, LOW);
  delayMicroseconds(delay_us);
  step_count--;

  digitalWrite(2, LOW);   
  digitalWrite(3, HIGH);
  delayMicroseconds(delay_us);
  step_count--;
    
  digitalWrite(4, LOW);   
  digitalWrite(5,HIGH);
  delayMicroseconds(delay_us);   
  step_count--;
}

void up(int delay_us){
  digitalWrite(4, HIGH);   
  digitalWrite(5, LOW);
  delayMicroseconds(delay_us);
  step_count++;
  
  digitalWrite(2, HIGH);   
  digitalWrite(3, LOW);  
  delayMicroseconds(delay_us); 
  step_count++;
  
  digitalWrite(4, LOW);   
  digitalWrite(5,HIGH);
  delayMicroseconds(delay_us);  
  step_count++;

  digitalWrite(2, LOW);   
  digitalWrite(3, HIGH);
  delayMicroseconds(delay_us);
  step_count++;
    
    
}
