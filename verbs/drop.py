import room
from . import common

class Drop:
    def __init__(self, s:list[str], r: room.Room, inventory: list[str]):
        self.s = s
        self.r = r
        self.inventory = inventory
    def do(self):
        if len(self.inventory) == 0:
            print("You don't have anything to drop.")
            return room.CURRENT
        name = self.s[1]
        return common.GetOrDrop(name, self.inventory, self.r.items, False)
    def help(self)->str:
        items = self.inventory
        str = " or ".join(s for s in items)
        return f"drop {str}"