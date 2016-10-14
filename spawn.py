import pygame,random,os
from tile import Tile
from charactersC import *
from gameManager import PlayerHealth

itemSpawnList = [46,50,54,106,110,114,166,170,174,226,230,234]
spawnTiles = []

class SpawnPoint():

    def makeSpawns(self):
        for tile in Tile.Lista:
            if tile.number in itemSpawnList:
                tile.isItemSpawn = True
                spawnTiles.append(tile)

    def randomItems(self):
        for tile in spawnTiles:
            tile.itemType = random.randint(0,4)

    def drawItem(self,tela):
        drinksprite = os.path.join('tileset','drink.png')
        drink = pygame.image.load(drinksprite).convert_alpha()

        fruitsprite = os.path.join('tileset','fruits.png')
        fruit = pygame.image.load(fruitsprite).convert_alpha()
        for tile in spawnTiles:
            if tile.itemType > 1:
                pass
            elif tile.itemType == 0:
                tela.blit(fruit,tile)
            elif tile.itemType == 1:
                tela.blit(drink,tile)

    def ColectSpawnItem(self,player):
        for tile in spawnTiles:
            if player.get_number() == tile.number:
                if tile.itemType > 1:
                    pass
                elif tile.itemType == 0:
                    tile.itemType = 2
                    PlayerHealth.healthAmount += 5
                elif tile.itemType == 1:
                    tile.itemType = 2
                    PlayerHealth.healthAmount += 10
