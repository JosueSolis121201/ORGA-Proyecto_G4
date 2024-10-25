class Tablero:
    def __init__(self, filas, columnas, minas, tipoGen,archivo,inputs):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.revelado = [[False for _ in range(columnas)] for _ in range(filas)]
        self.marcas = [[False for _ in range(columnas)] for _ in range(filas)]
        self.tipo_generacion_minas(tipoGen,archivo,inputs)
        self.contar_adyacentes()

    def tipo_generacion_minas(self,tipoGen,archivo=[],inputs=[]):
        if tipoGen=='aleatorio':
            self.generar_minas()
        elif tipoGen=='ReadArchivo':
            self.read_archivo(archivo)
        elif tipoGen=='ReadInputs':
            self.read_inputs(inputs)

#################################################################################################
            # Clase para el juego
class Buscaminas:
    def __init__(self, filas=9, columnas=9, minas=10, tipoGen='',archivo=[],inputs=[]):
        self.tablero = Tablero(filas, columnas, minas, tipoGen,archivo,inputs)
        self.juego_terminado = False

        self.puntaje =0

    def jugar(self):
        jugando()# El juego se esta corriendo
        while not self.juego_terminado:
            self.tablero.imprimir_tablero()
            print("Revelar una casilla")
            accion = 1
            print(f"Introduce la fila (0 a {self.tablero.filas - 1}): ")
            fila = int(respuesta_Bluetooth())
            print(f"Introduce la columna (0 a {self.tablero.columnas - 1}): ")
            columna = int(respuesta_Bluetooth())
            if accion == 1:
                if not self.tablero.revelar_casilla(fila, columna):
                    self.tablero.imprimir_tablero(mostrar_minas=True)
                    print("¡Has perdido! Había una mina.")
                    gameOver()#Enviar que perdio al jugador
                    puntajeJugador(self.puntaje)
                    self.juego_terminado = True
                else :
                    self.puntaje=self.puntaje+1
                    aciertoCorrecto()#acerto que perdio al jugador + 1 punto
            if self.tablero.todas_reveladas():
                self.tablero.imprimir_tablero(mostrar_minas=True)
                print("¡Felicidades! Has revelado todas las casillas sin minas.")
                self.juego_terminado = True
                victoria()
                self.puntaje = 16
                puntajeJugador(self.puntaje)
            

# Iniciar el juego
if __name__ == "__main__":
    juego = Buscaminas(1, 1, 0)
    juego.jugar()