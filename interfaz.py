import pygame
from environment import Environment
from uniform_cost_search import uniform_cost_search


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

    def render(self):
        for y in range(10):
            for x in range(10):
                self.screen.blit(self.tile_images[self.world_data[y][x]], (x * self.tile_size, y * self.tile_size))
        pygame.display.flip()


if __name__ == "__main__":
    env = Environment("Prueba1.txt")
    path, _, _, _, _ = uniform_cost_search(env)

    pygame.init()
    pygame.display.set_caption("Smart Mandalorian")
    world_renderer = WorldRenderer(env.grid)
    mandalorian_position = env.start

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la posición anterior del Mandalorian
        env.grid[mandalorian_position[0]][mandalorian_position[1]] = 0

        # Mover al Mandalorian a la siguiente posición en la ruta
        if len(path) > 1:
            mandalorian_position = path[1]
            path = path[1:]  # Eliminar la posición actual de la ruta
            env.grid[mandalorian_position[0]][mandalorian_position[1]] = 2  # Actualizar la posición del Mandalorian en el mundo

        world_renderer.render()

        # Agregar una pausa para ralentizar el movimiento
        pygame.time.delay(200)  # Pausa de 200 milisegundos (0.2 segundos)

    pygame.quit()
# Función para mostrar los resultados en una ventana de Pygame
def show_results(path, cost, nodes_expanded, max_depth, computation_time):
    pygame.init()
    pygame.display.set_caption("Resultados de la búsqueda")
    screen_width = 1000
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 24)

    # Renderizar los resultados en la pantalla
    results_text = [
        
        f"Costo de la ruta: {cost}",
        f"Cantidad de nodos expandidos: {nodes_expanded}",
        f"Profundidad máxima del árbol de búsqueda: {max_depth}",
        f"Tiempo de cómputo: {computation_time} segundos"
    ]

    y_offset = 50
    for text in results_text:
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += 30

    pygame.display.flip()

    # Bucle principal de Pygame para mantener la ventana abierta
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def main():
    env = Environment("Prueba1.txt")
    path, cost, nodes_expanded, max_depth, computation_time = uniform_cost_search(env)
    
    # Mostrar los resultados en la ventana de Pygame
    show_results(path, cost, nodes_expanded, max_depth, computation_time)

if __name__ == "__main__":
    main()