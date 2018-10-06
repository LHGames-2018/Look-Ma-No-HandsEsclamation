from helper import *
from botTools.proximityFinder import findCloseRessource


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


        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        afficherMap(gameMap)
        print(self.PlayerInfo)
        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

def afficherMap(gameMap):
    for row in reversed(gameMap.tiles):
        line = ""
        for tile in row:
            line += str(tile.TileContent.value) + " "
        print(line)
