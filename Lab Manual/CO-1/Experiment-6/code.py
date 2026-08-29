room = {'A':'Dirty', 'B':'Dirty'}
pos = 'A'

while 'Dirty' in room.values():
    print("Vacuum at", pos)

    if room[pos] == 'Dirty':
        room[pos] = 'Clean'
        print("Cleaning", pos)
    else:
        pos = 'B' if pos == 'A' else 'A'

print("Both rooms are clean")
