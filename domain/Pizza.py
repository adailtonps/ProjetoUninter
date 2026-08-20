import pygame

class Pizza:
    def __init__(self, ingredientes_pedido, window):
        self.window = window
        self.ingredientes_pedido = ingredientes_pedido

        self.surf = pygame.image.load('./asset/pizza.png')
        self.window.blit(self.surf, self.rect)