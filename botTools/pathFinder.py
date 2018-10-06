from botTools import dijsktra
from helper import Point

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
                graph.add_edge((x, y), (point.x, point.y), 1)

    visited, path = dijsktra.dijsktra(graph, (depart.x, depart.y))
    
    depart = (depart.x, depart.y)
    point = (arrivee.x, arrivee.y)
    avantDernier = None

    while point != depart:
        avantDernier = point
        point = path[point]
    
    return Point(avantDernier[0], avantDernier[1])
