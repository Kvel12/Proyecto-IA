import pygame
from interfaz import WorldRenderer
from Avara import avara
import time

# Cargar los datos del mundo desde un archivo de texto
world_data = []
with open("Prueba2.txt", "r") as file:
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
path, nodes_expanded, depth, computation_time = avara(world_data)
end_time = time.perf_counter()

if path:
    print(f"Ruta encontrada: {path}")
    print(f"Nodos expandidos: {nodes_expanded}")
    print(f"Profundidad del árbol: {depth}")
    print(f"Tiempo de cómputo: {computation_time:.2f} segundos")

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