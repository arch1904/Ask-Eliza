/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

// the setup routine runs once when you press reset:
#include <math.h>
float heartpeaks = 0;
const int B=4275;                 // B value of the thermistor
const int R0 = 100000;            // R0 = 100k
const int pinTempSensor = A0;     // Grove - Temperature Sensor connect to A5
float starttime;
float heartbeat = 0;
boolean timercase = false;
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  heartpeaks;
  heartbeat;
  timercase;
  starttime;
  //Serial.println(timercase);
  // read the input on analog pin 0:
  int sensorValue = analogRead(A1);
  delay(1000);
  // print out the value you read:
  if (sensorValue>300){
    heartpeaks = heartpeaks + 1;
    if (not timercase){
    timercase = true;
    starttime = millis();
    
    }
  }
  //Serial.println(heartpeaks);
  Serial.println(sensorValue);
  heartbeat = heartpeaks * 600000/starttime;
  //Serial.println(heartbeat);
 // Serial.println(starttime);
  //Serial.println(timercase);
  //Serial.println(sensorValue);
{
    int a = analogRead(pinTempSensor );

    float R = 1023.0/((float)a)-1.0;
    R = 100000.0*R;

    float temperature=1.0/(log(R/100000.0)/B+1/298.15)-273.15;//convert to temperature via datasheet ;

    Serial.print("temperature = ");
    Serial.println(temperature);

    //delay(100);
}
}
