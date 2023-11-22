/*
 Name:    step_drive.ino
 Author:  mertwhocodes
*/

#include<mwc_stepper.h>

#define EN_PIN 3
#define DIR_PIN 2
#define STEP_PIN 4

#define RPM 50
#define RPM1 50

#define PULSE 1600

#define ClOCKWISE 1
#define OTHERWISE 0

#define SWITCHPIN A0   // pin for the home position microswitch

MWCSTEPPER nema23(EN_PIN, DIR_PIN, STEP_PIN);

void setup() {

  nema23.init();
  pinMode(SWITCHPIN, INPUT_PULLUP);
  Serial.begin(9600);
  
  //nema23.active(DEACTIVE);
}

void loop() {
  

  bool home_switch;
  home_switch= digitalRead(SWITCHPIN);
  Serial.println(home_switch);

  nema23.set(ClOCKWISE, RPM, PULSE); //clock=down
  
  while(home_switch == 1){
    home_switch= digitalRead(SWITCHPIN);
    nema23.run();
      
  }
  
    delay(1000);
  
    nema23.set(OTHERWISE, RPM1, PULSE);
  
    for (size_t i = 0; i < 5000; i++)
    {
      nema23.run();
    }

  
}
