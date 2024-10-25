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