CURRENT = -1
QUIT = -2

class Direction:
    north:int = None
    east:int = None
    west:int = None
    south:int = None
    northwest:int = None
    northeast:int = None
    southwest:int = None
    southeast:int = None

class Room:
    name:str = ""
    desc:str = ""
    exits:Direction = { Direction }
    items:list = []
    idx:int = 0
    locked:bool = False
    def __init__(self, name, desc = "", exits = {Direction}, items = [], idx = 0):
        self.name = name
        self.desc = desc
        self.exits = [] if exits is None else exits
        self.items = [] if items is None else items
        self.idx = idx
        self.locked = False
    def curPos(self):
        print(f"{self.name}\n\n{self.desc}\n")
        if self.items != None and len(self.items) != 0:
            print('Items: ', end = "")
            print(", ".join(self.items))  # rose, light
            print("")
        if self.exits != None and len(self.exits) != 0:
            print('Exits: ', end = "")
            for exit in self.exits: print(exit, end= " ")
            print("\n")

def toRooms(json: str) -> list[Room]:
        rooms = []
        idx = 0
        for obj in json:
          name = obj.get('name')
          desc = obj.get('desc')
          exits = obj.get('exits')
          items = obj.get('items')
          rooms.append(Room(name, desc, exits, items, idx))
          idx += 1
        return rooms