import pygame, sys, random, text,os
from tile import Tile
from colors import Color
from charactersC import Zombie

# =============== tiles ao redor do cenario =======================
laterais = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
			21,40,41,60,61,80,81,100,101,120,121,140,141,160,
			161,180,181,200,201,220,221,240,241,260,261,280,
			281,282,283,284,285,286,287,288,289,290,291,292,293,
			294,295,296,297,298,299,300)
# ==================================================================

# ============== fechar a janela do game pelo "x" ===================
def CloseWindow():
	close = pygame.event.get(pygame.QUIT)
	if close:
		pygame.quit()
		sys.exit()
# ====================================================================
# ============== textos de inicio antes do gameplay ==================
def Intro(tela):
	clock = pygame.time.Clock()
	tempo = 0
	soundTime = 0
	R,G,B = 255,255,255
	audio = False

	startS = os.path.join('sounds','MenuGameStart.wav')
	StartSound = pygame.mixer.Sound(startS)
	StartSound.set_volume(0.5)

	# ======= efeito de 'esmaecer' e som de start =====
	while soundTime < 240:
		CloseWindow()
		clock.tick(30)

		if audio == False:
			StartSound.play()
			audio = True

		tela.fill([R,G,B])
		if R >= 2:
			R,G,B = R-2,G-2,B-2
		soundTime += 1
		pygame.display.flip()
	#================================================
	#============ exibicao dos textos ==============
	while tempo < 120:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'September 28.',100,500,15)
		tempo += 1
		pygame.display.flip()
	while tempo < 240:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'Daylight...',100,500,15)
		tempo += 1
		pygame.display.flip()
	while tempo < 360:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'The Monsters have overtaken the city.',100,500,15)
		tempo += 1
		pygame.display.flip()
	while tempo < 480:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'Somehow...',100,500,15)
		tempo += 1
		pygame.display.flip()
	while tempo < 600:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,"I'm still... Alive.",100,500,15)
		tempo += 1
		pygame.display.flip()
	#===============================================

	tempo = 0
	soundTime = 0
	R,G,B = 255,255,255
	audio = False
# ==========================================================================
# ===================== gera o proximo nivel =========================
def nextLevel(tela,survivor,LevelAtual):

	tempo = 0
	clock = pygame.time.Clock()

	while tempo < 60:
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'Day '+str(LevelAtual),100,250,50)
		tempo += 1
		pygame.display.flip()

	Tile.refresh()
	#Tile.RecarregarAleatorios()
# ========================================================================

# ========== tela de fim de jogo ao acabar a energia do player ===========
def GameOver(tela,LevelAtual):
	clock = pygame.time.Clock()

	if LevelAtual > 1:
		texto = ' Days You Starved.'
	else:
		texto = ' Day You Starved.'

	while True:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'After ' +str(LevelAtual) + texto,100,250,15)
		pygame.display.flip()
# ==========================================================================

# ============== invalidos ao redor do cenario ==============================
def TilesLaterais(tela):
	for y in range(0, tela.get_height(), 40):
		for x in range(0, tela.get_width(), 40):
			if Tile.total_tiles in laterais:
				Tile(x, y, 'solido')
			else:
				Tile(x, y, 'vazio')
# ===========================================================================

# ================= exibe a quantidade de energia do player ===================
class PlayerHealth():

	healthAmount = 100

	def displayHealth(self,tela,tonalidade):
		text.ExibirTexto(tela,'Food:',320,10,15)
		text.ExibirTexto(tela,str(self.healthAmount),400,10,15,tonalidade)

# ============================================================================

# ========== Torna inacessivel tiles onde estao os zumbis =======================
def PosicaoDeZumbi(listaDeTiles = []):

	for zombie in Zombie.Lista:
		for tile in Tile.Lista:
			if tile.number == zombie.get_number():
				listaDeTiles.append(tile)

	for zombie in Zombie.Lista:
		for tile in listaDeTiles:
			if tile.number == zombie.get_number():
				tile.walkable = False
# ================================================================================

# === zera a lista de tiles de zumbis para q possa ser verificada a posicao novamente ======
def AttPosicaoDeZumbi(listaDeTiles):

	for tile in listaDeTiles:
		tile.walkable = True
# ===========================================================================================

# ===================== geremcia turnos, menu, dificuldade etc ========================
class Gerenciador():

	 playerTurn = True

	 onMenu = True

	 primeiroDia = True

	 gameMode = 'easy'
