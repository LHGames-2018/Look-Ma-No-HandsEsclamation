from helper import TileContent, aiHelper, Point
from botTools import pathFinder

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
        if self.PlayerInfo.CarriedResources / self.PlayerInfo.CarryingCapacity > 0.75:
            prochain, _ = pathFinder.getNextLocation(gameMap, self.PlayerInfo.Position, self.PlayerInfo.HouseLocation)
            deplacement = prochain - self.PlayerInfo.Position
            return getNextAction(gameMap.getTileAt(prochain), deplacement)
        else:
            distanceMin = 99999
            prochainProche = None
            for ressource in sortTiles(gameMap)[str(TileContent.Resource.value)]:
                prochain, valeur = pathFinder.getNextLocation(gameMap, self.PlayerInfo.Position, ressource)
                if valeur < distanceMin:
                    distanceMin = valeur
                    prochainProche = ressource

            if not prochainProche:
                return aiHelper.create_move_action(Point(0, 1))

            prochain, valeur = pathFinder.getNextLocation(gameMap, self.PlayerInfo.Position, prochainProche)
            deplacement = prochain - self.PlayerInfo.Position
            return getNextAction(gameMap.getTileAt(prochain), deplacement)

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

def getNextAction(tileType, deplacement):
    if tileType == TileContent.Resource:
        return aiHelper.create_collect_action(deplacement)
    elif tileType == TileContent.Wall or tileType == TileContent.Player:
        return aiHelper.create_attack_action(deplacement)
    else:
        return aiHelper.create_move_action(deplacement)
