import pygame
from interfaz import WorldRenderer
from Amplitud import busqueda_amplitud
from Costo_Uniforme import costo_uniforme,g
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

def show_algorithm_options():
    print("=" * 50)
    print("Selecciona el tipo de algoritmo de búsqueda:")
    print("1. Algoritmos de búsqueda no Informada")
    print("2. Algoritmos de búsqueda Informada")
    choice = int(input("Ingresa el número de opción (1 o 2): "))
    print("=" * 50)
    return choice

def execute_uninformed_search():
    print("=" * 50)
    print("Selecciona el algoritmo de búsqueda no Informada:")
    print("1. Algoritmo de búsqueda por amplitud")
    print("2. Algoritmo de búsqueda por costo uniforme")
    print("3. Algoritmo de búsqueda por profundidad")
    choice = int(input("Ingresa el número de opción (1, 2 o 3): "))
    print("=" * 50)

    # Crear el renderizador del mundo
    world_renderer = WorldRenderer(world_data)

    if choice == 1:
        path, nodes_expanded, depth, computation_time, nombre = busqueda_amplitud(world_data)
    elif choice == 2:
        path, cost, nodes_expanded, depth, computation_time, nombre = costo_uniforme(world_data);cost = cost=g(path, world_data)
    elif choice == 3:
        path, nodes_expanded, depth, computation_time, nombre = profundidad_evitando_ciclos(world_data)
    else:
        print("Opción inválida.")
        return

    if path:
        
        print("=" * 50)

        # Invertir el orden de las coordenadas en la ruta
        if nombre == "Búsqueda por Profundidad":
            path = [(y, x) for x, y in path]

        print(f"Ruta encontrada: {path}")
        if 'cost' in locals():
            print(f"Costo: {cost}")
        print(f"Nodos expandidos: {nodes_expanded}")
        print(f"Profundidad del árbol: {depth}")
        print(f"Tiempo de cómputo: {computation_time:.8f} segundos")
        print("\n¡¡¡Advertencia la interfaz del programa se ha minimizado!!!")
        print("=" * 50)

        # Crear el renderizador del mundo
        world_renderer = WorldRenderer(world_data)
        world_renderer.set_mandalorian_position(path[0])
        world_renderer.set_path(path)

        # Inicializar Pygame
        pygame.init()
        pygame.display.set_caption("Smart Mandalorian -> " + nombre)
        run_interface(world_renderer)

    else:
        print("=" * 50)
        print("No se encontró solución.")
        print("=" * 50)

def execute_informed_search():
    print("=" * 50)
    print("Selecciona el algoritmo de búsqueda Informada:")
    print("1. Algoritmo de búsqueda Avara")
    print("2. Algoritmo de búsqueda A*")
    choice = int(input("Ingresa el número de opción (1 o 2): "))
    print("=" * 50)

    if choice == 1:
        path, nodes_expanded, depth, computation_time, nombre = avara(world_data)
    elif choice == 2:
        path, cost, nodes_expanded, depth, computation_time, nombre = a_star(world_data)
    else:
        print("Opción inválida.")
        return

    if path:
        print("=" * 50)
        print(f"Ruta encontrada: {path}")
        if 'cost' in locals():
            print(f"Costo: {cost}")
        print(f"Nodos expandidos: {nodes_expanded}")
        print(f"Profundidad del árbol: {depth}")
        print(f"Tiempo de cómputo: {computation_time:.8f} segundos")
        print("\n¡¡¡Advertencia la interfaz del programa se ha minimizado!!!")
        print("=" * 50)


        # Crear el renderizador del mundo
        world_renderer = WorldRenderer(world_data)
        world_renderer.set_mandalorian_position(path[0])
        world_renderer.set_path(path)

        # Inicializar Pygame
        pygame.init()
        pygame.display.set_caption("Smart Mandalorian -> " + nombre)
        run_interface(world_renderer)

    else:
        print("=" * 50)
        print("No se encontró solución.")
        print("=" * 50)

def run_interface(world_renderer):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        world_renderer.update()
        world_renderer.render()
        pygame.time.delay(200)  # Esperar 0.2 segundos entre cada cuadro
    pygame.quit()

if __name__ == "__main__":
    choice = show_algorithm_options()
    if choice == 1:
        execute_uninformed_search()
    elif choice == 2:
        execute_informed_search()
    else:
        print("Opción inválida.")