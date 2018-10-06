from botTools import dijsktra
from helper import Point, TileContent

def getNextLocation(gameMap, depart, arrivee):
    graph = dijsktra.Graph()

    for y in range(gameMap.yMin, gameMap.yMax):
        for x in range(gameMap.xMin, gameMap.xMax):
            graph.add_node((x, y))

            pointsAdjacents = []
            pointsAdjacents.append(Point(x - 1, y))
            pointsAdjacents.append(Point(x + 1, y))
            pointsAdjacents.append(Point(x, y - 1))
            pointsAdjacents.append(Point(x, y + 1))

            for point in pointsAdjacents:
                valeur = 1
                if gameMap.getTileAt(point) == TileContent.Lava:
                    valeur = 999
                elif gameMap.getTileAt(point) == TileContent.Wall:
                    valeur = 3
                elif gameMap.getTileAt(point) == TileContent.House:
                    valeur = 700
                elif gameMap.getTileAt(point) == TileContent.Shop:
                    valeur = 600
                elif gameMap.getTileAt(point) == TileContent.Resource:
                    valeur = 500
                
                graph.add_edge((x, y), (point.x, point.y), valeur)

    distances, path = dijsktra.dijsktra(graph, (depart.x, depart.y))
    
    ptDepart = (depart.x, depart.y)
    point = (arrivee.x, arrivee.y)
    avantDernier = point

    if depart == point:
        return depart, 0

    while point != ptDepart:
        avantDernier = point
        point = path[point]

    return Point(avantDernier[0], avantDernier[1]), distances[(arrivee.x, arrivee.y)]
