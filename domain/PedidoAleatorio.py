import random

import pygame

from domain.Hamburguer import Hamburguer
from domain.Pizza import Pizza
from domain.Sopa import Sopa


class PedidoAleatorio:
    comidas = [
        "HAMBÚRGUER",
        "PIZZA",
        "SOPA"
    ]

    def __init__(self, window, score):
        self.window = window
        self.score = score
        self.surf = pygame.image.load('./asset/cliente_balao.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        rect_balao = pygame.Rect(385, 53, 357, 283)

        self.pedido = self.gerar_pedido()
        self.ingredientes_pedido = []

        if self.pedido == "PIZZA":
            self.ingredientes_pedido.append("MASSA DE PIZZA")

            quantidade_aleatoria_ingredientes = random.randint(1, len(self.ingredientes_pizza))
            ingredientes_sorteados_pizza = random.sample(self.ingredientes_pizza, quantidade_aleatoria_ingredientes)

            self.ingredientes_pedido.extend(ingredientes_sorteados_pizza)

        elif self.pedido == "SOPA":
            self.ingredientes_pedido.append("ÁGUA QUENTE")
            self.ingredientes_pedido.append("MACARRÃO")

            quantidade_aleatorio_ingredientes = random.randint(1, len(self.ingredientes_sopa))

            ingrediente_sorteados_sopa = random.sample(self.ingredientes_sopa, quantidade_aleatorio_ingredientes)

            self.ingredientes_pedido.extend(ingrediente_sorteados_sopa)

        elif self.pedido == "HAMBÚRGUER":
            self.ingredientes_pedido.append("PÃO")
            quantidade_aleatoria_ingredientes = random.randint(1, len(self.ingredientes_hamburguer))
            ingredientes_aleatorios_burguer = random.sample(self.ingredientes_hamburguer,
                                                            quantidade_aleatoria_ingredientes)

            self.ingredientes_pedido.extend(ingredientes_aleatorios_burguer)

    def gerar_pedido(self):
        return random.choice(self.comidas)

    ingredientes_pizza = [
        "MOLHO DE TOMATE",
        "QUEIJO",
        "ALFACE",
        "CAEBOLA",
        "SALAME",
        "COGUMELO",
        "KETCHUP",
        "MOSTARDA"
    ]

    ingredientes_sopa = [
        "BATATA",
        "CENOURA",
        "BETERRABA",
        "ABÓBORA",
        "CARNE DE FRANGO",
        "CEBOLA",
        "ESPINAFRE"
    ]

    ingredientes_hamburguer = [
        "CARNE DE HAMBÚRGUER",
        "TOMATE",
        "QUEIJO",
        "ALFACE",
        "KETCHUP",
        "MOSTARDA"
    ]

    def run(self):
        fonte = pygame.font.SysFont('Arial', 20, bold=True)
        fonteIngredientes = pygame.font.SysFont('Arial', 12, bold=True)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            pedido_texto = fonte.render(f"Desejo {self.pedido} com",True, (255, 0, 0))
            self.window.blit(pedido_texto, (400, 65))

            for i, ingredientes_do_pedido in enumerate(self.ingredientes_pedido):
                texto = fonteIngredientes.render(ingredientes_do_pedido, True, (255, 0, 0))
                self.window.blit(texto, (400, 95+i*20))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.pedido == "PIZZA":
                            return Pizza (self.window, self.score, self.ingredientes_pedido)

                        elif self.pedido == "SOPA":
                            return Sopa(self.window, self.score, self.ingredientes_pedido)

                        elif self.pedido == "HAMBÚRGUER":
                            return Hamburguer(self.window, self.score, self.ingredientes_pedido)

