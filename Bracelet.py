from Products import Product


class Bracelet(Product):
    def __init__(self, _Color, _Material, _Weight, _Category, _ID, _Price, _Name, _Elements):
        super().__init__(_Category, _ID, _Price, _Name, _Elements)
        self.Color = _Color
        self.Material = _Material
        self.Weight = _Weight
