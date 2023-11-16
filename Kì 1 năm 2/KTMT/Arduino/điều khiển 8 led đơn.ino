void setup() {
  for(int i=2;i<=9;i++){
    pinMode(i,OUTPUT);  
  }
}

void loop() {
  // 1.led chop tat
  int i,j;
  for(i=2;i<=9;i++){
    digitalWrite(i,HIGH);
  }
  delay(500);
  for(i=2;i<=9;i++){
      digitalWrite(i,LOW);
  }
  delay(500);
  // 2.bat lan luot, tat lan luot
  for(i=2;i<=9;i++){
    digitalWrite(i,HIGH);
    delay(500);  
  }
  for(i=2;i<=9;i++){
    digitalWrite(i,LOW);
    delay(500);  
  }
  // 3.bat roi tat lan luot
  for(i=2;i<=9;i++){
    digitalWrite(i,HIGH);
    delay(500);
    digitalWrite(i,LOW);
    delay(500);  
  }
 // 4.bat va tat led doi xung
 //(18,27,36,45)
  for(i=0;i<=4;i++){
      digitalWrite(i+2,HIGH);
      digitalWrite(9-i,HIGH);
      delay(500);
  }
  for(i=0;i<=4;i++){
    digitalWrite(i+2,LOW);
    digitalWrite(9-i,LOW);
    delay(500);
  }
  //(45,36,27,18)
  for(i=4;i>=0;i--){
    digitalWrite(i+2,HIGH);
    digitalWrite(9-i,HIGH);
    delay(500);  
  }
  for(i=4;i>=0;i--){
    digitalWrite(i+2,LOW);
    digitalWrite(9-i,LOW);
    delay(500);  
  }
  // 5.led sang don 1->8
  for(i=2;i<=9;i++){
    for(j=2;j<=11-(i+1);j++){
      digitalWrite(j,HIGH);
      delay(500);
      digitalWrite(j,LOW);
      delay(500);
    }
    digitalWrite(11-i,HIGH);
  }
}
