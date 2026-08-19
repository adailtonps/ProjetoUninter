import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from domain.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/background_sound.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(40, MENU_OPTIONS[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 480 + 50 * i))

            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

    # metodo que gera o texto escrito no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
