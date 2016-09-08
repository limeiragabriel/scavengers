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

LevelAtual = 1

playerHealth = PlayerHealth()

# mostrar o primeiro dia /// tirar quando implementar o menu
nextLevel(tela,survivor,LevelAtual)

# ... loop principal ...
while True:

	if playerHealth.healthAmount <= 0:
		som.stop()
		GameOver(tela,LevelAtual)

	if survivor.get_number() == 39:
		LevelAtual += 1
		nextLevel(tela,survivor,LevelAtual)
		survivor = Survivor(40,520)

	CloseWindow()
	MovePlayer(tela,survivor, zombie1)

	tela.fill((0,0,0))
	Tile.draw_tiles(tela)

	text.ExibirTexto(tela,'Day '+str(LevelAtual),20,10,15)
	playerHealth.displayHealth(tela)

	survivor.draw(tela)
	zombie1.draw(tela)

	if audio == False:
		som.play(-1)
		audio = True

	pygame.display.set_caption('FPS %.2f' %(clock.get_fps()) )
	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1