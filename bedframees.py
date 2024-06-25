class Bed:
    def __init__(self, color, material):
        self.__color = color
        self.__material = material
    
    def set_color(self, color):
        self.__color = color

    def set_material(self, material):
        self.__material = material

    def get_color(self):
        return self.__color

    def get_material(self):
        return self.__material
    
    def display(self):
        print(f"Bed Color: {self.__color}")
        print(f"Bed Material: {self.__material}")



Richbond = Bed("blue", "cotton")
Mizidor = Bed("black", "poly")
Richbond.display()
