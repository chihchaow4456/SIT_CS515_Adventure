import room
class Help:
    def __init__(self, cmds: dict):
        self.cmds = cmds
    def do(self):
        print("You can run the following commands:")
        for cmd in self.cmds:
            print("  " + cmd.help())
        return room.CURRENT
    def help(self):
        return "help"

class Look:
    def __init__(self, r:room.Room):
        self.r = r
    def do(self)->int:
        self.r.curPos()
        return room.CURRENT
    def help(self):
        return "look"

class Inventory:
    def __init__(self, inventory:list[str]):
        self.inventory = inventory
    def do(self)->int:
        if len(self.inventory) == 0:
            print("You're not carrying anything.")
            return room.CURRENT
        print("Inventory:")
        for item in self.inventory: print(f"  {item}")
        return room.CURRENT
    def help(self)->str:
        return "inventory"

class Quit:
    def __init__(self):
        pass
    def do(self)->int:
        print("Goodbye!")
        return room.QUIT
    def help(self)->str:
        return "quit"
    
def GetOrDrop(name:str, items:list[str], backpack:list[str], isGet: True)->int:
    arr = []
    for item in items:
        if name in item: arr.append(item)
    if len(arr) == 0:
        print(f"There's no {name} anywhere.")
        return room.CURRENT
    elif len(arr) == 1:
        for i, item in enumerate(items):
            if item == arr[0]:
                backpack.append(item)
                items.pop(i)
        if isGet: print(f"You pick up the {arr[0]}.")
        else: print(f"You drop the {arr[0]}.")
    else:
        str = ""
        str += ", ".join(arr[:-1])
        str += f" or the {arr[-1]}"
        print("Did you want to get the " + str + "?")
    return room.CURRENT
