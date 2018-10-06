from helper import *
import queue
from botTools import pathFinder
from helper import TileContent

class Bot:
    def __init__(self):
        self._killedPlayers = []
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        positionJoueur = self.PlayerInfo.Position

        positionCible = Point(positionJoueur.x + 5, positionJoueur.y + 5)

        try:
            ennemy = visiblePlayers[0]
            if distanceCheck(positionJoueur, ennemy.Position):
                positionCible = ennemy.Position
        except:
            ennemy = False


        showMap(gameMap)
        print(positionJoueur)
        print(positionCible)

        nextStep = pathFinder.getNextLocation(gameMap, positionJoueur, positionCible)
        direction = Point(nextStep.x - positionJoueur.x, nextStep.y - positionJoueur.y)

        prochaineTuile = gameMap.getTileAt(nextStep)

        print(prochaineTuile)
        print(direction)

        if prochaineTuile == TileContent.Wall or prochaineTuile == TileContent.Player:
            return create_attack_action(direction)

        return create_move_action(direction)

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

def showMap(gameMap):
    for y in range(gameMap.yMin, gameMap.yMax):
        line = ""
        for x in range(gameMap.xMin, gameMap.xMax):
            line += str(gameMap.getTileAt(Point(x, y)).value) + " "
        print(line)

def distanceCheck(joueur, p2):
    return abs(joueur.x - p2.x) <= 10 and abs(joueur.y - p2.y) <= 10

def sortTiles(gameMap):
    sortedTiles = {}
    for y in range(gameMap.yMin, gameMap.yMax):
        for x in range(gameMap.xMin, gameMap.xMax):
            tileType = str(gameMap.getTileAt(Point(x, y)).value)
            if sortedTiles.get(tileType):
                sortedTiles[tileType].append(Point(x, y))
            else:
                sortedTiles[tileType] = [Point(x, y)]
    return sortedTiles