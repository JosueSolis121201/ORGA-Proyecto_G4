import serial

arduino=serial.Serial('COM3',9600,timeout=1)

def respuesta_Bluetooth():
    try:
        while True:
            if arduino.in_waiting > 0:  # Verificar si hay datos disponibles
                respuesta = arduino.readline().decode('utf-8').strip()  # Leer la respuesta
                print(f"Respuesta recibida: {respuesta}")
                return  respuesta # Terminar el bucle una vez que se recibe el primer byte
    except KeyboardInterrupt:
        print("Conexión terminada por el usuario.")


#Respuestas para el juego
def gameOver():
    arduino.write(b'Z')
def aciertoCorrecto():
    arduino.write(b'X') 
def victoria():
    arduino.write(b'Y')
def jugando():
    arduino.write(b'W')  

def Reiniciar():
    arduino.write(b'R')  

#Respuestas para Puntaje del jugaodr

def puntajeJugador(puntaje):
    if(puntaje==1):
        arduino.write(b'1')
    elif(puntaje==2):
        arduino.write(b'2')
    elif(puntaje==3):
        arduino.write(b'3')
    elif(puntaje==4):
        arduino.write(b'4')
    elif(puntaje==5):
        arduino.write(b'5')
    elif(puntaje==6):
        arduino.write(b'6')
    elif(puntaje==7):
        arduino.write(b'7')
    elif(puntaje==8):
        arduino.write(b'8')
    elif(puntaje==9):
        arduino.write(b'9')
    elif(puntaje==0):
        arduino.write(b'0')
    elif(puntaje==10):
        arduino.write(b'a')
    elif(puntaje==11):
        arduino.write(b'b')
    elif(puntaje==12):
        arduino.write(b'c')
    elif(puntaje==13):
        arduino.write(b'd')
    elif(puntaje==14):
        arduino.write(b'e')
    elif(puntaje==15):
        arduino.write(b'f')
    elif(puntaje==16):
        arduino.write(b'g')

    
    
    

  



def cerrarPuerto():
    arduino.close()
    

