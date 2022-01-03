import json


class Product:
    def __init__(self, _Category, _ID, _Price, _Name, _Elements):
        self.ID = _ID
        self.Price = _Price
        self.Name = _Name
        self.Category = _Category
        self.Elements = _Elements

    def __str__(self):
        return "\nPrice: {}\nName: {}\nCategory: {}\nElements{}\n".format(self.Price, self.Name, self.Category, self.Elements)

    def SerializeJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Products:
    def __init__(self, values):
        self.MaxID = 0
        self.products = {}

        for idx, vls in values.items():
            if int(vls["ID"]) > self.MaxID:
                self.MaxID = int(vls["ID"])

            prod = Product(vls["Category"], vls["ID"], vls["Price"], vls["Name"], vls["Elements"])
            self.products[idx] = prod

    def __str__(self):
        string = ""

        for index, prod in self.products.items():
            string = string + str(index) + ": " + str(prod) + "\n"

        return string

    def maxID(self):
        return self.MaxID

    def AddProduct(self, values):
        self.MaxID += 1
        vls = Product(values[0], str(self.MaxID), values[1], values[2], values[3:])

        self.products[str(self.MaxID)] = vls
        out_file = open("Products.json", "w")

        json.dump(self.SerializeProducts(), out_file)

    def RemoveProduct(self, ID):
        ID = str(ID)

        if not self.CheckID(ID):
            print(f"No item with ID: {ID}")
            input("Continue:")
            return

        del self.products[ID]
        out_file = open("Products.json", "w")
        json.dump(self.SerializeProducts(), out_file)

        print("Item successfully removed")
        input("Continue: ")

    def CalculatePrice(self, itemsID):
        price = 0

        for itm_id in itemsID:
            price += int(self.products[itm_id].Price)

        return price

    def CheckID(self, ID):
        ID = str(ID)

        if ID not in self.products:
            return False
        else:
            return True

    def SerializeProducts(self):
        prod = {}

        for idx, vls in self.products.items():
            prod[idx] = json.loads(vls.SerializeJSON())

        return prod