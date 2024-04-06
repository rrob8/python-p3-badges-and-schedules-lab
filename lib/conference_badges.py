def badge_maker(name):
    badge = (f'Hello, my name is {name}.')
    return badge

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f'Hello, my name is {name}.')

    return badges

def assign_rooms(names):
    rooms = []
    i = 1
    for name in names:
        rooms.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i += 1
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    for name in badges:
        print (name)

    rooms = assign_rooms(names)
    for person in rooms:
        print (person)           
