import pygame


class Comandos:
    def __init__(self, window):
        self.window = window
        self.fundo = pygame.image.load("asset/menu.png")

    def run(self):
        fonte = pygame.font.SysFont("Arial", 17, bold=True)

        while True:
            self.window.fill((255, 255, 255))
            self.window.blit(self.fundo, (0, 0))

            texto_comando1 = fonte.render(
                "COMO JOGAR:",
                True, (255, 255, 255)
            )

            texto_comando2 = fonte.render(
                "1 - Uma cliente fará um pedido. Memorize os ingredientes e monte o prato corretamente.",
                True, (255, 255, 255)
            )


            texto_comando12 = fonte.render(
                "TODOS OS PEDIDOS POSSUEM AO MENOS 1 INGREDIENTE OBRIGATÓRIO.",
                True, (255, 255, 255)
            )
            texto_comando14 = fonte.render(
                "ESSES INGREDIENTES NÃO ENTRAM NO CÁLCULO DOS PONTOS.",
                True, (255, 255, 255))

            texto_comando13 = fonte.render(
                "VOCÊ PODE RECEBER A MENSSAGEM QUE ACERTOU 1 INGREDIENTE MAS TEVE 0 PONTOS.",
                True, (255, 255, 255)
            )
            texto_comando15 = fonte.render(
                "SÓ OS INGREDIENTES QUE VOCÊ ADICIONA QUE CONTAM.",
                True, (255, 255, 255)
            )

            texto_comando3 = fonte.render(
                "COMANDOS:",
                True, (255, 255, 255)
            )

            texto_comando4 = fonte.render(
                "ENTER - Seleciona uma opção do menu ou confirma o nome do jogador.",
                True, (255, 255, 255)
            )

            texto_comando5 = fonte.render(
                "ENTER na tela do pedido - Confirma o pedido. Memorize os ingredientes antes!",
                True, (255, 255, 255)
            )

            texto_comando6 = fonte.render(
                "MOUSE + CLIQUE - Seleciona um ingrediente.",
                True, (255, 255, 255)
            )

            texto_comando7 = fonte.render(
                "BACKSPACE - Remove o último ingrediente selecionado na cozinha.",
                True, (255, 255, 255)
            )

            texto_comando8 = fonte.render(
                "ENTER na cozinha - Confirma os ingredientes escolhidos.",
                True, (255, 255, 255)
            )

            texto_comando9 = fonte.render(
                "ENTER na tela de resultados do pedido - Volta ao menu."
                , True, (255, 255, 255)
            )

            texto_comando10 = fonte.render(
                "ENTER na tela de score - Volta ao menu.",
                True, (255, 255, 255)
            )

            self.window.blit(texto_comando1, (30, 50))
            self.window.blit(texto_comando2, (30, 90))
            self.window.blit(texto_comando3, (30, 130))
            self.window.blit(texto_comando4, (30, 180))
            self.window.blit(texto_comando5, (30, 220))
            self.window.blit(texto_comando6, (30, 260))
            self.window.blit(texto_comando7, (30, 300))
            self.window.blit(texto_comando8, (30, 330))
            self.window.blit(texto_comando9, (30, 380))
            self.window.blit(texto_comando10, (30, 420))
            self.window.blit(texto_comando12, (30, 480))
            self.window.blit(texto_comando13, (30, 530))
            self.window.blit(texto_comando14, (30, 560))
            self.window.blit(texto_comando15, (30, 620))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
