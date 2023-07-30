#define BLYNK_PRINT SwSerial
#include <SoftwareSerial.h>
SoftwareSerial SwSerial(10, 11); // RX, TX
#include <BlynkSimpleStream.h>
// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "6b3f585f3b784db6bb1027f6ef724b56";
void setup()
{
// Debug console
SwSerial.begin(9600);
// Blynk will work through Serial
// Do not read or write this serial manually in your sketch
Serial.begin(9600);
Blynk.begin(Serial,auth);
}
void loop()
{
Blynk.run();
// You can inject your own code or combine it with other sketches.
// Check other examples on how to communicate with Blynk. Remember
// to avoid delay() function!
}
