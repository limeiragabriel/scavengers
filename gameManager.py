import pygame, sys, random, text
from charactersC import *
from tile import Tile

# tiles ao redor do cenario
laterais = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
			21,40,41,60,61,80,81,100,101,120,121,140,141,160,
			161,180,181,200,201,220,221,240,241,260,261,280,
			281,282,283,284,285,286,287,288,289,290,291,292,293,
			294,295,296,297,298,299,300)
# ..................................

# fechar a janela do game
def QuitGame():
	close = pygame.event.get(pygame.QUIT)
	if close:
		pygame.quit()
		sys.exit()
# ........................

def levelTransition(tela,LevelAtual):
	tempo = 0
	while tempo < 120:
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'Day '+str(LevelAtual),50,100,30)
		tempo += 1


# avancar e gerar o proximo level
def nextLevel(tela,survivor,LevelAtual):

	tempo = 0
	fundo = pygame.image.load("fundo.png")

	while tempo < 120:
		tela.blit(fundo,(0,0))
		text.ExibirTexto(tela,'Day '+str(LevelAtual),100,250,50)
		tempo += 1
		pygame.display.flip()

	Tile.refresh()
	Tile.RecarregarAleatorios()
# ..............................

# definindo onde sera cada tile valido e invalido
def TilesLaterais(tela):
	for y in range(0, tela.get_height(), 40):
		for x in range(0, tela.get_width(), 40):
			if Tile.total_tiles in laterais:
				Tile(x, y, 'solido')
			else:
				Tile(x, y, 'vazio')
# ................................................
