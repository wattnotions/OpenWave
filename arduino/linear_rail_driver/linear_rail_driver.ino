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
  
}

// the loop routine runs over and over again forever:

int step_count,i;
void loop() {

  go_home();

  while(1){
    Serial.println("START OF WHILE LOOP");
    i=0;
    while(step_count < 7000){
      
      up(5000);
      Serial.println(step_count);
      if(END_STOP == ON) {
        Serial.println("END STOP PRESSED");
        while(1){};
        }
    }

    i=0;
    Serial.println("OUT OF FIRST LOOP");
    while(step_count > 0){
     
      down(5000);
      Serial.println(step_count);
      if(END_STOP == ON) {
        Serial.println("END STOP PRESSED");
        while(1){};
        }
    }
    
  }
  
  while(1){}

  
}

void go_home(void){
  
  while(END_STOP == 1){
    down(5000);
    Serial.println(step_count);
  }


  while(END_STOP == 0){
    up(5000);
    Serial.println(step_count);
  }

  step_count = 0;
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
