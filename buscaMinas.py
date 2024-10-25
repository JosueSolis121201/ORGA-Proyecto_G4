import random
from respuesta  import respuesta_Bluetooth, aciertoCorrecto,gameOver,victoria,jugando, puntajeJugador

# Clase para el tablero del juego
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

    def read_archivo(self,archivo):
        
        for i in archivo:
            self.tablero[i[0]][i[1]] = "M"

    def read_inputs(self,inputs):
        for i in inputs:
            self.tablero[i[0]][i[1]] = "M"

    def generar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] != "M":
                self.tablero[fila][columna] = "M"
                minas_colocadas += 1

    

    def contar_adyacentes(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] == "M":
                    continue
                self.tablero[i][j] = self.contar_minas_adyacentes(i, j)

    def contar_minas_adyacentes(self, fila, columna):
        contador = 0
        for i in range(max(0, fila - 1), min(self.filas, fila + 2)):
            for j in range(max(0, columna - 1), min(self.columnas, columna + 2)):
                if self.tablero[i][j] == "M":
                    contador += 1
        return contador

    def imprimir_tablero(self, mostrar_minas=False):
        print("\nTablero:")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.revelado[i][j]:
                    print(self.tablero[i][j], end=" ")
                elif mostrar_minas and self.tablero[i][j] == "M":
                    print("M", end=" ")
                elif self.marcas[i][j]:
                    print("P", end=" ")  # Marcado como posible mina
                else:
                    print("X", end=" ")
            print()

    def revelar_casilla(self, fila, columna):
        if self.tablero[fila][columna] == "M":
            return False
        self.revelar_recursivamente(fila, columna)
        return True

    def revelar_recursivamente(self, fila, columna):
        if self.revelado[fila][columna] or self.tablero[fila][columna] == "M":
            return
        self.revelado[fila][columna] = True


    def todas_reveladas(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j] != "M" and not self.revelado[i][j]:
                    return False
        return True

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
