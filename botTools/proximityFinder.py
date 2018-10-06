import math
from helper import Point


class ProximityFinder:

    @staticmethod
    def findClosestTile(playerPosition, tiles):

        """

        Retourne la position de la tuile la plus proche du personnage

        :param playerPosition: position du joueur
        :param tiles: une liste des tuiles de meme type
        :return: la position de la tuile la plus proche dans cette liste

        """

        positionTuileProche = {}
        distanceMin = 20000
        for tuile in tiles:
            x = math.pow(tuile.x - playerPosition.x, 2)
            y = pow(tuile.y - playerPosition.y, 2)
            distance = math.sqrt(x + y)

            if distance < distanceMin:
                positionTuileProche = Point(tuile.x, tuile.y)
                distanceMin = distance

        return positionTuileProche
