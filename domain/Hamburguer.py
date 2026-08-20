import pygame


class Hamburguer:
    def __init__(self, ingredientes_pedido, window):
        self.ingredientes_pedido = ingredientes_pedido
        self.window = window
        self.surf = pygame.image.load('./asset/hamburguer.png')
        self.window.blit(self.surf, self.rect)