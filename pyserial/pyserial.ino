#include <Stepper.h>
#include <Timing.h>

#define STEPS 2050

Stepper stepper(STEPS, 8, 10, 9, 11);

char var;
String cod = "";
String cod2 = "";
String C1 = "";
String Flag = "";
String Tempo = "";

Timing a;
Timing b;
Timing c;
Timing d;
Timing e;
Timing f;
Timing g;
Timing h;
Timing w;
Timing z;
Timing k;
Timing m;

int v[11];
int t[11];

int centesimos = 0;
int segundos = 0;
int minutos = 0;



void ini_vet(int x[11]){
   int j;
   for(j=0;j<11;j++){
      x[j] = -1; 
   }   

}

void setup() {

  Serial.begin(9600);
  ini_vet(v);
  ini_vet(t);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  stepper.setSpeed(4);

}


int i = 0;
int j = 0;
bool cont = false;
bool cont1 = false;
bool cont2 = false;
bool cont3 = false;
bool cont4 = false;
bool cont5 = false;
bool cont6 = false;
bool cont7 = false;
bool cont8 = false;
bool cont9 = false;
bool cont10 = false;

int ak;
int ai;

void loop() {
 
  while(Serial.available()){
    delay(10);
    char aux = Serial.read();
    cod += aux;   
  }

  //Trata os dados recebidos
  if(cod != ""){  
    while(cod[i] != 'l'){
        Tempo += char(cod[i]);
        i++;
    }
    Flag += char(cod[i+1]);
    Flag += char(cod[i+2]); 
    Flag += char(cod[i+3]);
    Flag += char(cod[i+4]);
    Flag += char(cod[i+5]);
    i = 0; 
  }
 
  if(Flag == "34601"){
    
    v[0] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }
  
  if(Flag == "82702"){

    v[1] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "18603"){
    
    v[2] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "19804"){
    
    v[3] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "82705"){
    
    v[4] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "92806"){
    
    v[5] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "34407"){
    
    v[6] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "92808"){
    
    v[7] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "93709"){
    
    v[8] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "23210"){
    
    v[9] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "98411"){
    
    v[10] = atoi( Tempo.c_str());
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "10412"){
    
    v[0] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "12213"){
    
    v[1] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "76314"){
    
    v[2] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "53615"){
    
    v[3] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "76616"){
    
    v[4] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "36517"){
    
    v[5] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "22418"){
    
    v[6] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "37919"){
    
    v[7] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "12320"){
    
    v[8] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "93521"){
    
    v[9] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "23322"){
    
    v[10] = -1;
    cod = "";
    Flag = "";
    Tempo = "";
  }

  if(Flag == "10623"){
    //sao as variaveis que controlam a rotação do histotecno
    bool conta = true;
    //
    while(1){
      if(cont == false){
          //delay de descida do elevador
         if(conta == true){  
            stepper.step(STEPS*2);
            conta = false;
            a.begin(0);
            b.begin(0);
            c.begin(0);
            d.begin(0);
            e.begin(0);
            f.begin(0);
            g.begin(0);
            h.begin(0);
            w.begin(0);
            z.begin(0);
            k.begin(0);
            m.begin(0);
         }
          //controle de oscilações
          
          if(m.onTimeout(7000)){
            //for(ak=0; ak<=3;ak++){
               stepper.step(STEPS/4);
               delay(2000);
           // }
            //for(ai=0; ai<=3;ai++){
               stepper.step(-STEPS/4);
               delay(2000);
            //}
          }
          if(a.onTimeout(v[0]*60000)){
             //delay de subida do elevador
             stepper.step(STEPS*2);
             //ativação da rotação do histotecno
             stepper.step(-STEPS/12);
             cont = true;
             cont1 = true;
          }
      }
      /*
      if(cont1 == true){
        if(b.onTimeout(v[0]*60000 + v[1]*60000)){
           digitalWrite(3, HIGH);
           delay(3000);
           digitalWrite(3, LOW);
           cont1 = false;
           cont2 = true;
        }
      }
      if(cont2 == true){
        if(c.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000)){
           digitalWrite(4, HIGH);
           delay(3000);
           digitalWrite(4, LOW);
           cont2 = false;
           cont3 = true;
        }
      }
      if(cont3 == true){
        if(d.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000)){
           digitalWrite(5, HIGH);
           delay(3000);
           digitalWrite(5, LOW);
           cont3 = false;
           cont4 = true;
        }
      }
      if(cont4 == true){
        if(e.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000)){
           digitalWrite(6, HIGH);
           delay(3000);
           digitalWrite(6, LOW);
           cont4 = false;
           cont5 = true;
        }
      }
      if(cont5 == true){
        if(f.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000 + v[5]*60000)){
           digitalWrite(7, HIGH);
           delay(3000);
           digitalWrite(7, LOW);
           cont5 = false;
           cont6 = true;
        }
      }
      if(cont6 == true){
        if(g.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000 + v[5]*60000 + v[6]*60000)){
           digitalWrite(8, HIGH);
           delay(3000);
           digitalWrite(8, LOW);
           cont6 = false;
           cont7 = true;
        }
      }
      if(cont7 == true){
        if(h.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000 + v[5]*60000 + v[6]*60000 + v[7]*60000)){
           digitalWrite(9, HIGH);
           delay(3000);
           digitalWrite(9, LOW);
           cont7 = false;
           cont8 = true;
        }
      }
      if(cont8 == true){
        if(w.onTimeout( v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000 + v[5]*60000 + v[6]*60000 + v[7]*60000 + v[8]*60000)){
           digitalWrite(10, HIGH);
           delay(3000);
           digitalWrite(10, LOW);
           cont8 = false;
           cont9 = true;
        }
      }
      if(cont9 == true){
        if(z.onTimeout( v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000 + v[5]*60000 + v[6]*60000 + v[7]*60000 + v[8]*60000 + v[9]*60000)){
           digitalWrite(11, HIGH);
           delay(3000);
           digitalWrite(11, LOW);
           cont9 = false;
           cont10 = true;
        }
      }
      if(cont10 == true){
        if(k.onTimeout(v[0]*60000 + v[1]*60000 + v[2]*60000 + v[3]*60000 + v[4]*60000 + v[5]*60000 + v[6]*60000 + v[7]*60000 + v[8]*60000 + v[9]*60000 + v[10]*60000)){
           digitalWrite(12, HIGH);
           delay(3000);
           digitalWrite(12, LOW);
           cont10 = false;
        }
      }
    }
    cod = "";
    Flag = "";
    Tempo = "";

    
    */ 
  }
  /*
  if(v[0] == 10){

    digitalWrite(2, HIGH);
    delay(50);
    digitalWrite(2, LOW);
  }

  if(v[1] == 20){

    digitalWrite(3, HIGH);
    delay(50);
    digitalWrite(3, LOW);
  }

  if(v[2] == 30){

    digitalWrite(4, HIGH);
    delay(50);
    digitalWrite(4, LOW);
  }
  
  if(v[3] == 40){

    digitalWrite(5, HIGH);
    delay(50);
    digitalWrite(5, LOW);
  }

  if(v[4] == 50){

    digitalWrite(6, HIGH);
    delay(50);
    digitalWrite(6, LOW);
  }

  if(v[5] == 60){

    digitalWrite(7, HIGH);
    delay(50);
    digitalWrite(7, LOW);
  }

  if(v[6] == 70){

    digitalWrite(8, HIGH);
    delay(50);
    digitalWrite(8, LOW);
  }

  if(v[7] == 80){

    digitalWrite(9, HIGH);
    delay(50);
    digitalWrite(9, LOW);
  }

  if(v[8] == 90){

    digitalWrite(10, HIGH);
    delay(50);
    digitalWrite(10, LOW);
  }

  if(v[9] == 100){

    digitalWrite(11, HIGH);
    delay(50);
    digitalWrite(11, LOW);
  }

  if(v[10] == 110){

    digitalWrite(12, HIGH);
    delay(50);
    digitalWrite(12, LOW);
  }
  */
  /*
  //Condição responsavel por guardar os tempos dos copos em um vetor
  if(cod != "" && cod != "1060669" && cod != "1007778" && cod != "1003401" 
  && cod != "1235202" && cod != "7612303" && cod != "5345604" && cod != "7644605" && cod != "3634506" 
  && cod != "2273407" && cod != "3745908" && cod != "1247309" && cod != "9340510" && cod != "2342311"
  && cod != "3457612" && cod != "8234713" && cod != "1823614" && cod != "1984815" && cod != "8234716" 
  && cod != "9234817" && cod != "3463418" && cod != "9234819" && cod != "9345720" && cod != "2389421"
  && cod != "9823422"){
    
    C1 = cod;
    v[i] = atoi( C1.c_str());
    i++;
    cod = "";
    C1 = "";
  }
  
  //Clean dos Copos
  if(cod == "1003401" || cod == "1235202" || cod == "7612303" || cod == "5345604" 
  || cod == "7644605" || cod == "3634506" || cod == "2273407" || cod == "3745908" 
  || cod == "1247309" || cod == "9340510" || cod == "2342311"){
    
    v[i-1] = -1;
    i--;
  }
  */
  //Se o usuario entrar com os valores fora de ordem
  /*
  if(cod == "3457612"){

    t[0] = v[i-1];
    cod = "";
  }

  if(cod == "8234713"){

    t[1] = v[i-1];
    cod = "";
  }

  if(cod == "1823614"){

    t[2] = v[i-1];
    cod = "";
  }

  if(cod == "1984815"){

    t[3] = v[i-1];
    cod = "";
  }

  if(cod == "8234716"){

    t[4] = v[i-1];
    cod = "";
  }

  if(cod == "9234817"){

    t[5] = v[i-1];
    cod = "";
  }

  if(cod == "3463418"){

    t[6] = v[i-1];
    cod = "";
  }

  if(cod == "9234819"){

    t[7] = v[i-1];
    cod = "";
  }

  if(cod == "9345720"){

    t[8] = v[i-1];
    cod = "";
  }

  if(cod == "2389421"){

    t[9] = v[i-1];
    cod = "";
  }

  if(cod == "9823422"){

    t[10] = v[i-1];
    cod = "";
  }
  
 
 if(t[0] == 10){
    digitalWrite(2, HIGH);
    delay(500);
    digitalWrite(2, LOW);
 }
 if(t[1] == 20){
    digitalWrite(3, HIGH);
    delay(500);
    digitalWrite(3, LOW);
 }
 if(t[2] == 30){
    digitalWrite(4, HIGH);
    delay(500);
    digitalWrite(4, LOW);
 }
 if(t[3] == 40){
    digitalWrite(5, HIGH);
    delay(500);
    digitalWrite(5, LOW);
 }
 if(t[4] == 50){
    digitalWrite(6, HIGH);
    delay(500);
    digitalWrite(6, LOW);
 }
 if(t[5] == 60){
    digitalWrite(7, HIGH);
    delay(500);
    digitalWrite(7, LOW);
 }
 if(t[6] == 70){
    digitalWrite(8, HIGH);
    delay(500);
    digitalWrite(8, LOW);
 }
 if(t[7] == 80){
    digitalWrite(9, HIGH);
    delay(500);
    digitalWrite(9, LOW);
 }
 if(t[8] == 90){
    digitalWrite(10, HIGH);
    delay(500);
    digitalWrite(10, LOW);
 }
 if(t[9] == 100){
    digitalWrite(11, HIGH);
    delay(500);
    digitalWrite(11, LOW);
 }
 if(t[10] == 110){
    digitalWrite(12, HIGH);
    delay(500);
    digitalWrite(12, LOW);
 }
 */
 }
}
