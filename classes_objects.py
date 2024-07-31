class Store:
    def __init__(self, name):
        self.name = name
        self.items = list()
    
    def add_item(self, name, price):
        itemdict = {
            "name" : name,
            "price" : price
        }
        self.items.append(itemdict)

    def stock_price(self):
        return sum(item["price"] for item in self.items)


# Example usage:
store = Store("My Store")
store.add_item("Apple", 1.0)
store.add_item("Banana", 1.5)
store.add_item("Orange", 2.0)