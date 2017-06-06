/*
 * Zender.ino
 * 
 * Geschreven door Mark & Clemens
 * Project ISEN
 * Versie: 1.0
 */

/*
 * Deze library is nodig voor de communicatie via 433mhz
 * 
 */
#include <VirtualWire.h>
#include <avr/sleep.h>
#include <avr/wdt.h>
#define RELAY1  7  
/*
 * Hier declareren we 2 waardes, SensorNummer en SensorWaarde.
 * Ook defineren we de Array, genaamd Istr. Met een lengte van 6
 */
int SensorNummer;
int SensorWaarde;
char Istr[6];
/*
 * Dit is nodig voor de soil meter, deze is op pin A0 aangesloten (Analoog)
 * Ook moet de output value een integer zijn.
 */
int sensor_pin = A0; 
int output_value ;

/* 
 *  In de setup zetten wij neer wat de Arduino nodig heeft om te kunnen werken
 *  Hier zetten wij de TX pin (van het verzenden) op pin D12 (digital)
 *  Ook moet vw_set_ptt_inverted aan omdat wij met een DRS3100 werken
 *  vw_setup() moet op 4000 staan voor de DRS3100, dit is het aantal bits per seconde.
 *  Daarna geven we een delay aan.
 */
 
// watchdog interrupt
ISR (WDT_vect) 
{
   wdt_disable();  // disable watchdog
}  // end of WDT_vect

void setup()
{
  pinMode(RELAY1, OUTPUT);       
  digitalWrite(RELAY1,1);    
  Serial.begin(9600);
  vw_set_tx_pin(12);        
  vw_set_ptt_inverted(true); 
  vw_setup(4000); 
  delay(2500);
  
}

void myWatchdogEnable(const byte interval)
  { 
  MCUSR = 0;                          // reset various flags
  WDTCSR |= 0b00011000;               // see docs, set WDCE, WDE
  WDTCSR =  0b01000000 | interval;    // set WDIE, and appropriate delay

  wdt_reset();
  set_sleep_mode (SLEEP_MODE_PWR_DOWN); 
  sleep_mode();            // now goes to Sleep and waits for the interrupt
  }

void sendData(){    
    for(int i=0; i <= 10; i++){
      output_value = analogRead(sensor_pin);
      output_value = map(output_value,1023,431,0,100); //A1
      //output_value = map(output_value,1023,140,0,100); //A2
      int SensorNummer = 1;

      if(output_value > 100){
        output_value = 99;           
      }

      if(i == 10 and output_value < 25){
        pompje();
       }

      if(output_value == 0){
        output_value = 1;
      }
      else{
        output_value = output_value;
      }
      Serial.println(output_value);
      Istr[0] = SensorNummer;
      Istr[1] =  output_value;
        if(SensorNummer > 0){
           vw_send((uint8_t *)Istr, strlen(Istr));
           vw_wait_tx(); // Wait until the whole message is gone
        }
    }   
}

void pompje(){
        Serial.println("Pompje gaat aan");
        digitalWrite(RELAY1,0);
        delay(8000);
        digitalWrite(RELAY1,1);  
}

void loop(){
  sendData();
  //sleep for a total of 240 seconds
  int i;
  for (i = 0; i < 450; i++)
  { 
    myWatchdogEnable (0b100001);  // 8 seconds
  }
  
}
