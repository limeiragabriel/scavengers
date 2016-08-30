import pygame, sys

pygame.init()


# ... tela ...
WIDTH,HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# ... taxa de refresh ...
clock = pygame.time.Clock()
FPS = 30
total_frames = 0

while True:

	# ... fechando a janela ...
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# ... ...

	screen.fill([0,0,0])
	
	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1