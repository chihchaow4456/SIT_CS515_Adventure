import room
import json
import sys
import verbs.verb as verb

f = sys.argv[1]
j = json.load(open(f))

rooms = room.toRooms(j)
rooms[0].curPos()

stop = True
pos = 0
inventory = []

while stop and pos <= len(rooms):
    try:
        print('What would you like to do?', end = " ")
        s = list(map(str.lower,input('').split(' ')))  # text input and lower the str
        idx = verb.to(s, rooms, pos, inventory)
        if idx == room.CURRENT: continue
        elif idx == room.QUIT: stop = False
        else:
            pos = idx
            rooms[pos].curPos()
    except KeyboardInterrupt:
        print("\n Use 'quit' to exit.")
    except EOFError:
        print("\n Use 'quit' to exit.")
