import pygame, sys
from tile import Tile

pygame.init()


# ... tela ...
LARGURA,ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA,ALTURA))

# ... taxa de refresh ...
clock = pygame.time.Clock()
FPS = 30
total_frames = 0

# ... tiles onde o player nao pode andar ...
invalidos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
			19,37,55,73,91,109,127,145,163,181,
			198,199,216,217,234,235,252,253,
			36,54,72,90,108,126,144,162,180,198,
			270,271,272,273,274,275,276,277,278,279,280,281,
			282,283,284,285,286,287,288)


for y in range(0, tela.get_height(), 40):
	for x in range(0, tela.get_width(), 40):
		if Tile.total_tiles in invalidos:
			Tile(x, y, 'solido')
		else:
			Tile(x, y, 'vazio')


# ... loop principal ...
while True:

	# ... fechando a janela ...
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# ... ...

	tela.fill([0,0,0])
	
	Tile.draw_tiles(tela)

	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1