import room

class Go:
    def __init__(self, s:list[str], r:room.Room) -> None:
        self.s:str = s
        self.r:room.Room = r
    def do(self)->int:
        s = self.s
        r = self.r
        cur = r.exits
        if len(s) == 1:
            print("Sorry, you need to 'go' somewhere.")
            return room.CURRENT
        arr = []
        dir = s[1]
        for direction in cur:
            if direction.startswith(dir): arr.append(direction)
        if len(arr) == 0:
            print(f"There's no way to go {dir}.")
            return room.CURRENT
        elif len(arr) == 1:
            print(f"You go {arr[0]}.\n")
            return cur[arr[0]]
        else:
            for direction in arr: # check the prefix is matched with whole string
                if direction == dir:
                    print(f"You go {direction}.\n")
                    return cur[direction]
            str = ""
            str += ", ".join(arr[:-1])
            str += f" or {arr[-1]}"
            print("Did you want to go " + str + "?")
        return room.CURRENT
    def help(self)->str:
        dirs = self.r.exits
        str = " or ".join(s for s in dirs.keys())
        return f"go {str}."
