from logging import exception
from tkinter.font import BOLD

import pygame


class Pizza:
    def __init__(self, window, score, ingredientes_pedido):
        self.ingredientes_pedido = ingredientes_pedido
        self.window = window
        self.score = score

        self.surf = pygame.image.load('./asset/pizza.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.ingredientes_do_jogador = ["MASSA DE PIZZA"]
        self.mensagem = ""
        self.mensagem_tempo = 0
        self.pedido_finalizado = False
        self.qnt_jogador = len(self.ingredientes_pedido)
        self.ingredientes = [
            ("MASSA", pygame.Rect(205, 306, 100, 90)),
            ("TOMATE", pygame.Rect(347, 308, 100, 90)),
            ("QUEIJO", pygame.Rect(489, 306, 100, 90)),
            ("SALAME", pygame.Rect(209, 404, 100, 90)),
            ("ALFACE", pygame.Rect(350, 418, 100, 90)),
            ("CEBOLA", pygame.Rect(208, 523, 100, 90)),
            ("COGUMELO", pygame.Rect(352, 521, 100, 90)),
            ("MOLHO DE TOMATE", pygame.Rect(493, 540, 100, 60)),
            ("KETCHUP", pygame.Rect(475, 435, 70, 85)),
            ("MOSTARDA", pygame.Rect(550, 435, 70, 85))
        ]

    def run(self):
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            fonte = pygame.font.SysFont('Arial', 20, bold=True)

            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.mensagem_tempo < 2000:
                texto = fonte.render(self.mensagem, True, (255, 0, 0))
                self.window.blit(texto, (250, 200))

            ingrediente_ja_adicionado_texto = fonte.render("INGREDIENTES JÁ ADICIONADOS!", True, (255, 0, 0))
            self.window.blit(ingrediente_ja_adicionado_texto, (20, 20))
            for i, ingrediente in enumerate(self.ingredientes_do_jogador):
                texto = fonte.render(ingrediente + " - OK!", True, (0, 255, 0))
                self.window.blit(texto, (20, 60 + i * 30))

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
                            if ultimo_ingrediente not in ["MASSA DE PIZZA"]:
                                self.ingredientes_do_jogador.pop()

                    if event.key == pygame.K_RETURN:
                        qnt_correta = 0

                        for ingrediente in self.ingredientes_pedido:
                            if ingrediente in self.ingredientes_do_jogador:
                                qnt_correta += 1


                        porcentagem = round((qnt_correta / len(self.ingredientes_pedido)) * 100)

                        print("Ingredientes corretos:", qnt_correta)
                        print("Ingredientes do pedido:", len(self.ingredientes_pedido))
                        print("Porcentagem:", porcentagem, "%")

                        if porcentagem == 100:
                            resultado = "Pedido correto!"
                            self.score.pontuacao += 100
                            print("Score: ", self.score.pontuacao)

                        elif porcentagem >= 50:
                            resultado = "Pedido parcialmente correto!"
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