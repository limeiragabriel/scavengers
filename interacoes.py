import pygame, sys, text,random,os
from tile import Tile
from gameManager import PlayerHealth
from gameManager import Gerenciador,DisplayDamage
from charactersC import Zombie

pygame.mixer.init()

#=================playe sounds =========================================
footsteps = os.path.join('sounds','footstep2.aif')
PlayerFootsteps = pygame.mixer.Sound(footsteps)
PlayerFootsteps.set_volume(0.3)

playerHit = os.path.join('sounds','hit.aif')
playerDamage = pygame.mixer.Sound(playerHit)
playerDamage.set_volume(0.5)
#=======================================================================

# ================ zombieSounds ===========================================
zombieSound = os.path.join('sounds','enemy.aif')
somZumbi = pygame.mixer.Sound(zombieSound)
somZumbi.set_volume(0.5)

zombiefootstep = os.path.join('sounds','footstep1.aif')
footstepsZombie = pygame.mixer.Sound(zombiefootstep)
footstepsZombie.set_volume(0.3)
#==========================================================================

# ================= movimentacao do personagem =======================
def MovePlayer(survivor):

	global PlayerFootsteps

	# ============ eventos do teclado =================================
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN: #se alguma tecla for pressionada
			# ======================= tecla W ==========================
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				proxTile = survivor.get_number() - Tile.V
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				PlayerFootsteps.play(0)

				# ========= ao tentar realizar movimento o turno muda =====
				Gerenciador.playerTurn = False

				# ================== mover para cima =========================
				if Tile.get_tile(proxTile).walkable:
					survivor.y -= survivor.altura
			# ============================================================

			# ======================= tecla S ==========================
			elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
				proxTile = survivor.get_number() + Tile.V
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				PlayerFootsteps.play(0)

				# ========= ao tentar realizar movimento o turno muda =====
				Gerenciador.playerTurn = False

				# ================== mover para baixo =========================
				if Tile.get_tile(proxTile).walkable:
					survivor.y += survivor.altura
				# ============================================================

			# ======================= tecla A ==========================
			elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
				proxTile = survivor.get_number() - Tile.H
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				PlayerFootsteps.play(0)

				# ========= ao tentar realizar movimento o turno muda =====
				Gerenciador.playerTurn = False

				# ================== mover para besquerda ====================
				if Tile.get_tile(proxTile).walkable:
					survivor.x -= survivor.largura
				# ============================================================

			# ======================= tecla D ==========================
			elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				proxTile = survivor.get_number() + Tile.H
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				PlayerFootsteps.play(0)

				# ========= ao tentar realizar movimento o turno muda =====
				Gerenciador.playerTurn = False
				# ================== mover para direita ====================
				if Tile.get_tile(proxTile).walkable:
					survivor.x += survivor.largura
				# ============================================================
	# ============================================================================

# ============== verifica se player esta proxim ao zumbi e deve tomar dano ===========================
a = 0
b = 0
largura = 4000
altura = 600
frame = 0.0

def GetHit(survivor,tela):
	global a,b,largura,altura,frame,playerDamage,somZumbi
	# ====== tiles ao redor do player =================================================================
	U_Tile = survivor.get_number() - Tile.V #Tile superior
	D_Tile = survivor.get_number() + Tile.V #Tile inferior
	L_Tile = survivor.get_number() - Tile.H #Tile Lateral Esquerda
	R_Tile = survivor.get_number() + Tile.H #Tile Lateral Direita
	# =================================================================================================

	# ========================= checa se ha zumbis ao redor do player =================================
	for zombie in Zombie.Lista:

		if (U_Tile == zombie.get_number()) or (D_Tile == zombie.get_number()) or (L_Tile == zombie.get_number()) or (R_Tile == zombie.get_number()):
			if Gerenciador.gameMode == 'easy':
				PlayerHealth.healthAmount -= 10
			else:
				PlayerHealth.healthAmount -= 30
			DisplayDamage.enemyHit = True

			playerDamage.play(0)
			somZumbi.play(0)

			caminho = os.path.join('tileset','bloodblur.png')

			if frame >= 1.0:
				a += 800
				frame = 0.0

			frame += 0.1

			if a >= (800 * 5):
				a = 0

			blur = pygame.image.load(caminho).convert_alpha()
			tela.blit(blur,(0, 0),(a,b,largura,altura))

	# ==================================================================================================
# ======================================================================================================

def MoveZombie(survivor):
	global footstepsZombie

	for zombie in Zombie.Lista:

		move = random.randint(0,1)

		if move == 0:
			Gerenciador.playerTurn = True

		else:

			direction = random.randint(0,3)

			U_Tile = zombie.get_number() - Tile.V #Tile superior
			D_Tile = zombie.get_number() + Tile.V #Tile inferior
			L_Tile = zombie.get_number() - Tile.H #Tile Lateral Esquerda
			R_Tile = zombie.get_number() + Tile.H #Tile Lateral Direita

			tiledoplayer = survivor.get_number()  #Tile onde o player esta

			if direction == 0:

				proxTile = zombie.get_number() - Tile.V

				if Tile.get_tile(proxTile).walkable and proxTile != tiledoplayer:
					zombie.y -= zombie.altura

					footstepsZombie.play(0)

			elif direction == 1:

				proxTile = zombie.get_number() + Tile.V

				if Tile.get_tile(proxTile).walkable and proxTile != tiledoplayer:
					zombie.y += zombie.altura

					footstepsZombie.play(0)

			elif direction == 2:

				proxTile = zombie.get_number() - Tile.H

				if Tile.get_tile(proxTile).walkable and proxTile != tiledoplayer:
					zombie.x -= zombie.largura

					footstepsZombie.play(0)

			elif direction == 3:

				proxTile = zombie.get_number() + Tile.H

				if Tile.get_tile(proxTile).walkable and proxTile != tiledoplayer:
					zombie.x += zombie.largura

					footstepsZombie.play(0)

			Gerenciador.playerTurn = True
