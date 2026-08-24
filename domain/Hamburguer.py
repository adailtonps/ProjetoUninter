from logging import exception

import pygame


class Hamburguer:
    def __init__(self, window, score, ingredientes_pedido):
        self.ingredientes_pedido = ingredientes_pedido
        self.score = score
        self.window = window
        self.surf = pygame.image.load('./asset/hamburguer.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.ingredientes_do_jogador = ["PÃO"]
        self.mensagem = ""
        self.mensagem_tempo = 0
        self.qnt_jogador = len(self.ingredientes_pedido)
        self.ingredientes = [
            ("PÃO", pygame.Rect(206, 312, 100, 90)),
            ("TOMATE", pygame.Rect(352, 322, 100, 90)),
            ("QUEIJO", pygame.Rect(486, 319, 100, 90)),
            ("CARNE DE HAMBÚRGUER", pygame.Rect(191, 445, 100, 90)),
            ("ALFACE", pygame.Rect(344, 449, 100, 90)),
            ("KETCHUP", pygame.Rect(475, 450, 70, 85)),
            ("MOSTARDA", pygame.Rect(550, 450, 70, 85))
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
            self.window.blit(ingrediente_ja_adicionado_texto, (20, 20))
            for i, ingrediente in enumerate(self.ingredientes_do_jogador):
                texto = fonte.render(ingrediente+" - OK!", True, (0, 255, 0))
                self.window.blit(texto, (20,60+i*30))

            pygame.display.flip()

            for event in pygame.event.get():
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
                            if ultimo_ingrediente not in ["PÃO"]:
                                self.ingredientes_do_jogador.pop()

                    if event.key == pygame.K_RETURN:
                        qnt_correta = 0

                        for ingrediente in self.ingredientes_pedido:
                            if ingrediente in self.ingredientes_do_jogador:
                                qnt_correta += 1

                        porcentagem = round((qnt_correta / len(self.ingredientes_pedido)) * 100)

                        self.ingredientes_corretos = "Ingredientes corretos:", qnt_correta
                        self.ingredientes_do_pedido = "Ingredientes do pedido:", len(self.ingredientes_pedido)
                        self.porcentagem_de_acerto = "Porcentagem:", porcentagem, "%"

                        if porcentagem == 100:
                            resultado = "Pedido correto!"
                            self.score.pontuacao += 100
                            print("Score: ", self.score.pontuacao)

                        elif porcentagem >= 50:
                            resultado= "Pedido parcialmente correto!"
                            self.score.pontuacao += 65
                            print("Score: ", self.score.pontuacao)
                        elif porcentagem > 0:
                            resultado = "Pedido bem abaixo do esperado!"
                            self.score.pontuacao += 35
                            print("Score: ", self.score.pontuacao)
                        else:
                            resultado = "Pedido horrível!"
                            self.score.pontuacao += 0
                            print("Score: ", self.score.pontuacao)

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        return resultado