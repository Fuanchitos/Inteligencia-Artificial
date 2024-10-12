# Inteligencia-Artificial

# Algoritmo de Búsqueda de Rutas

Este proyecto contiene un algoritmo en Python que busca las rutas de menor y mayor costo en una matriz, representando un gráfico de costos.

## Descripción del Algoritmo

El algoritmo explora una matriz bidimensional para encontrar la ruta de menor y mayor costo entre dos puntos designados (inicio y final). Utiliza un enfoque de búsqueda en anchura, asegurándose de considerar todas las posibles direcciones (arriba, abajo, izquierda, derecha) para encontrar la solución.

## Estructura de la Matriz

La matriz representa un conjunto de costos. Cada celda contiene un número que representa el costo de pasar por esa celda.

## Funcionamiento

1. Se definen las direcciones posibles para el movimiento (arriba, abajo, izquierda, derecha).
2. Se utiliza una cola para explorar las posiciones de la matriz, almacenando la ruta y el costo acumulado.
3. Al llegar a la posición final, se devuelve la ruta y el costo correspondiente.
4. Para encontrar la ruta de mayor costo, se invierten los valores de la matriz y se aplica el mismo algoritmo.

## Ejemplo de Uso

Define la matriz, el punto de inicio y el punto final:

```python
# Definir la matriz
matriz = [
    [-3, -3,  2, -3, ...],  # Fila 1
    ...
]

# Definir el punto de inicio y el punto final
inicio = (1, 2)  # C2
final = (11, 7)  # H12

