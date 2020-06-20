from map_objects.map_objects import Tile
from map_objects.rectangle import Rect


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [
            [Tile(True) for y in range(self.height)] for x in range(self.width)
        ]

        return tiles

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    def intersect(self, other):
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )

    def make_map(self):
        room1 = Rect(20, 15, 10, 15)
        room2 = Rect(35, 15, 10, 15)

        self.create_room(room1)
        self.create_room(room2)

        self.create_h_tunnel(25, 40, 23)

    def create_room(self, room):
        for x, y in room.blocks():
            tile = self.tiles[x][y]
            tile.blocked = False
            tile.block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            tile = self.tiles[x][y]
            tile.blocked = False
            tile.block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            tile = self.tiles[x][y]
            tile.blocked = False
            tile.block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
