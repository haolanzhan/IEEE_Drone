int data = 0;

void setup() {
Serial.begin(9600);              //Starting serial communication
}
  
void loop() {
  if (//condition to send instruction to rpi){
    Serial.write(1);
    while(Serial.available()){}// wait for return
    wear_or_not = Serial.read() // 2 wear, 3 not wear, 4 fail
    // any code for print out the prediction
  }
  // ignore whatever below
  //if(Serial.available()){        // From RPi to Arduino, check if data available
    //data = Serial.read();  // read as ASCII encoding
    //Serial.println(data);        // send data as string to rpi
}
