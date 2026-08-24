import pygame

class Sopa:
    def __init__(self, window, score, ingredientes_pedido):
        self.ingredientes_pedido = ingredientes_pedido
        self.window = window
        self.score = score

        self.surf = pygame.image.load('./asset/sopa.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.ingredientes_do_jogador =["ÁGUA QUENTE","MACARRÃO"]
        self.mensagem = ''
        self.mensagem_tempo = 0
        self.qnt_jogador = len(self.ingredientes_pedido)
        self.ingredientes = [
            ("ÁGUA QUENTE", pygame.Rect(210, 300, 100, 90)),
            ("BATATA", pygame.Rect(350, 300, 100, 90)),
            ("MACARRÃO", pygame.Rect(500, 400, 100, 90)),
            ("CENOURA", pygame.Rect(500, 302, 100, 90)),
            ("BETERRABA", pygame.Rect(209, 409, 100, 90)),
            ("ESPINAFRE", pygame.Rect(346, 417, 100, 90)),
            ("CEBOLA", pygame.Rect(195, 521, 100, 90)),
            ("ABÓBORA", pygame.Rect(355, 521, 100, 90)),
            ("CARNE DE FRANGO", pygame.Rect(500, 525, 120, 90))
        ]


    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            fonte = pygame.font.SysFont('Arial', 20, bold=True)

            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.mensagem_tempo < 2000:
                texto = fonte.render(self.mensagem, True, (255, 0, 0))
                self.window.blit(texto, (250, 200))

            ingrediente_ja_adicionado_texto = fonte.render("INGREDIENTES JÁ ADICIONADOS:", True, (255, 0, 0))
            self.window.blit(ingrediente_ja_adicionado_texto, (20,20))
            for i, ingrediente in enumerate(self.ingredientes_do_jogador):
                texto = fonte.render(ingrediente+" - OK!", True, (0, 255, 0))
                self.window.blit(texto, (20, 60 + i * 30))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    for nome, rect in self.ingredientes:
                        if rect.collidepoint(event.pos):
                            if nome in self.ingredientes_do_jogador:
                                self.mensagem = "INGREDIENTE JÁ ADICIONADO!"
                                self.mensagem_tempo = pygame.time.get_ticks()
                            else:
                                self.ingredientes_do_jogador.append(nome)
                                print(nome)
                                print(self.ingredientes_do_jogador)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.ingredientes_do_jogador:
                            ultimo_ingrediente = self.ingredientes_do_jogador[-1]
                            if ultimo_ingrediente not in ["ÁGUA QUENTE", "MACARRÃO"]:
                                self.ingredientes_do_jogador.pop()

                    if event.key == pygame.K_RETURN:
                        qnt_correta = 0

                        for ingrediente in self.ingredientes_pedido:
                            if ingrediente in self.ingredientes_do_jogador:
                                qnt_correta += 1

                        porcentagem = round((qnt_correta / len(self.ingredientes_pedido)) * 100)

                        print("Ingredientes corretos:", qnt_correta)
                        print("Ingredientes do pedido:", len(self.ingredientes_pedido))
                        print("Porcentagem:", porcentagem,"%")

                        if porcentagem == 100:
                            resultado="Pedido correto!"
                            self.score.pontuacao += 100
                            print("Score: ", self.score.pontuacao)

                        elif porcentagem >= 50:
                            resultado="Pedido parcialmente correto!"
                            self.score.pontuacao += 65
                            print("Score: ", self.score.pontuacao)
                        elif porcentagem > 0:
                            resultado="Pedido bem abaixo do esperado!"
                            self.score.pontuacao += 35
                            print("Score: ", self.score.pontuacao)
                        else:
                            resultado="Pedido horrível!"
                            self.score.pontuacao += 0
                            print("Score: ", self.score.pontuacao)

                        return resultado
