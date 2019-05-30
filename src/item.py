
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def get_item(self):
        return { "name": self.name, "description": self.description }
    def on_take(self, item):
        print(f"You have picked up {item['name']}")
        return