import pygame,os

def ExibirTexto(tela, texto, x, y, size = 15, color = (255,255,255), font_type = os.path.join("PressStart2P-Regular.ttf")):

	try:
		texto = str(texto)
		caminho = os.path.join("PressStart2P-Regular.ttf")
		font = pygame.font.Font(caminho, size)
		texto = font.render(texto, False, color)
		tela.blit(texto, (x,y))
	
	except Exception:
		print 'Erro de Fonte'