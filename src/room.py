# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    def getRoomName(self):
        return self.name
    def getRoomDesc(self):
        return self.description
    def addItem(self, item):
        self.items.append(item)
    def checkForItems(self):
        if not not self.items:
            for item in self.items:
                itemInRoom = item.get_item()
                print('\n')
                print(f"You foud a {itemInRoom['name']} ({itemInRoom['description']})")
                print('\n')
            return self.items
        else:
            print('There are no items')
            return None
    def updateItems(self, newItems):
        self.items = newItems
    pass