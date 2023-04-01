import room
from . import go, get, drop, common

def to(s: list[str], r: list[room.Room], pos: int, inventory: list):
    cmds = {
    'go': go.Go(s, r[pos]),
    'get': get.Get(s, r[pos], inventory),
    "drop": drop.Drop(s, r[pos], inventory),
    'look': common.Look(r[pos]),
    'inventory': common.Inventory(inventory),
    "quit": common.Quit(),
    }
    cmds["help"] = common.Help(cmds.values())
    return getAbbr(s, cmds)

def getAbbr(s: list[str], cmds):
    prefix = s[0]
    arr = []
    [arr.append(cmd) for cmd in cmds if cmd.startswith(prefix)]
    if len(arr) == 0: return room.CURRENT # do nothing when user inputs wrong cmds
    elif len(arr) == 1:
        if arr[0] in cmds:
            return cmds[arr[0]].do()
        return room.CURRENT
    str = ""
    str += ", ".join(arr[:-1])
    str += f" or the {arr[-1]}"
    print("Did you want to type the " + str + "?")
    return room.CURRENT