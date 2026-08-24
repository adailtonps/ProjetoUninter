import pygame


class Avaliacao:
    def __init__(self, window, resultado, score, ingredientes_pedido, ingredientes_do_jogador):
        self.window = window
        self.resultado = resultado
        self.score = score
        self.ingredientes_pedido = ingredientes_pedido
        self.ingredientes_do_jogador = ingredientes_do_jogador

        self.surf = pygame.image.load('asset/cliente_balao.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        fonte = pygame.font.SysFont('Arial', 15, bold=True)
        fonte_ingredientes = pygame.font.SysFont('Arial', 10, bold=True)

        ingredientes_corretos = []

        for ingrediente in self.ingredientes_pedido:
            if ingrediente in self.ingredientes_do_jogador:
                ingredientes_corretos.append(ingrediente)

        if self.resultado == "Pedido correto!":
            imagem = pygame.image.load('asset/cliente_feliz.png')

        elif self.resultado == "Pedido parcialmente correto!":
            imagem = pygame.image.load('asset/cliente_ok.png')

        elif self.resultado == "Pedido bem abaixo do esperado!":
            imagem = pygame.image.load('asset/cliente_desapontado.png')

        else:
            imagem = pygame.image.load('asset/cliente_brava.png')

        resposta_pedido_okOrnot = fonte.render(
            self.resultado,
            True,
            (255, 0, 0)
        )

        resposta_score = fonte.render(
            f"Pontuação: {self.score.pontuacao}",
            True,
            (255, 0, 0)
        )

        resposta_acertos = fonte.render(
            f"Você acertou: {len(ingredientes_corretos)}",
            True,
            (255, 0, 0)
        )

        titulo = fonte.render(
            "O pedido era:",
            True,
            (255, 0, 0)
        )

        while True:
            self.window.blit(imagem, (0, 0))

            self.window.blit(resposta_pedido_okOrnot, (420, 55))
            self.window.blit(resposta_score, (420, 75))
            self.window.blit(resposta_acertos, (420, 95))
            self.window.blit(titulo, (420, 125))

            # Ingredientes em uma lista compacta
            for i, ingrediente in enumerate(self.ingredientes_pedido):
                texto = fonte_ingredientes.render(
                    ingrediente,
                    True,
                    (255, 0, 0)
                )

                self.window.blit(
                    texto,
                    (420, 145 + i * 13)
                )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return
