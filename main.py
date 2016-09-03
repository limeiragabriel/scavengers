import pygame, sys
from tile import *
from charactersC import *
from interacoes import Interacoes

pygame.init()
pygame.mixer.init()


# ... tela ...
LARGURA,ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA,ALTURA))

# ... taxa de refresh ...
clock = pygame.time.Clock()
FPS = 30
total_frames = 0

# ... tiles onde o player nao pode andar ...
invalidos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
			21,40,41,60,61,80,81,100,101,120,121,140,141,160,
			161,180,181,200,201,220,221,240,241,260,261,280,
			281,282,283,284,285,286,287,288,289,290,291,292,293,
			294,295,296,297,298,299,300)


# definindo onde sera cada tile valido e invalido
for y in range(0, tela.get_height(), 40):
	for x in range(0, tela.get_width(), 40):
		if Tile.total_tiles in invalidos:
			Tile(x, y, 'solido')
		else:
			Tile(x, y, 'vazio')


zombie1 = Zombie(200,240)
survivor = Survivor(400,120)


# ... musica de fundo ...
som = pygame.mixer.Sound('scavengers_music.aif')
som.set_volume(0.5)
audio = False
# ... .... ...... ....

generate = True
# ... loop principal ...
while True:

	Interacoes(tela,survivor)

	tela.fill([0,0,0])
	
	Tile.draw_tiles(tela)

	survivor.draw(tela)
	zombie1.draw(tela)

	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1

	if audio == False:
		som.play(-1)
		audio = True