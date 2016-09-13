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
a = 0
b = 0
largura = 4000
altura = 600
frame = 0.0
class PlayerHealth():

	healthAmount = 100

	def displayHealth(self,tela):
		text.ExibirTexto(tela,'Food:',320,10,15)
		text.ExibirTexto(tela,str(self.healthAmount),400,10,15, Color.DarkRed)

	def bloodblur(self,tela):
		global a,b,largura,altura,frame

		caminho = os.path.join('tileset','bloodblur.png')

		if frame >= 1.0:
			a += 800
			frame = 0.0

		frame += 0.1

		if a >= (800 * 5):
			a = 0
		blur = pygame.image.load(caminho).convert_alpha()
		tela.blit(blur,(0, 0),(a,b,largura,altura))

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


class Turnos():

	 playerTurn = True
