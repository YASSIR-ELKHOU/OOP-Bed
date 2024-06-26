class Bed:
    def __init__(self, color, material):
        self._color = color
        self._material = material
    
    def set_color(self, color):
        self._color = color

    def set_material(self, material):
        self._material = material

    def get_color(self):
        return self._color

    def get_material(self):
        return self._material
    
    def display(self):
        print(f"Bed Color: {self._color}")
        print(f"Bed Material: {self._material}")

Richbond = Bed("blue", "cotton")
Mizidor = Bed("black", "polyster")
Richbond.display()
Mizidor.display()


class BedFilling:
    def __init__(self, material, type):
        self._material = material
        self._type = type

    def set_type(self, material):
        self._material = material

    def set_material(self, type):
        self._type = type

    def get_material(self):
        return self._material

    def get_type(self):
        return self._type


    def display(self):
        print(f"Bed Filling Material: {self._material}")
        print(f"Bed Filling Type: {self._type}")


Richbond = BedFilling("Wool", "eco-friendly")
Richbond.display()

Mizidor = BedFilling("Foam", "economic")
Mizidor.display()
