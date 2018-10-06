import math
from helper import TileContent

def findCloseRessource(playerPosition, tiles):
    min = 200
    positionPlusProche = playerPosition
    for row in tiles:
        for col in row:
            if not col.TileContent == TileContent.Resource:
                continue
            pos = col.Position
            x = math.pow(pos - playerPosition[0], 2)
            y = math.pow(pos.y - playerPosition[1], 2)
            distance = math.sqrt(x + y)
            print(distance)
            if distance < min:
                min = distance
                positionPlusProche = pos
    return positionPlusProche