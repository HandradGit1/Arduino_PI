const char ABRIR_PORTA = 'A';
const char FECHAR_PORTA = 'B';
const int PORTA_LED = 13;
char teste =' ';

void setup()
{
  pinMode(PORTA_LED,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  
  if(Serial.available()>0){
    cobaia = Serial.read();
 
 switch(teste){
  case ABRIR_PORTA:
      digitalWrite(13,HIGH);
      Serial.print("ABERTO");
      digitalWrite(13,LOW);
      break;
  case FECHAR_PORTA:
      digitalWrite(13,HIGH);
      Serial.print("FECHADO");
      digitalWrite(13,LOW);
      break;
  };
 }
}
