int led=13;
int ledVerde =10;
int ledAzul = 7;

String valor;
char valor2;

void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial1.begin(9600);
}


void loop() {
//lectura BackEnd
  if(Serial.available()>0){
     valor2=Serial.read();
    if(valor2=='Z'){
      Serial1.println("Game Over");
      digitalWrite(led,HIGH);
      digitalWrite(ledAzul,LOW);
    }
    else if(valor2=='X'){
      Serial1.println("Acierto Correcto");
    }
    else if(valor2=='Y'){
      Serial1.println("Victoria revelaste todas las casillas");
      digitalWrite(ledVerde,HIGH);
      digitalWrite(ledAzul,LOW);
    }
    else if(valor2=='W'){
      digitalWrite(ledAzul,HIGH);
      digitalWrite(led,LOW);
      digitalWrite(ledVerde,LOW);
       Serial1.println("Iniciando juego");
    }

    else if(valor2=='R'){
       Serial1.println("Escribe reiniciar para configurar o cualquier cosa para repetir configuracion anterior");
    }
    else if(valor2=='1'){
      Serial1.println("Tu puntuacion es de: 1");
    }
    else if(valor2=='2'){
      Serial1.println("Tu puntuacion es de: 2");
    }
    else if(valor2=='3'){
      Serial1.println("Tu puntuacion es de: 3");
    }
    else if(valor2=='4'){
      Serial1.println("Tu puntuacion es de: 4");
    }
    else if(valor2=='5'){
      Serial1.println("Tu puntuacion es de: 5");
    }
    else if(valor2=='6'){
      Serial1.println("Tu puntuacion es de: 6");
    }
    else if(valor2=='7'){
      Serial1.println("Tu puntuacion es de: 7");
    }
    else if(valor2=='8'){
      Serial1.println("Tu puntuacion es de: 8");
    }
    else if(valor2=='9'){
      Serial1.println("Tu puntuacion es de: 9");
    }
    else if(valor2=='0'){
      Serial1.println("Tu puntuacion es de: 0");
    }
    else if(valor2=='a'){
      Serial1.println("Tu puntuacion es de: 10");
    }
    else if(valor2=='b'){
      Serial1.println("Tu puntuacion es de: 11");
    }
    else if(valor2=='c'){
      Serial1.println("Tu puntuacion es de: 12");
    }
    else if(valor2=='d'){
      Serial1.println("Tu puntuacion es de: 13");
    }
    else if(valor2=='e'){
      Serial1.println("Tu puntuacion es de: 14");
    }
    else if(valor2=='f'){
      Serial1.println("Tu puntuacion es de: 15");
    }
    else if(valor2=='g'){
      Serial1.println("Tu puntuacion es de: 16");
    }

  }


//lectura Bluetooth 
  if(Serial1.available()>0){
     valor=Serial1.readString();
     valor.trim();  // Elimina espacios y caracteres de nueva línea al inicio y final
    if(valor.equals("reinicio")){
      digitalWrite(led,HIGH);
      Serial1.println("Encendido");
    }
    Serial.println(valor);
  }
}
