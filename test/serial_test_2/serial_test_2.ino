int data = 0;

void setup() {
Serial.begin(9600);              //Starting serial communication
}
  
void loop() {
  if(Serial.available()){        // From RPi to Arduino, check if data available
    data = Serial.read();  // read as ASCII encoding
    Serial.println(data);        // send data as string to rpi
  }
}
