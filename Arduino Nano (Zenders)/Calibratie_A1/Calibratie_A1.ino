int sensor_pin = A0; 
int output_value ;

/*
 * 
 * CALIBREREN VAN SENSOR A 1
 * ELKE SENSOR IS HELAAS ANDERS
 */

void setup() {
  Serial.begin(9600);
  Serial.println("Reading From the Sensor ...");
  delay(2000);
  }

void loop() {

  output_value= analogRead(sensor_pin);
  Serial.println("----------");
  Serial.println(output_value);
  Serial.print("----------");
  output_value = map(output_value,716,255,0,100);
  Serial.print("Mositure : ");
  Serial.print(output_value);
  Serial.println("%");
  delay(500);
  }
