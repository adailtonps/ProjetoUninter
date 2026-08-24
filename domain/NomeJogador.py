import pygame


class NomeJogador:
    def __init__(self, window):
        self.window = window
        self.nome = ""
        self.fundo = pygame.image.load("asset/menu.png")#corrigir

    def run(self):
        fonte = pygame.font.SysFont("Arial", 30, bold=True)

        while True:
            self.window.fill((255, 255, 255))
            self.window.blit(self.fundo, (0, 0))

            titulo = fonte.render("DIGITE O SEU NOME:", True, (255,255,255))

            nome = fonte.render(self.nome.upper(), True, (255,255,255))

            self.window.blit(titulo, (240,240))
            self.window.blit(nome, (240,290))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.nome.strip():
                            return self.nome.upper()
                    elif event.key == pygame.K_BACKSPACE:
                        self.nome = self.nome[:-1]

                    else:
                        self.nome += event.unicode