
class Warehouse:
    stock_name = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_name += 1

    def __del__(self):
        Warehouse.stock_name -= 1

user1 = Warehouse('kim')
user2 = Warehouse('lim')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)

print(Warehouse.__dict__)

print(user1.stock_name)
print(user2.stock_name)
print(Warehouse.stock_name)
