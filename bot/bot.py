from helper import *
from helper import TileContent
class Bot:
    def __init__(self):
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
        positionAdjacente = Point(positionJoueur.x + 1, positionJoueur.y)
        direction = Point(0, 0)
        action = create_move_action(Point(1, 0))

        if gameMap.getTileAt(positionAdjacente) == TileContent.Resource or gameMap.getTileAt(positionAdjacente) == TileContent.House or gameMap.getTileAt(positionAdjacente) == TileContent.Shop:
            action = create_move_action(Point(0, 1))


        if len(visiblePlayers) > 0:
            ennemy = visiblePlayers[0]
            diffx = ennemy.Position.x - positionJoueur.x
            diffy = ennemy.Position.y - positionJoueur.y
            if diffx > diffy:
                action = create_move_action(Point(1, 0))
                direction = Point(1, 0)
            else:
                action = create_move_action(Point(0, 1))
                direction = Point(0, 1)

            if diffy + diffx == 1:

                if diffx == 1:
                    action = create_attack_action(Point(diffx, 0))
                if diffy == 1:
                    action = create_attack_action(Point(0, diffy))

        if gameMap.getTileAt(Point(positionJoueur.x + direction.x, positionJoueur.y + direction.y)) == TileContent.Wall:
            action = create_attack_action(direction)

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