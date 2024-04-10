import pygame
import time
from uniform_cost_search import uniform_cost_search, get_neighbors, is_valid_move, reconstruct_path

def load_world(file_path):
    world_data = []
    mandalorian_position = None
    goal_position = None
    with open(file_path, "r") as file:
        for y, line in enumerate(file):
            row = []
            for x, num in enumerate(line.strip().split()):
                num = int(num)
                if num == 2:
                    mandalorian_position = (y, x)
                elif num == 5:
                    goal_position = (y, x)
                row.append(num)
            world_data.append(row)
    return world_data, mandalorian_position, goal_position

class WorldRenderer:
    def __init__(self, world_data):
        self.world_data = world_data
        self.tile_size = 50
        self.screen_width = 10 * self.tile_size
        self.screen_height = 10 * self.tile_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.load_assets()

    def load_assets(self):
        self.tile_images = {
            0: pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA),  # Suelo (blanco)
            1: pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA),  # Muro (gris)
            2: pygame.transform.scale(pygame.image.load("assets/mandalorian.png"), (self.tile_size, self.tile_size)),
            3: pygame.transform.scale(pygame.image.load("assets/ship.png"), (self.tile_size, self.tile_size)),
            4: pygame.transform.scale(pygame.image.load("assets/enemy.png"), (self.tile_size, self.tile_size)),
            5: pygame.transform.scale(pygame.image.load("assets/grogu.png"), (self.tile_size, self.tile_size))
        }
        self.tile_images[0].fill((255, 255, 255))  # Llenar el suelo de blanco
        self.tile_images[1].fill((128, 128, 128))  # Llenar el muro de gris

    def render(self, mandalorian_position):
        for y in range(10):
            for x in range(10):
                self.screen.blit(self.tile_images[self.world_data[y][x]], (x * self.tile_size, y * self.tile_size))
        self.screen.blit(self.tile_images[2], (mandalorian_position[1] * self.tile_size, mandalorian_position[0] * self.tile_size))
        pygame.display.flip()

def print_search_results(algorithm_name, path, cost, nodes_expanded, max_depth, computation_time):
    print(f"{algorithm_name}:")
    print(f"Tiempo de cómputo: {computation_time:.2f} segundos")
    print(f"Nodos expandidos: {nodes_expanded}")
    print(f"Profundidad máxima: {max_depth}")
    if algorithm_name == "Búsqueda de costo uniforme":
        print(f"Costo de la ruta: {cost}")
    print(f"Ruta encontrada: {path}")
    print()

def main():
    # Cargar los datos del mundo desde un archivo de texto
    world_data, mandalorian_position, goal_position = load_world("Prueba1.txt")

    # Inicializar Pygame
    pygame.init()
    pygame.display.set_caption("Smart Mandalorian")

    # Crear el renderizador del mundo
    world_renderer = WorldRenderer(world_data)

    # Ejecutar el algoritmo de búsqueda de costo uniforme
    start_time = time.perf_counter()
    path, cost, nodes_expanded, max_depth, computation_time = uniform_cost_search(world_data)
    print_search_results("Búsqueda de costo uniforme", path, cost, nodes_expanded, max_depth, computation_time)
    end_time = time.perf_counter()
    total_computation_time = end_time - start_time
    print(f"Tiempo total de cómputo: {total_computation_time:.2f} segundos")

    # Simulación del movimiento del Mandalorian
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la posición anterior del Mandalorian
        world_data[mandalorian_position[0]][mandalorian_position[1]] = 0

        # Mover al Mandalorian a la siguiente posición en la ruta
        if len(path) > 1:
            mandalorian_position = path[1]
            path = path[1:]  # Eliminar la posición actual de la ruta
            world_data[mandalorian_position[0]][mandalorian_position[1]] = 2  # Actualizar la posición del Mandalorian en el mundo

        world_renderer.render(mandalorian_position)

        # Agregar una pausa para ralentizar el movimiento
        pygame.time.delay(200)  # Pausa de 200 milisegundos (0.2 segundos)

    pygame.quit()

if __name__ == "__main__":
    main()