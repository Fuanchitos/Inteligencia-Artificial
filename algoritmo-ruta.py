def encontrar_ruta(matriz, inicio, final, buscar_mayor=False):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Direcciones posibles: (arriba, abajo, izquierda, derecha)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Inicializar estructuras
    cola = [(inicio, [inicio], 0)]  # (posicion, ruta, costo)
    visitados = set()

    while cola:
        (posicion_actual, ruta_actual, costo_actual) = cola.pop(0)
        
        # Verificar si hemos llegado al destino
        if posicion_actual == final:
            return ruta_actual, costo_actual
        
        visitados.add(posicion_actual)

        # Explorar vecinos
        for direccion in direcciones:
            nuevo_x = posicion_actual[0] + direccion[0]
            nuevo_y = posicion_actual[1] + direccion[1]
            vecino = (nuevo_x, nuevo_y)

            if (0 <= nuevo_x < filas and 0 <= nuevo_y < columnas and 
                vecino not in visitados):
                nuevo_costo = costo_actual + matriz[nuevo_x][nuevo_y]
                cola.append((vecino, ruta_actual + [vecino], nuevo_costo))

    return None, float('inf')  # Si no se encuentra ruta

# Definir la matriz
matriz = [
    [-3, -3,  2, -3,  3, -2, -2,  1,  2,  0,  2,  0,  1],  # Fila 1
    [ 2,  3, -1, -1, -1,  3,  2,  0, -3, -3,  2,  1,  1],  # Fila 2
    [ 1, -3, -3,  2,  3,  1,  3,  3,  2,  1, -2, -2,  3],  # Fila 3
    [ 0,  0,  3,  0,  3, -3, -2, -3,  0,  2,  2,  1,  1],  # Fila 4
    [ 2, -1, -1, -3,  3,  3,  0, -3,  1, -2,  2,  0,  1],  # Fila 5
    [ 0,  3, -1,  1, -1, -2,  2, -2,  2, -1, -2, -3,  0],  # Fila 6
    [ 0,  3,  2,  0,  1,  1,  2,  3, -1, -3,  0,  0, -2],  # Fila 7
    [ 3,  3, -3, -2,  3, -3, -1, -3,  3, -2,  2, -2, -1],  # Fila 8
    [-2, -2,  1,  0,  0,  0,  2,  0, -2,  0,  2,  1, -1],  # Fila 9
    [-3,  3,  0, -1, -3,  1,  2, -3,  2, -3,  0,  2, -2],  # Fila 10
    [-3, -3, -3,  3, -2,  0, -2, -3,  1,  0,  1, -1, -2],  # Fila 11
    [-1,  0,  1,  2,  1,  0,  0,  3, -3,  3,  3, -2, -1],  # Fila 12
    [ 1, -3,  1,  0,  0,  2,  3,  1, -2,  3,  3,  0,  3],  # Fila 13
]

# Definir el punto de inicio y el punto final
inicio = (1, 2)  # C2
final = (11, 7)  # H12

# Encontrar la ruta mínima
ruta_minima, costo_minimo = encontrar_ruta(matriz, inicio, final)

# Ahora, para la ruta de mayor costo, invertir los valores de la matriz
matriz_invertida = [[-valor for valor in fila] for fila in matriz]
ruta_maxima, costo_maximo = encontrar_ruta(matriz_invertida, inicio, final)
costo_maximo = -costo_maximo  # Revertir el costo para mostrar el original

# Mostrar resultados
print("Ruta mínima encontrada:", ruta_minima)
print("Costo mínimo total:", costo_minimo)
print("Ruta máxima encontrada:", ruta_maxima)
print("Costo máximo total:", costo_maximo)
