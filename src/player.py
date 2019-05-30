# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
        self.inventory = []

    def moveToRoom(self, direction):
        if hasattr(self.room, 'n_to') and direction == 'n':
            self.room = self.room.n_to
        elif hasattr(self.room, 's_to') and direction == 's':
            self.room = self.room.s_to
        elif hasattr(self.room, 'e_to') and direction == 'e':
            self.room = self.room.e_to
        elif hasattr(self.room, 'w_to') and direction == 'w':
            self.room = self.room.w_to
        else:
            print('Sorry, that is a dead end... pick another direction')
            print('\n')
            return
        print(f"Location: {self.room.getRoomName()}")
        print(f"This is what you see {self.room.getRoomDesc()}")
        items_found = self.room.checkForItems()
        if not items_found:
            return
        self.putItemInInventory(items_found)

    def putItemInInventory(self, items):
        while not not items:
            choice = input("Select items you want to pick-up (example: 'get sword', type 'no' to exit) ")
            if choice == 'no':
                return
            choice_arr = choice.split(" ")
            if choice_arr[0] == 'get':
                for item in items:
                    if item['name'] == choice_arr[1]:
                        self.inventory.append(item)
                        items.remove(item)
                        self.room.updateItems(items)
                    else:
                        print('There is no item by that name')
            else:
                print('You can only use a get action right now')


    