import json

class Category:
    def __init__(self, _ID, _Name, _Elements):
        self.Price = None
        self.ID = _ID
        self.Name = _Name
        self.Elements = _Elements

    def __str__(self):
        return "\nName: {}\nElements: {}\n".format(self.Name, self.Elements)


    def SerializeJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Categories:
    def __init__(self, values):
        self.MaxID = 0
        self.categories = {}

        for index, vls in values.items():
            if int(vls["ID"]) > self.MaxID:
                self.MaxID = int(vls["ID"])

            prod = Category(vls["ID"], vls["Name"], vls["Elements"])
            self.categories[index] = prod

    def __str__(self):
        string = ""

        for index, itm in self.categories.items():
            string = string + str(index) + ": " + str(itm) + "\n"

        return string

    def maxID(self):
        return self.MaxID

    def AddCategory(self, values):
        self.MaxID += 1
        vls = Category(str(self.MaxID), values[0], values[1:])

        self.categories[str(self.MaxID)] = vls
        out_file = open("Categories.json", "w")

        json.dump(self.SerializeCategories(), out_file)

    def RemoveCategory(self, ID):
        ID = str(ID)
        if not self.CheckID(ID):
            print(f"No category with ID: {ID}")
            input("Continue")
            return

        del self.categories[ID]
        out_file = open("Categories.json", "w")
        json.dump(self.SerializeCategories(), out_file)

        print("Item successfully removed")

    def CalculatePrice(self, itemsID):
        price = 0

        for itm_id in itemsID:
            price += int(self.categories[itm_id].Price)

        return price

    def CheckID(self, ID):
        ID = str(ID)
        if ID not in self.categories:
            return False
        else:
            return True

    def SerializeCategories(self):
        itm = {}

        for idx, val in self.categories.items():
            itm[idx] = json.loads(val.SerializeJSON())

        return itm

    def GetCategories(self):
        nameCategories = {}

        for idx, vls in self.categories:
            nameCategories[vls.SeializeJSON()["Name"]] = vls.SerializeJSON()

        return nameCategories