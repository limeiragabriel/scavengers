import pygame, sys, text,os
from tile import *
from charactersC import *
from interacoes import *
from gameManager import *
from menu import Menu
from spawn import *

pygame.init()
pygame.mixer.init()

# ====================== Resolucao ======================================
LARGURA,ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA,ALTURA))
# =======================================================================

# ==================== taxa de atualizacao ===============================
clock = pygame.time.Clock()
FPS = 30
total_frames = 0
# ========================================================================

# ================ tiles invalidos pelo cenario ==========================
TilesLaterais(tela)
#Tile.RecarregarAleatorios()
# ========================================================================

# ========= tiles do Back ground =========================================
caminho = os.path.join("tileset", "back.png")
ground = pygame.image.load(caminho).convert_alpha()
# ========================================================================

#=========================items spawpoits ================================

items = SpawnPoint()
items.makeSpawns()

displayRegen = LifeRegen()
#=========================================================================

# =================== personagens ========================================
enemyPoint = EnemySPoint()

zombie1 = Zombie(Tile.get_tile(enemyPoint.sp1).x,Tile.get_tile(enemyPoint.sp1).y)

survivor = Survivor(40,520)
# ========================================================================

# ======================= musica de fundo ================================
trilha = os.path.join('sounds','scavengers_music.aif')
som = pygame.mixer.Sound(trilha)
som.set_volume(1)
audio = False
# ========================================================================

# ======================== dia atual e energia ===========================
LevelAtual = 1
playerHealth = PlayerHealth()
tonalidade = Color.LimeGreen
# ========================================================================

Manager = Gerenciador() #classe do gamemanager

listaDeTiles = [] # armazenar posicoes dos zumbis

pygame.display.set_caption('Scavengers')
# ============================== loop principal ===========================
while True:
	# ================ fechar janela
	CloseWindow()
	# ==============================
	# ========================== menu principal ==============================
	while Manager.onMenu:
		Menu(tela)
	# ========================================================================
	#============= mostrar o primeiro dia ao sair do menu ================
	if Manager.primeiroDia:
		Intro(tela)
		nextLevel(tela,survivor,LevelAtual)
		Manager.primeiroDia = False #torna falso para nao exibir dia 1 mais de uma vez
	# ======================================================================
	# ======================= Game Over ===================================
	if playerHealth.healthAmount <= 0:
		som.stop()
		GameOver(tela,LevelAtual)
	# =====================================================================
	# ========== checa se o player alcancou o fim da fase =================
	if survivor.get_number() == 39:
		LevelAtual += 1
		nextLevel(tela,survivor,LevelAtual)
		survivor = Survivor(40,520)

		items.randomItems()
		enemyPoint.refreshSpawns()
		#zombie = Zombie()
		Zombie.Lista = []
		zombie1 = Zombie(Tile.get_tile(enemyPoint.sp1).x,Tile.get_tile(enemyPoint.sp1).y)
		if LevelAtual > 2:
			zombie2 = Zombie(Tile.get_tile(enemyPoint.sp2).x,Tile.get_tile(enemyPoint.sp2).y)
			if LevelAtual > 3:
				zombie3 = Zombie(Tile.get_tile(enemyPoint.sp3).x,Tile.get_tile(enemyPoint.sp3).y)
				if LevelAtual > 4:
					zombie4 = Zombie(Tile.get_tile(enemyPoint.sp4).x,Tile.get_tile(enemyPoint.sp4).y)
					if LevelAtual > 5 and Manager.gameMode == 'hard':
						zombie5 = Zombie(Tile.get_tile(enemyPoint.sp5).x,Tile.get_tile(enemyPoint.sp5).y)
						if LevelAtual > 6:
							zombie6 = Zombie(Tile.get_tile(enemyPoint.sp6).x,Tile.get_tile(enemyPoint.sp6).y)
							if LevelAtual > 7:
								zombie7 = Zombie(Tile.get_tile(enemyPoint.sp7).x,Tile.get_tile(enemyPoint.sp7).y)
					elif LevelAtual > 10 and Manager.gameMode == 'easy':
						zombie5 = Zombie(Tile.get_tile(enemyPoint.sp5).x,Tile.get_tile(enemyPoint.sp5).y)
						if LevelAtual > 12:
							zombie6 = Zombie(Tile.get_tile(enemyPoint.sp6).x,Tile.get_tile(enemyPoint.sp6).y)
							if LevelAtual > 14:
								zombie7 = Zombie(Tile.get_tile(enemyPoint.sp7).x,Tile.get_tile(enemyPoint.sp7).y)

	# =====================================================================
	# ================ torna nao andavel lugar onde tem zumbi ================
	if LevelAtual != 1:
		PosicaoDeZumbi(listaDeTiles)
	# ======================================================================

	tela.blit(ground,(0,0)) # fundo (terreno)

	Tile.draw_tiles(tela)   # desenha os tiles do cenario


	items.drawItem(tela)

	items.ColectSpawnItem(survivor)

	if displayRegen.displayFruit:
		regenFruit(tela)
	if displayRegen.displayDrink:
		regenDrink(tela)

	DisplayHitInfo(tela)
	# ================== sistema de trurnos ==================================
	if Manager.playerTurn:
		MovePlayer(survivor)
	else:
		#GetHit(survivor,tela)
		MoveZombie(survivor)
		if LevelAtual != 1:
			GetHit(survivor,tela)
	# =========================================================================

	# =============== zera as posicoes para atualiza-las =====================
	if LevelAtual != 1:
		AttPosicaoDeZumbi(listaDeTiles)
		listaDeTiles = []
	# =========================================================================

	# ======================== HUD =========================================
	if playerHealth.healthAmount >= 75:
		tonalidade = Color.LimeGreen
	elif playerHealth.healthAmount >= 50:
		tonalidade = Color.DarkOrange
	else:
		tonalidade = Color.Red

	text.ExibirTexto(tela,'Day '+str(LevelAtual),20,10,15)
	playerHealth.displayHealth(tela,tonalidade)
	# ======================================================================

	survivor.draw(tela) # desenha o sobrevivente

	# zumbis =========================
	if LevelAtual != 1:
		zombie1.draw(tela)
		if LevelAtual > 2:
			zombie2.draw(tela)
			if LevelAtual > 3:
				zombie3.draw(tela)
				if LevelAtual > 4:
					zombie4.draw(tela)
					if LevelAtual > 5 and Manager.gameMode == 'hard':
						zombie5.draw(tela)
						if LevelAtual > 6:
							zombie6.draw(tela)
							if LevelAtual > 7:
								zombie7.draw(tela)
					elif LevelAtual > 10 and Manager.gameMode == 'easy':
						zombie5.draw(tela)
						if LevelAtual > 12:
							zombie6.draw(tela)
							if LevelAtual > 14:
								zombie7.draw(tela)
	# ===================
	# ================================

	# ====================== inicia a musica de fundo ======================
	if audio == False:
		som.play(-1)
		audio = True
	# ======================================================================

	# fps counter ===============
	#pygame.display.set_caption('Scavengers - FPS %.2f' %(clock.get_fps()) )
	# ===========================

	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1
