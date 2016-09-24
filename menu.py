import pygame, sys, os
from gameManager import CloseWindow
from gameManager import Gerenciador

telas = ['menu01.png','menu02.png','menu03.png','menu04.png','menuControls.png']
telaAtual = 0

podeTrocar = True


def trocarMenu():

	Move = os.path.join('sounds','move.wav')
	MoveSound = pygame.mixer.Sound(Move)
	MoveSound.set_volume(0.5)

	Select = os.path.join('sounds','select.wav')
	SelectSound = pygame.mixer.Sound(Select)
	SelectSound.set_volume(0.5)

	Cancel = os.path.join('sounds','cancel.wav')
	CancelSound = pygame.mixer.Sound(Cancel)
	CancelSound.set_volume(0.5)

	global telaAtual, podeTrocar

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			

			# =============== mover a selecao (L e R) ==========================
			if event.key == pygame.K_LEFT and podeTrocar:

				if telaAtual > 0:
					MoveSound.play()
					telaAtual -= 1
					
			elif event.key == pygame.K_RIGHT and podeTrocar:
				if telaAtual < 3:
					MoveSound.play()
					telaAtual += 1
			# =========================================================================

			# ==================  mostra a tela controls =================================
			if (event.key == pygame.K_SPACE ) and (telaAtual == 2):
				podeTrocar = False
				SelectSound.play()
				telaAtual = 4
			# ============================================================================
			
			# ========== se tela atual for control a acao volta ao menu principal ============
			if telaAtual == 4 and event.key == pygame.K_ESCAPE:
					podeTrocar = True
					CancelSound.play()
					telaAtual = 0
			# ===============================================================================

			# ==================== fecha o game caso selecione exit ======================
			if telaAtual == 3 and event.key == pygame.K_SPACE:
				pygame.quit()
				sys.exit()

			# ================= saltar menu e iniciar o jogo ========================
			if (telaAtual == 0) and (event.key == pygame.K_SPACE):
				Gerenciador.gameMode = 'easy'
				Gerenciador.onMenu = False
			elif (telaAtual == 1) and (event.key == pygame.K_SPACE):
				Gerenciador.gameMode = 'hard'
				Gerenciador.onMenu = False
			# ========================================================================





def Menu(tela):

	global telaAtual,telas


	caminhoMenu = os.path.join('menu_imgs',telas[telaAtual])
	imgMenu = pygame.image.load(caminhoMenu)

	tela.blit(imgMenu,(0,0))

	CloseWindow()

	trocarMenu()

	pygame.display.flip()
