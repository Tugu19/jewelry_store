import json

class Order:
    def __init__(self, _ID, _Products, _SurName, _FirstName, _Phone, _Address):
        self.Price = None
        self.ID = _ID
        self.Products = _Products
        self.SurName = _SurName
        self.FirstName = _FirstName
        self.Phone = _Phone
        self.Address = _Address

    def __str__(self):
        return "\nProducts: {}\nName: {} {}\nPhone: {}\nAddress: {}\n".format(self.Products, self.SurName, self.FirstName, self.Phone, self.Address)


    def SerializeJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Orders:
    def __init__(self, values):
        self.MaxID = 0
        self.orders = {}

        for idx, vls in values.items():
            if int(vls["ID"]) > self.MaxID:
                self.MaxID = int(vls["ID"])

            prod = Order(vls["ID"], vls["Products"], vls["SurName"], vls["FirstName"], vls["Phone"], vls["Address"])
            self.orders[idx] = prod

    def __str__(self):
        string = ""

        for index, prod in self.orders.items():
            string = string + str(index) + ": " + str(prod) + "\n"

        return string

    def maxID(self):
        return self.MaxID

    def AddOrder(self, values):
        self.MaxID += 1
        vls = Order(str(self.MaxID), values[0], values[1], values[2], values[3], values[4])

        self.orders[str(self.MaxID)] = vls
        out_file = open("Orders.json", "w")

        json.dump(self.SerializeOrders(), out_file)

    def RemoveOrder(self, ID):
        ID = str(ID)

        if not self.CheckID(ID):
            print(f"No item with ID: {ID}")
            input("Continue: ")
            return

        del self.orders[ID]
        out_file = open("Orders.json", "w")
        json.dump(self.orders, out_file)

        print("Item successfully removed")
        input("Continue: ")

    def CalculatePrice(self, itemsID):
        price = 0

        for itm_id in itemsID:
            price += int(self.orders[itm_id].Price)

        return price

    def CheckID(self, ID):
        ID = str(ID)

        if ID not in self.orders:
            print("No order has that ID")
            input("Continue: ")
            return False
        else:
            return True

    def SerializeOrders(self):
        prod = {}
        for idx, val in self.orders.items():
            prod[idx] = json.loads(val.SerializeJSON())
        return prod