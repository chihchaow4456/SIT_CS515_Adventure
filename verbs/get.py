import room
from . import common

class Get:
    def __init__(self, s:list[str], r:room.Room, inventory: list[str]) -> None:
        self.s:str = s
        self.r:room.Room = r
        self.inventory:int = inventory
    def do(self)->int:
        if len(self.s) == 1:
            print("Sorry, you need to 'get' something.")
            return room.CURRENT
        if len(self.r.items) == 0:
            print(f"There's no {self.s[1]} anywhere.")
            return room.CURRENT
        name = self.s[1]
        return common.GetOrDrop(name, self.r.items, self.inventory, True)
    def help(self)->str:
        items = self.r.items
        str = " or ".join(s for s in items)
        return f"get {str}"