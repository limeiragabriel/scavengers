import pygame, sys, text
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
TilesLaterais(tela)
Tile.RecarregarAleatorios()
# ................................


zombie1 = Zombie(Tile.get_tile(126).x,Tile.get_tile(126).y)
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

	Tile.draw_tiles(tela)
	text.ExibirTexto(tela,'Day '+str(LevelAtual),20,10,15)
	
	survivor.draw(tela)
	zombie1.draw(tela)

	if survivor.get_number() == 39:
		LevelAtual += 1
		nextLevel(tela,survivor,LevelAtual)
		survivor = Survivor(40,520)


	if audio == False:
		som.play(-1)
		audio = True

	#pygame.display.set_caption('FPS %.2f' %(clock.get_fps()) )
	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1