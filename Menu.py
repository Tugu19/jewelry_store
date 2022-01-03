import json
import os
from Orders import Orders
from Products import Products
from Categories import Categories


class Menu:
    menus = {1: "AddCategory", 2: "RemoveCategory", 3: "DisplayCategory", 4: "AddProduct", 5: "RemoveProduct",
             6: "DisplayProducts", 7: "PlaceOrder", 8: "DisplayOrders"}

    def __init__(self):
        file = open('Products.json')
        dataProducts = json.load(file)
        file = open('Orders.json')
        dataOrders = json.load(file)
        file = open('Categories.json')
        dataCategories = json.load(file)

        self.products = Products(dataProducts)
        self.orders = Orders(dataOrders)
        self.categories = Categories(dataCategories)

    def AddCategory(self):
        items = input("Please write the name of the category and its specifics\n (e.g.Ring Material Weight)\n")
        self.categories.AddCategory(items.split(" "))
        print("\n")

    def DisplayCategory(self):
        print(self.categories)
        input("Continue: ")

    def RemoveCategory(self):
        print(self.categories)
        try:
            id_remove = int(input("Please enter the ID of the Category you want removed: "))
        except:
            print("Invalid integer")
            return
        self.categories.RemoveCategory(id_remove)

    def PlaceOrder(self):
        items = input(""" 
What Products do you wish to buy?

"""
                      + str(self.products) +
                      """
Please write the IDs of the products one by another:
"""
                      )
        items = items.split(" ")
        for i in items:
            if not self.products.CheckID(i):
                print("There is no item with ID {}".format(i))
                return
        price = self.products.CalculatePrice(items)
        userData = input("""
Total price: {}
If you want to cancel the order type 'exit'
If you want to continue, enter your Name, Surname and phone number
""".format(price))

        if userData == "exit":
            return

        address = input("Please enter the address: ")

        self.orders.AddOrder([items, *userData.split(" "), address])

    def DisplayOrders(self):
        print(self.orders)
        input("Continue: ")

    def AddProduct(self):
        allCategories = self.categories.SerializeCategories()
        allCategoriesString = ""
        for idx, category in allCategories.items():
            allCategoriesString = allCategoriesString + str(idx) + ": " + category["Name"] + "\n"
        try:
            prod = int(input("What kind of product do you wish to add?\n" + allCategoriesString))
            prod = str(prod)
            if not self.categories.CheckID(prod):
                print("No category has this ID")
                input("Continue: ")
                return
        except:
            return
        Type = allCategories[prod]["Name"]
        string = input("Please specify the Price, Name, " + ", ".join(allCategories[prod]["Elements"]) + "\n")
        if string.split(" ") == 2 + len(allCategories[prod]["Elements"]):
            print("Invalid syntax")
            input("Continue: ")
            return

        self.products.AddProduct([Type, *string.split(" ")])

    def DisplayProducts(self):
        print(self.products)
        input("Continue: ")

    def RemoveProduct(self):
        print(self.products)
        try:
            prd_id = int(input("Please enter the ID of the product you want removed: "))
            prd_id = str(prd_id)
        except:
            print("Invalid integer")
            input("Continue")
            return
        self.products.RemoveProduct(prd_id)

    def StartMenu(self):
        while True:
            os.system('cls')
            print("""Welcome to Emerald Store!
Choose an option
 
1: Add Category
2: Remove Category
3: Display Category
4: Add Product
5: Remove Product
6: Display Products
7: Place Order
8: Display Orders
9: Exit Store
            """
                  )
            try:
                option = int(input("Your option is: "))
                if option > 9 or option < 1:
                    continue
            except:
                continue

            if option == 9:
                break
            else:
                method = getattr(self, self.menus[option])
                method()


menu = Menu()
menu.StartMenu()
