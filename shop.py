import copy


class Shop:
    def __init__(self, *items):
        self.stock = list(items)

    def list_items(self):
        output = 'In stock:\n'
        for item in self.stock:
            if item.amount > 0:
                output += f'{item.name}: {item.amount}\n'
        return output

    def buy(self, item_name, amount=1):
        for item in self.stock:
            if item_name == item.name:
                item.decrease_amount(amount)
                break
        else:
            raise ValueError('No such item in stock')

        item_copy = copy.deepcopy(item)
        item_copy.set_amount(amount)
        return item_copy

    def sell(self, item, amount=1):
        item.decrease_amount(amount)
        for stock_item in self.stock:
            if stock_item.name == item.name:
                stock_item.increase_amount(amount)
                break
        else:
            item_copy = copy.deepcopy(item)
            item_copy.set_amount(amount)
            self.stock.append(item_copy)


class Item:
    def __init__(self, name, amount=1, rarity='common'):
        self.name = name
        self.amount = amount
        self.rarity = rarity

    def set_amount(self, value):
        if value < 0:
            raise ValueError('Value can not be negative')
        self.amount = value

    def decrease_amount(self, value=1):
        if self.amount - value >= 0:
            self.amount -= value
        else:
            raise ValueError('Item amount can not be negative')

    def increase_amount(self, value=1):
        if value < 0:
            raise ValueError('Value can not be negative')
        self.amount += value


shop = Shop(Item('Shovel', 1), Item('Carrot seeds', 10))
print(shop.list_items())
bought_item = shop.buy('Carrot seeds', 7)
print(f"Bought items: {bought_item.name}: {bought_item.amount}")
shop.sell(Item('Hoe', 1), 1)
print(shop.list_items())
