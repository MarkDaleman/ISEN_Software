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
void setup()
{
  Serial.begin(9600);    // Debugging only
  Serial.println("VirtualWire setup...");
  vw_set_tx_pin(12);        
  // Initialise the IO and ISR
  vw_set_ptt_inverted(true); 
  vw_setup(4000); 
  delay(250); 
  Serial.println("VirtualWire setup complete");
  delay(250); 
}
/*
 * Hieronder is de Main loop. Deze zal continu draaien op de Arduino
 * Sensornummer is voor elke sensor anders. Deze Arduino heeft ID 5
 * De Waarde van de komt uit de soil vochtigheid meter
 * Vervolgens stoppen we de waarde en sensornummer in de Array
 * De Array versturen we met vw_send richting de Raspberry Pi
 * Daarna wachten we tot het bericht is verzonden en gaan we in slaap
 */
void loop(){
  Serial.println("Reading sensor and sending data");
  output_value = analogRead(sensor_pin);
  output_value = map(output_value,1023,140,0,100);
  Serial.println(output_value);
  int SensorNummer = 1;           
  Istr[0] = SensorNummer;
  Istr[1] =  output_value;
  if(SensorNummer > 0 and output_value < 100){
     vw_send((uint8_t *)Istr, strlen(Istr));
     vw_wait_tx(); // Wait until the whole message is gone
  }
  delay(1000);
}
