from room import Room
from player import Player
from item import Item
import random
# Declare all the rooms

items = [
    Item("rock", "This is just a rock"),
    Item("sword", "Known as 'Excalibur"),
    Item("flashlight", "Does not have batteries..."),
    Item("batteries", "Can be put into a flashlight")
]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room_keys = list(room.keys())
for item in items:
    ran_int = random.randint(1, 3)
    room[room_keys[ran_int]].addItem(item)
    


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player1 = Player(room['outside'])
print(f"Location: {player1.room.getRoomName()}")
print(f"This is what you see {player1.room.getRoomDesc()}")
player1.room.checkForItems()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    new_direction = input("Nice work, move to another room (n, s, e, w) ")
    if new_direction.strip() in ['n', 's', 'w', 'e']:
        player1.moveToRoom(new_direction)
    elif new_direction.strip().startswith('drop'):
        player1.handleItemDrop(new_direction.split(' ')[1])
    elif new_direction.strip() in ['i', 'inventory']:
        player1.getInventory()
    else:
        print('please only type "n", "s", "e", or "w"')
    pass