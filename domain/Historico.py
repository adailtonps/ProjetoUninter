import pygame

from database.Banco import Banco


class Historico:
    def __init__(self, window, banco):
        self.window = window
        self.banco = banco
        self.fundo = pygame.image.load("asset/menu.png")

    def run(self):
        fonte_titulo = pygame.font.SysFont('Arial', 25, bold=True)
        fonte = pygame.font.SysFont('Arial', 20, bold=True)
        historico = self.banco.buscar_historico()
        inicio = 0
        linhas_visiveis = 15

        while True:
            self.window.blit(self.fundo, (0, 0))

            titulo = fonte_titulo.render("HISTÓRICO DE PONTUAÇÕES", True, (255, 255, 255))
            self.window.blit(titulo, (255,20))

            partida_texto = fonte.render(
                "PARTIDA",
                True,
                (255, 255, 255)
            )

            jogador_texto = fonte.render(
                "JOGADOR",
                True,
                (255, 255, 255)
            )

            pontos_texto = fonte.render(
                "PONTOS",
                True,
                (255, 255, 255)
            )
            self.window.blit(
                partida_texto,
                (50, 80)
            )

            self.window.blit(
                jogador_texto,
                (170, 80)
            )

            self.window.blit(
                pontos_texto,
                (350, 80)
            )

            partidas_visiveis = historico[inicio:inicio + linhas_visiveis]


            for i, partida in enumerate(partidas_visiveis):
                    id_partida = partida[0]
                    jogador = partida[1]
                    pontuacao = partida[2]

                    y = 120 + i * 30

                    texto_partida = fonte.render(
                        str(id_partida),
                        True,
                        (255, 255, 255)
                    )

                    texto_jogador = fonte.render(
                        jogador,
                        True,
                        (255, 255, 255)
                    )

                    texto_pontos = fonte.render(
                        str(pontuacao),
                        True,
                        (255, 255, 255)
                    )

                    self.window.blit(
                        texto_partida,
                        (70, y)
                    )

                    self.window.blit(
                        texto_jogador,
                        (170, y)
                    )

                    self.window.blit(
                        texto_pontos,
                        (370, y)
                    )
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if inicio + linhas_visiveis < len(historico):
                            inicio += 1

                    elif event.key == pygame.K_UP:
                        if inicio > 0:
                            inicio -= 1

                    if event.key == pygame.K_RETURN:
                        return


