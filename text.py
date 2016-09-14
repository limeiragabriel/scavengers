import pygame,os
from colors import Color

def ExibirTexto(tela, texto, x, y, size = 15, color = Color.White, font_type = os.path.join("font","PressStart2P-Regular.ttf")):

	try:
		texto = str(texto)
		caminho = os.path.join("font","PressStart2P-Regular.ttf")
		font = pygame.font.Font(caminho, size)
		texto = font.render(texto, False, color)
		tela.blit(texto, (x,y))
	
	except Exception:
		print 'Erro de Fonte'