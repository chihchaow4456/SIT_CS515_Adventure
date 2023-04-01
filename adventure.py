import room
import json
import sys
from verbs import verb

f = sys.argv[1]
j = json.load(open(f))

rooms = room.toRooms(j)
rooms[0].curPos()

stop = True
pos = 0
inventory = []

while stop and pos <= len(rooms):
    try:
        print('What would you like to do?', end = ' ')
        s = list(map(str.lower,input('').split(' ')))  # text input and lower the str
        idx = verb.to(s, rooms, pos, inventory)
        if idx == room.CURRENT: continue
        elif idx == room.QUIT: stop = False
        else:
            pos = idx
            rooms[pos].curPos()
    except KeyboardInterrupt:
        stop = False
    except EOFError:
        print("\nUse 'quit' to exit.")

