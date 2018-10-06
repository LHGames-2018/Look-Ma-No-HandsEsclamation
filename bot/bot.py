from helper import *
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

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        # showMap(gameMap)
        # prochain = pathFinder.getNextLocation(gameMap, self.PlayerInfo.Position, sortTiles(gameMap)[str(TileContent.Resource.value)][0])
        # deplacement = prochain - self.PlayerInfo.Position
        # return create_move_action(deplacement)

        positionJoueur = self.PlayerInfo.Position
        direction = Point(1, 0)
        positionAdjacente = Point(positionJoueur.x + direction.x, positionJoueur.y + direction.y)
        prochaineTuile = gameMap.getTileAt(positionAdjacente)

        action = create_move_action(direction)

        ennemy = False
        try:
            for mechan in visiblePlayers:
                ennemy = mechan
                if ennemy.Name in self._killedPlayers:
                    ennemy = False
        except:
            ennemy = False

        if ennemy:
            diffx = ennemy.Position.x - positionJoueur.x
            diffy = ennemy.Position.y - positionJoueur.y
            if diffx > diffy:
                direction = Point(1, 0)
                positionAdjacente = Point(positionJoueur.x + direction.x, positionJoueur.y + direction.y)
                prochaineTuile = gameMap.getTileAt(positionAdjacente)
            else:
                direction = Point(0, 1)
                positionAdjacente = Point(positionJoueur.x + direction.x, positionJoueur.y + direction.y)
                prochaineTuile = gameMap.getTileAt(positionAdjacente)

            action = create_move_action(direction)

            if diffy + diffx == 1:
                self._killedPlayers.append(ennemy)
                if diffx == 1:
                    action = create_attack_action(Point(diffx, 0))
                if diffy == 1:
                    action = create_attack_action(Point(0, diffy))
                if ennemy.Health <= 2:
                    self._killedPlayers.append(ennemy.Name)

        if prochaineTuile == TileContent.House or prochaineTuile == TileContent.Shop or prochaineTuile == TileContent.Resource:
            direction = Point(direction.y, direction.x)
            positionAdjacente = Point(positionJoueur.x + direction.x, positionJoueur.y + direction.y)
            prochaineTuile = gameMap.getTileAt(positionAdjacente)
            action = create_move_action(direction)

        if prochaineTuile == TileContent.Wall or prochaineTuile == TileContent.Player:
            action = create_attack_action(direction)

        print(prochaineTuile)

        return action

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