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

// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  
}

// the loop routine runs over and over again forever:
void loop() {

  
   
  
  
  
     
  

  



  
             
}


void forward(delay_us){
  digitalWrite(2, HIGH);   
  digitalWrite(3, LOW);  
  delayMicroseconds(delay_us); 

  digitalWrite(4, HIGH);   
  digitalWrite(5, LOW);
  delayMicroseconds(delay_us);

  digitalWrite(2, LOW);   
  digitalWrite(3, HIGH);
  delayMicroseconds(delay_us);
    
  digitalWrite(4, LOW);   
  digitalWrite(5,HIGH);
  delayMicroseconds(delay_us);   
}

void reverse(delay_us){
  digitalWrite(4, HIGH);   
  digitalWrite(5, LOW);
  delayMicroseconds(delay_us);
  
  digitalWrite(2, HIGH);   
  digitalWrite(3, LOW);  
  delayMicroseconds(delay_us); 

  digitalWrite(4, LOW);   
  digitalWrite(5,HIGH);
  delayMicroseconds(delay_us);  

  digitalWrite(2, LOW);   
  digitalWrite(3, HIGH);
  delayMicroseconds(delay_us);
    
    
}
