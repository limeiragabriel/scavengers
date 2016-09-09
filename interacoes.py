import pygame, sys, text,random
from tile import Tile
from gameManager import PlayerHealth
from charactersC import Zombie

# ================= movimentacao do personagem =======================
def MovePlayer(survivor):

	# ============ eventos do teclado =================================
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN: #se alguma tecla for pressionada
			# ======================= tecla W ==========================
			if event.key == pygame.K_w:
				proxTile = survivor.get_number() - Tile.V
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para cima ========================= 
				if Tile.get_tile(proxTile).walkable:
					survivor.y -= survivor.altura
			# ============================================================

			# ======================= tecla S ==========================
			elif event.key == pygame.K_s:
				proxTile = survivor.get_number() + Tile.V
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para baixo =========================
				if Tile.get_tile(proxTile).walkable:
					survivor.y += survivor.altura
				# ============================================================

			# ======================= tecla A ==========================
			elif event.key == pygame.K_a:
				proxTile = survivor.get_number() - Tile.H
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para besquerda ====================
				if Tile.get_tile(proxTile).walkable:
					survivor.x -= survivor.largura
				# ============================================================

			# ======================= tecla D ==========================
			elif event.key == pygame.K_d:
				proxTile = survivor.get_number() + Tile.H
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para direita ====================
				if Tile.get_tile(proxTile).walkable:
					survivor.x += survivor.largura
				# ============================================================
	# ============================================================================

# ============== verifica se player esta proxim ao zumbi e deve tomar dano ===========================
def GetHit(survivor):

	# ====== tiles ao redor do player =================================================================
	U_Tile = survivor.get_number() - Tile.V #Tile superior
	D_Tile = survivor.get_number() + Tile.V #Tile inferior
	L_Tile = survivor.get_number() - Tile.H #Tile Lateral Esquerda
	R_Tile = survivor.get_number() + Tile.H #Tile Lateral Direita
	# =================================================================================================

	# ========================= checa se ha zumbis ao redor do player =================================
	for zombie in Zombie.Lista:

		if (U_Tile == zombie.get_number()) or (D_Tile == zombie.get_number()) or (L_Tile == zombie.get_number()) or (R_Tile == zombie.get_number()):
			return True
	# ==================================================================================================
# ======================================================================================================

def MoveZombie():

	for zombie in Zombie.Lista:

		move = random.randint(0,1)
		direction = random.randint(0,3)

		U_Tile = zombie.get_number() - Tile.V #Tile superior
		D_Tile = zombie.get_number() + Tile.V #Tile inferior
		L_Tile = zombie.get_number() - Tile.H #Tile Lateral Esquerda
		R_Tile = zombie.get_number() + Tile.H #Tile Lateral Direita

		if move == 0:
			pass
		else:
			if direction == 0:
				
				proxTile = zombie.get_number() - Tile.V

				if Tile.get_tile(proxTile).walkable:
					zombie.y -= zombie.altura

			elif direction == 1:
				
				proxTile = zombie.get_number() + Tile.V

				if Tile.get_tile(proxTile).walkable:
					zombie.y += zombie.altura

			elif direction == 2:
				
				proxTile = zombie.get_number() - Tile.H

				if Tile.get_tile(proxTile).walkable:
					zombie.x -= zombie.largura

			elif direction == 3:
				
				proxTile = zombie.get_number() + Tile.H

				if Tile.get_tile(proxTile).walkable:
					zombie.x += zombie.largura





