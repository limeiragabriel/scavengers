import pygame


# nao sei como funcionou entao melhor nao mexer kkkkkkk
def ExibirTexto(tela, texto, x, y, size = 15, color = (255,255,255), font_type = 'PressStart2P-Regular.ttf'):

	try:
		texto = str(texto)
		font = pygame.font.SysFont(font_type, size)
		texto = font.render(texto, False, color)
		tela.blit(texto, (x,y))
	
	except Exception:
		print 'Erro de Fonte'