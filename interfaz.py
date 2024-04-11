import pygame

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

    def render(self, path=None):
        for y in range(10):
            for x in range(10):
                self.screen.blit(self.tile_images[self.world_data[y][x]], (x * self.tile_size, y * self.tile_size))

        if path:
            for i in range(len(path)):
                x, y = path[i]
                if self.world_data[y][x] == 0:
                    pygame.draw.rect(self.screen, (0, 255, 0), (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

        pygame.display.flip()