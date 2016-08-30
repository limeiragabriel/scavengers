import pygame


# nao sei como funcionou entao melhor nao mexer kkkkkkk
def ExibirTexto(screen, text, x, y, size = 15, color = (255,255,255), font_type = 'PressStart2P-Regular.ttf'):

	try:
		text = str(text)
		font = pygame.font.SysFont(font_type, size)
		text = font.render(text, False, color)
		screen.blit(text, (x,y))

	except Exception, e:
		print 'Font error'
		raise e