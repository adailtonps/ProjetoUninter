import pygame

from domain import PedidoAleatorio
from domain.Menu import Menu
from domain.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                pedido_aleatorio = PedidoAleatorio()
            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
            else:
                pass
