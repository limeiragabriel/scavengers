import pygame, sys
from tile import *
from charactersC import *
from interacoes import *
from gameManager import *

pygame.init()
pygame.mixer.init()


# ... tela ...
LARGURA,ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA,ALTURA))

# ... taxa de refresh ...
clock = pygame.time.Clock()
FPS = 30
total_frames = 0

# tiles invalidos ao redor do cenario
invalidTiles(tela)
# ................................

zombie1 = Zombie(200,240)
survivor = Survivor(40,520)

# ... musica de fundo ...
som = pygame.mixer.Sound('scavengers_music.aif')
audio = False
# ... .... ...... ....

# randomiza as variaveis para gerar o terreno
LevelAtual = 1

# ... loop principal ...
while True:

	QuitGame()
	MovePlayer(tela,survivor,zombie1)

	tela.fill([0,0,0])
	
	if nextLevel(survivor):
		survivor = Survivor(40,520)
		LevelAtual += 1

	Tile.draw_tiles(tela)

	survivor.draw(tela)
	zombie1.draw(tela)

	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1


	if audio == False:
		som.play(-1)
		audio = True