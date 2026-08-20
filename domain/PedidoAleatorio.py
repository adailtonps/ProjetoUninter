import random

import pygame

from domain import Pizza, Hamburguer, Sopa


class PedidoAleatorio:
    comidas = [
        "hamburguer",
        "pizza",
        "sopa"
    ]

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/cliente_pedindo.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        self.pedido = self.gerar_pedido()
        self.ingredientes_pedido = []

        if self.pedido == "pizza":
            self.ingredientes_pedido.append("massa")
            quantidade_aleatoria_ingredientes = random.randint(1, len(self.ingredientes_pizza))
            ingredientes_sorteados_pizza = random.sample(self.ingredientes_pizza, quantidade_aleatoria_ingredientes)

            self.ingredientes_pedido.extend(ingredientes_sorteados_pizza)

        elif self.pedido == "sopa":
            self.ingredientes_pedido.append("água_quente_temperada")
            quantidade_aleatorio_ingredientes = random.randint(1, len(self.ingredientes_sopa))
            ingrediente_sorteados_sopa = random.sample(self.ingredientes_sopa, quantidade_aleatorio_ingredientes)

            self.ingredientes_pedido.extend(ingrediente_sorteados_sopa)

        elif self.pedido == "hamburguer":
            self.ingredientes_pedido.append("pão")
            quantidade_aleatoria_ingredientes = random.randint(1, len(self.ingredientes_hamburguer))
            ingredientes_aleatorios_burguer = random.sample(self.ingredientes_hamburguer,
                                                            quantidade_aleatoria_ingredientes)

            self.ingredientes_pedido.extend(ingredientes_aleatorios_burguer)

    def gerar_pedido(self):
        return random.choice(self.comidas)

    ingredientes_pizza = [
        "molho_tomate",
        "queijo",
        "alface",
        "cebola",
        "salame",
        "cogumelo",
        "ketchup",
        "mostarda"
    ]

    ingredientes_sopa = [
        "batata",
        "cenoura",
        "beterraba",
        "abobora",
        "carne_frango",
        "cebola"
    ]

    ingredientes_hamburguer = [
        "carne",
        "tomate",
        "queijo",
        "alface",
        "ketchup",
        "mostarda"
    ]

    def run(self):
        while True:
            self.rect = self.surf.get_rect(left=0, top=0)
            self.window.blit(source=self.surf, dest=self.rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if (self.pedido == "pizza"):
                            pizza = Pizza(self.ingredientes_pedido)
                            return pizza
                        elif (self.pedido == "sopa"):
                            sopa = Sopa(self.ingredientes_pedido)
                            return sopa
                        elif (self.pedido == "hamburguer"):
                            hamburguer = Hamburguer(self.ingredientes_pedido)
                            return hamburguer
