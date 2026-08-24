import pygame

from database.Banco import Banco
from domain.Avaliacao import Avaliacao
from domain.Comandos import Comandos
from domain.Historico import Historico
from domain.Menu import Menu
from domain.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from domain.NomeJogador import NomeJogador
from domain.PedidoAleatorio import PedidoAleatorio
from domain.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.score = Score()
        self.banco = Banco()
        self.nome_jogador = ""
        self.score.pontuacao = 0

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                nome_jogador = NomeJogador(self.window)
                self.nome_jogador = nome_jogador.run()
                pedido_aleatorio = PedidoAleatorio(self.window, self.score)
                comida = pedido_aleatorio.run()
                resultado = comida.run()

                avalicao = Avaliacao(self.window, resultado, self.score, comida.ingredientes_pedido,comida.ingredientes_do_jogador)

                avalicao.run()
                self.banco.salvar_pontuacao(self.nome_jogador, self.score.pontuacao)
            elif menu_return == MENU_OPTIONS[1]:
                historico = Historico(self.window, self.banco)
                historico.run()
            elif menu_return == MENU_OPTIONS[2]:
                comandos = Comandos(self.window)
                comandos.run()

            elif menu_return == MENU_OPTIONS[3]:
                pygame.quit()
                quit()
            else:
                pass
