# Matriz
matriz = [
    [-3, -3, 2, -3, -3, -2, 1, 2, 0, 2, 0, 0, 1],
    [2, 3, -1, -1, -1, 3, 0, -3, -3, 2, 2, 1, 1],
    [1, -3, -3, 2, -3, 3, 1, 3, 2, 1, -2, 2, 3],
    [0, 0, 3, 0, -3, -3, 0, 2, 2, 1, 1, 1, 1],
    [2, -1, -1, 3, 0, -3, 1, -2, 2, 0, 0, 1, 1],
    [0, 3, -1, -2, 1, 2, 1, -2, -3, 2, 0, 0, 0],
    [0, 3, 2, 0, 1, 1, 2, 3, -1, -3, 0, 0, -2],
    [3, -3, -2, 3, -1, -3, 3, 3, 0, 2, -2, -1],
    [-2, -2, 1, 0, 0, 0, 2, 0, -2, 0, 2, 1, -1],
    [-3, 3, 0, -1, -3, 2, 3, 0, -2, 3, 0, -2],
    [-3, 3, -3, -2, 0, -3, 1, 0, 1, 0, 1, -2],
    [-1, 0, 1, 0, -3, 3, 0, 3, 3, 0, -1, 0, -1],
    [1, -3, -1, 3, 0, 2, 3, 1, -2, 3, 3, 0, 3]
]

inicio = (2, 2)  
fin = (12, 12)   

#Para imprimir
for fila in matriz:
    print(fila)

print(f"Punto de inicio: {inicio}")
print(f"Punto final: {fin}")

class RutaCostos:
    def __init__(self, matriz, inicio, fin):
        self.matriz = matriz
        self.inicio = inicio
        self.fin = fin
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def buscar_rutas(self):
        pass

    def buscar_rutas(self):
        print("Matriz:")
        for fila in self.matriz:
            print(fila)
        print(f"Inicio: {self.inicio}")
        print(f"Fin: {self.fin}")

ruta_costos = RutaCostos(matriz, inicio, fin)

ruta_costos.buscar_rutas()

