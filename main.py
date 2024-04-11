import pygame
from interfaz import WorldRenderer
from Amplitud import busqueda_amplitud
from Costo_Uniforme import costo_uniforme
from Profundidad import profundidad_evitando_ciclos
from Avara import avara
from A import a_star
import time

# Cargar los datos del mundo desde un archivo de texto
world_data = []
with open("Prueba1.txt", "r") as file:
    for line in file:
        row = [int(x) for x in line.strip().split()]
        world_data.append(row)

# Inicializar Pygame
pygame.init()
pygame.display.set_caption("Smart Mandalorian")

# Crear el renderizador del mundo
world_renderer = WorldRenderer(world_data)

# Ejecutar el algoritmo de búsqueda voraz
start_time = time.perf_counter()
#path, nodes_expanded, depth, computation_time = busqueda_amplitud(world_data)
#path, cost, nodes_expanded, depth, computation_time = costo_uniforme(world_data)
#path, nodes_expanded, depth, computation_time = profundidad_evitando_ciclos(world_data)
#path, nodes_expanded, depth, computation_time = avara(world_data)
path, cost, nodes_expanded, depth, computation_time = a_star(world_data)

end_time = time.perf_counter()

if path:
    
    print(f"Ruta encontrada: {path}")
    print(f"Costo: {cost}")
    print(f"Nodos expandidos: {nodes_expanded}")
    print(f"Profundidad del árbol: {depth}")
    print(f"Tiempo de cómputo: {computation_time:.2f} segundos")


    if path[0][0] != 0:
        path = [(x, y) for y, x in path]

    # Renderizar la ruta
    world_renderer.render(path)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.delay(100)  # Esperar 0.1 segundos entre cada cuadro
else:
    print("No se encontró solución.")

pygame.quit()