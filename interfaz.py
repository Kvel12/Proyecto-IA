import pygame

class WorldRenderer:
    def __init__(self, world_data):
        self.world_data = world_data
        self.tile_size = 50
        self.screen_width = 10 * self.tile_size
        self.screen_height = 10 * self.tile_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.load_assets()
        self.mandalorian_image = pygame.transform.scale(pygame.image.load("assets/mandalorian.png"), (self.tile_size, self.tile_size))
        self.mandalorian_position = None
        self.path = []
        self.path_index = 0

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

    def set_mandalorian_position(self, position):
        self.mandalorian_position = position

    def set_path(self, path):
        self.path = path
        self.path_index = 0

    def update(self):
        # Limpiar la posición anterior del Mandalorian
        if self.mandalorian_position is not None:
            self.world_data[self.mandalorian_position[0]][self.mandalorian_position[1]] = 0

        # Mover al Mandalorian a la siguiente posición en la ruta
        if self.path and self.path_index < len(self.path):
            self.mandalorian_position = self.path[self.path_index]
            self.world_data[self.mandalorian_position[0]][self.mandalorian_position[1]] = 2
            self.path_index += 1

    def render(self):
        for y in range(10):
            for x in range(10):
                self.screen.blit(self.tile_images[self.world_data[y][x]], (x * self.tile_size, y * self.tile_size))

        # Dibujar el camino en verde, excepto la última posición
        for i, pos in enumerate(self.path):
            if i < len(self.path) - 1:
                pygame.draw.rect(self.screen, (0, 255, 0), (pos[1] * self.tile_size, pos[0] * self.tile_size, self.tile_size, self.tile_size))

        if self.mandalorian_position is not None:
            self.screen.blit(self.tile_images[2], (self.mandalorian_position[1] * self.tile_size, self.mandalorian_position[0] * self.tile_size))

        pygame.display.flip()