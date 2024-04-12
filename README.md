# Mandalorian Intelligent Pathfinding

Este programa implementa diferentes algoritmos de búsqueda para encontrar la ruta óptima para que un Mandaloriano navegue a través de un terreno peligroso hasta su destino. Los algoritmos implementados incluyen búsqueda no informada (amplitud, costo uniforme, profundidad) y búsqueda informada (Ávara, A*).

## Requerimientos

- Python 3.x
- Pygame (puede instalarse a través de `pip install pygame`)

## Uso

1. Ejecuta el script `main.py`.
2. Selecciona el tipo de algoritmo de búsqueda que deseas utilizar:
   - Para algoritmos de búsqueda no informada, ingresa `1`.
   - Para algoritmos de búsqueda informada, ingresa `2`.
3. Sigue las instrucciones adicionales según el tipo de algoritmo de búsqueda seleccionado.

## Algoritmos Implementados

### Búsqueda no Informada

1. **Algoritmo de búsqueda por amplitud**: Explora todos los nodos a una profundidad dada antes de moverse hacia el siguiente nivel.
2. **Algoritmo de búsqueda por costo uniforme**: Encuentra la ruta con el menor costo total.
3. **Algoritmo de búsqueda por profundidad**: Explora tanto como sea posible a lo largo de cada rama antes de retroceder.

### Búsqueda Informada

1. **Algoritmo de búsqueda Ávara**: Selecciona el nodo que parece más prometedor según alguna heurística.
2. **Algoritmo de búsqueda A***: Considera tanto el costo pasado como una estimación del costo futuro para decidir qué nodo expandir.

## Funciones Añadidas

### A.py

Este archivo contiene la implementación del algoritmo A* para búsqueda informada. Además, contiene funciones auxiliares como `manhattan_distance`, `is_valid_move`, y `get_move_cost`. El algoritmo A* utiliza una heurística para guiar la búsqueda hacia la solución óptima.

### Amplitud.py

Este archivo implementa el algoritmo de búsqueda por amplitud. Este algoritmo expande todos los nodos a una profundidad dada antes de moverse hacia el siguiente nivel, garantizando encontrar la solución óptima en un espacio de búsqueda finito.

### Avara.py

Este archivo contiene la implementación del algoritmo de búsqueda Ávara. Este algoritmo selecciona el nodo que parece más prometedor según alguna heurística, pero no garantiza encontrar la solución óptima.

### Costo_Uniforme.py

Este archivo implementa el algoritmo de búsqueda por costo uniforme. Este algoritmo encuentra la ruta con el menor costo total, expandiendo los nodos en función del costo acumulado desde el nodo inicial.

### Profundidad.py

Este archivo implementa el algoritmo de búsqueda por profundidad. Este algoritmo explora tanto como sea posible a lo largo de cada rama antes de retroceder, lo que puede llevar a una búsqueda no óptima en algunos casos.

## Contribuyentes

- Ervin CaravalI Ibarra
- Hernan David Cisneros Vargas
- Miguel Angel Moreno Romero
- Kevin Alejandro Velez Agudelo

## Notas Adicionales

- La interfaz gráfica del programa se minimizará automáticamente después de mostrar la solución.
- El archivo de texto `Prueba1.txt` y tambien el `Prueba2.txt` contiene los datos del mundo que el    programa utilizará para encontrar la ruta.
- Este programa está diseñado para ser utilizado por un Mandaloriano que necesita encontrar una ruta segura a través de un terreno peligroso para llegar a su destino.
