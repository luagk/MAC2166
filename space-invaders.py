'''
 Para rodar o jogo, precisa instalar o PyGame utilizando o comando:

 $ python -m pip install pygame

 Depois, coloque os arquivos ep03.py e space-invaders.py na mesma pasta.
 Dentro da pasta inicie o jogo a partir do comando:

 $ python space-invaders.py
  
'''
import pygame
from ep03 import *

#############################################################
# Codigo do jogo                                            #
#############################################################

class Game:
    screen = None
    alienigenas = []
    municoes = []
    pontos = 0
    perdeu = False
    modo = "NORMAL" # or "SPECIAL"

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        finalizado = False

        heroi = Heroi(self, width / 2, height - 20)
        gerador = GeradorDeAliens(self)
        municao = None

        while not finalizado:
            if len(self.alienigenas) == 0:
                if self.modo == "NORMAL":
                    self.displayText("Voce venceu com "+str(self.pontos)+" pontos!",
                                     "Pressione 'x' para ativar o modo SPECIAL!!")
                if self.modo == "SPECIAL":
                    self.displayText("Voce venceu com "+str(self.pontos)+" pontos!",
                                     "Parabens!")

            teclaPressionada = pygame.key.get_pressed()
            if teclaPressionada[pygame.K_LEFT]:
                heroi.x -= 2 if heroi.x > 1 else 0
            elif teclaPressionada[pygame.K_RIGHT]:
                heroi.x += 2 if heroi.x < width - 1 else 0
            elif teclaPressionada[pygame.K_x] and \
                 self.modo == "NORMAL" and  \
                 len(self.alienigenas) == 0:
                self.modo = "SPECIAL"
                self.pontos = 0
                gerador = GeradorDeAliens(self)
            elif teclaPressionada[pygame.K_r] and self.perdeu:
                self.alienigenas = []
                self.pontos = 0
                self.perdeu = False
                gerador = GeradorDeAliens(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finalizado = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.perdeu:
                    self.municoes.append(Municao(self, heroi.x, heroi.y))

            pygame.display.flip()
            self.clock.tick(60)
            if self.modo == "NORMAL":
                self.screen.fill(pygame.Color("white"))
            else:
                self.screen.fill(pygame.Color("black"))

            for alienigena in self.alienigenas: 
                alienigena.draw()
                alienigena.checkCollision(self)
                if (alienigena.v0[1] > height or alienigena.v1[1] > height or alienigena.v2[1] > height ):
                    self.perdeu = True
                    self.displayText("Voce perdeu com "+str(self.pontos)+" pontos.",
                                     "Pressione 'r' para reiniciar o jogo.")

            for municao in self.municoes:
                municao.draw()

            if not self.perdeu: heroi.draw()

    def displayText(self, text1, text2):
        pygame.font.init()

        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text1, False, pygame.Color("gray"))
        self.screen.blit(textsurface, (110, 160))

        font = pygame.font.SysFont('Arial', 30)
        textsurface = font.render(text2, False, pygame.Color("gray"))
        self.screen.blit(textsurface, (110, 360))


class Alienigena:
    def __init__(self, game, v0, v1, v2):
        self.game = game
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    def draw(self):
        pygame.draw.polygon(self.game.screen,
                         (81, 43, 88),  
                         [self.v0, self.v1, self.v2])
        if self.game.modo == "SPECIAL":
            self.v0[1] += 1
            self.v1[1] += 1
            self.v2[1] += 1

    def checkCollision(self, game):
        for municao in game.municoes:
            ponto = [ municao.x, municao.y ]
            v0 = self.v0
            v1 = self.v1
            v2 = self.v2
            if (pontoInterno(ponto, v0, v1, v2)):
                somarPontos = True
                try:
                    game.alienigenas.remove(self)
                    game.municoes.remove(municao)
                except:
                    somarPontos = False
                if somarPontos:
                    if (game.modo == "NORMAL"):
                        game.pontos += pontosNaBorda(v0,v1,v2)
                    else: # SPECIAL
                        game.pontos += pontosNaBorda(v0,v1,v2) + pontosInternos(v0,v1,v2)


class Heroi:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         pygame.Color("red"),
                         pygame.Rect(self.x, self.y, 18, 15))


# Gerador de alienigenas a partir das coordenadas
class GeradorDeAliens:
    def __init__(self, game):
        
        # alienigenas = [ ([150,250],[200,100],[100,150]),
        #                 ([400,480],[265,265],[388,388]),
        #                 ([500,400],[355,698],[421,699]),
        #                 ([  1,  1],[  9,  1],[  6,  6]) ]
        
        alienigenas = [ ([  0,200],[0  ,300],[100,200]),
                        ([ 50,300],[150,300],[150,200]),
                        ([200,200],[200,300],[300,300]),
                        ([250,200],[350,300],[350,200]),
                        ([400,200],[400,300],[500,200]),
                        ([550,200],[450,300],[550,300]),
                        ([600,200],[600,300],[700,300]),
                        ([650,200],[750,200],[750,300]),
                        ([400,400],[400,500],[500,500]),
                        ([450,400],[550,400],[550,500]) ]
        
        for alienigena in alienigenas:
            game.alienigenas.append( Alienigena(game, alienigena[0], 
                                                        alienigena[1], 
                                                        alienigena[2]) )


class Municao:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110),
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2


if __name__ == '__main__':
    game = Game(750, 750)

# Versão original do código:
# https://itnext.io/creating-space-invaders-clone-in-pygame-ea0f5336c677
# https://github.com/janjilecek/pygame-invaders