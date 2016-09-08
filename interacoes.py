import pygame, sys, text
from tile import Tile
from gameManager import PlayerHealth


def MovePlayer(tela, survivor, zombie):
	
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			
			zombieTile = zombie.get_number()

			if event.key == pygame.K_w:
				proxTile = survivor.get_number() - Tile.V
				PlayerHealth.healthAmount -= 1
			
				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.y -= survivor.altura

			elif event.key == pygame.K_s:
				proxTile = survivor.get_number() + Tile.V
				PlayerHealth.healthAmount -= 1

				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.y += survivor.altura
			
			elif event.key == pygame.K_a:
				proxTile = survivor.get_number() - Tile.H
				PlayerHealth.healthAmount -= 1

				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.x -= survivor.largura

			elif event.key == pygame.K_d:
				proxTile = survivor.get_number() + Tile.H
				PlayerHealth.healthAmount -= 1

				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.x += survivor.largura
