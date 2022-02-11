// 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'
// VERSION V1.1

void setup() {
Serial.begin(9600);      // set the baud rate
Serial.println("Ready"); // print "Ready" once
}

void loop() {
char inByte = ' ';

for(int x=0; x<10; x++){
  Serial.println(x);
  delay(300);
}

if(Serial.available()){ 
String(inByte) = Serial.readString(); 
Serial.println(inByte); // send the data back in a new line so that it is not all one long line
}

delay(1); // delay for 1/10 of a second
}
