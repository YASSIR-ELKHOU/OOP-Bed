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

class BedFrame:
    def __init__(self, material, color):
        self._material = material
        self._color = color

    def set_material(self, material):
        self._material = material

    def set_color(self, color):
        self._color = color

    def get_material(self):
        return self._material

    def get_color(self):
        return self._color

    def display(self):
        print(f"Bed Frame Material: {self._material}")
        print(f"Bed Frame Color: {self._color}")


class Bedd:
    max_pillows = 5

    def __init__(self, size, has_storage=False, frame=None, filling=None):
        self._size = size
        self._has_storage = has_storage
        self._frame = frame if isinstance(frame, BedFrame) else BedFrame("Default Material", "Default Color")
        self._filling = filling if isinstance(filling, BedFilling) else BedFilling("Default Material", "Default Type")
        self._pillows = []

    def add_pillow(self, pillow_description):
        if len(self._pillows) < Bedd.max_pillows:
            self._pillows.append(pillow_description)
        else:
            print("Cannot add more pillows, maximum limit reached.")

    def display(self):
        print(f"Bed Size: {self._size}")
        print(f"Has Storage: {'Yes' if self._has_storage else 'No'}")
        self._frame.display()
        self._filling.display()
        print("A bed without bed Pillows isn't a Bed")
        for pillow in self._pillows:
            print(pillow)


custom_frame = BedFrame("Wood", "Oak")
custom_filling = BedFilling("Foam", "Memory Foam")
HER = Bedd("QUEEN", has_storage=True, frame=custom_frame, filling=custom_filling)
HER.display()


