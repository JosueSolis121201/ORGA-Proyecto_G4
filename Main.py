import tkinter as tk
from PIL import ImageTk, Image
import serial
from buscaMinas import Buscaminas
from respuesta import cerrarPuerto, respuesta_Bluetooth ,Reiniciar
from tkinter import messagebox
from tkinter import filedialog
import re
# pip install Pillow
# pip install pyserial

#Funcion para minans con inputs
def extraer_parejas(texto):
    # Expresión regular para encontrar 'x:num, y:num'
    patron = r"x:(\d+),\s*y:(\d+)"
    # Buscar todas las coincidencias
    parejas = re.findall(patron, texto)
    # Convertir a enteros las coordenadas
    parejas = [(int(x), int(y)) for x, y in parejas]
    # Crear un conjunto para rastrear las parejas únicas
    parejas_unicas = set()
    for pareja in parejas:
        if pareja in parejas_unicas:
            messagebox.showinfo("Contenido", f"Error se ha detectado doble mina en una posicion")
            return
        else:
            parejas_unicas.add(pareja)
    
    return parejas

def obtener_contenido():
    # Obtener el contenido ingresado en el área de texto
    contenido = textoInput.get("1.0", "end-1c")  # "1.0" es la posición inicial, "end-1c" evita el salto de línea final
    messagebox.showinfo("Contenido", f"Has ingresado:\n{contenido}")
    textoInput.delete("1.0", "end")
    # Llamar a la función y mostrar el resultado
    coordenadas = extraer_parejas(contenido)
    print("Parejas de coordenadas:", coordenadas)
    return coordenadas

def iniciarJuegoInput():
    coordenadas=obtener_contenido()
    #Iniciando juego con inputs
    while True:
        juego = Buscaminas(4, 4, 6,'ReadInputs',[],coordenadas)
        juego.jugar() 
        print('Esperando respuesta del jugador para reinciar o continuar jugando')
        Reiniciar()
        if (respuesta_Bluetooth()=='reiniciar'):
            print('Se reiniciara a configuracion')
            break
        else :
            print('Se continuara con configuracion anterior')


        
    


#Funcion para minans con archivos
def abrir_archivo():
    # Abrir cuadro de diálogo para seleccionar archivo
    archivo_ruta = filedialog.askopenfilename(
        title="Abrir archivo de texto",
        filetypes=[("Archivos de texto", "*.org")]  # Filtrar solo archivos .txt
    )
    if archivo_ruta:
        try:
            with open(archivo_ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()  # Leer todo el contenido del archivo
                print(contenido)
                return contenido
                
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

def iniciarJuegoArchivo():
    archivo=abrir_archivo()
    coordenadas = extraer_parejas(archivo)
    print("Parejas de coordenadas:", coordenadas)
    #Iniciando juego con inputs
    while True:
        juego = Buscaminas(4, 4, 6,'ReadArchivo',coordenadas,[])
        juego.jugar() 
        print('Esperando respuesta del jugador para reinciar o continuar jugando')
        Reiniciar()
        if (respuesta_Bluetooth()=='reiniciar'):
            print('Se reiniciara a configuracion')
            break
        else :
            print('Se continuara con configuracion anterior')




#Funcion para minans aleatorias
def iniciarJuego():
    contenido = textoInputRandom.get("1.0", "end-1c") 
    juego = Buscaminas(4, 4, int(contenido),'aleatorio',[],[])
    #iniciando juego random
    juego.jugar() 






ventana=tk.Tk()
ventana.geometry("400x400")
ventana.resizable(0,0)
ventana.title("Busca minas")



def alternar_card():
    if card.winfo_viewable():
        card.pack_forget()  # Ocultar la tarjeta
    else:
        card.pack(pady=3)  # Mostrar la tarjeta

# Crear un marco para la tarjeta con un tamaño específico
card = tk.Frame(ventana, bg="lightblue", bd=2, relief=tk.RAISED, width=400, height=150)
card.pack_propagate(False)  # Evitar que el marco cambie de tamaño al agregar widgets

# Agregar un título a la tarjeta
titulo = tk.Label(card, text="Configuracion manual de minas", bg="lightblue", font=("Helvetica", 14))
titulo.pack(pady=10)

#texto
texto = tk.Label(ventana,text="Busca minas",font=("Arial", 20))
texto.pack(pady=10)


botonIniciar=tk.Button(text="Juego Rapido",command=iniciarJuego ,height=2,width=10)
botonIniciar.place(x=25,y=50)

botonConfig=tk.Button(text="Configurar",command=alternar_card ,height=2,width=10)
botonConfig.place(x=158,y=50)

botonCargar=tk.Button(text="Cargar archivo",command=iniciarJuegoArchivo,height=2,width=10)
botonCargar.place(x=291,y=50)


# Área de texto para mostrar el contenido del archivo
textoInput = tk.Text(card, wrap="word", width=30, height=15)
textoInput.pack(pady=4)


# Agregar un título a la tarjeta
titulo = tk.Label(ventana, text="Cantidad de minas aleatorias", font=("Helvetica", 14))
titulo.pack(pady=40)

# Área de texto para minas random
textoInputRandom = tk.Text(ventana, wrap="word", width=40, height=2)
textoInputRandom.pack(pady=5)



# Botón para mostrar el valor ingresado
boton_mostrar = tk.Button(card, text="Aceptar", command=iniciarJuegoInput, height=3)
boton_mostrar.place(x=10,y=60)


ventana.mainloop()
cerrarPuerto()