class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category


shop = Store(name="GAP", category="clothes")
print(shop.name, shop.category)
