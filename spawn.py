import pygame,random,os,text
from tile import Tile
from charactersC import *
from gameManager import PlayerHealth,LifeRegen

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
                    PlayerHealth.healthAmount += 10
                    LifeRegen.displayFruit = True
                    #text.ExibirTexto(tela,'+ 10',200,10,15)
                elif tile.itemType == 1:
                    tile.itemType = 2
                    PlayerHealth.healthAmount += 15
                    LifeRegen.displayDrink = True
                    #text.ExibirTexto(tela,'+ 20',200,10,15)

enemySpawnList = [66,104,108,74,112,116,184,206,188,192,214,196,70,150,210,26,34]

class EnemySPoint():
    sp1 = enemySpawnList[random.randint(0,2)]
    sp2 = enemySpawnList[random.randint(3,5)]
    sp3 = enemySpawnList[random.randint(6,8)]
    sp4 = enemySpawnList[random.randint(9,11)]
    sp5 = enemySpawnList[random.randint(12,14)]
    sp6 = enemySpawnList[15]
    sp7 = enemySpawnList[16]

    def refreshSpawns(self):
        self.sp1 = enemySpawnList[random.randint(0,2)]
        self.sp2 = enemySpawnList[random.randint(3,5)]
        self.sp3 = enemySpawnList[random.randint(6,8)]
        self.sp4 = enemySpawnList[random.randint(9,11)]
        self.sp5 = enemySpawnList[random.randint(12,14)]
