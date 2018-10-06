class Mapper:

    def __init__(self, gameMap):
        self._gameMap = gameMap
        self._dimensions = len(gameMap[0])

        self._map = []
        self.construireMap()

    def construireMap(self):
        for row in self._gameMap:
            buffer = []
            for col in row:
                if not bool(col):
                    buffer.append(0)
                if col == 6:
                    buffer.append("X")
                buffer.append(col[0])

            self._map.append(buffer)

    def afficher(self):
        for row in self._gameMap:
            for col in row:
                print(col, end='')
            print("")