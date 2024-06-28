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
        print("A bed without Pillows isn't a Bed")
        for pillow in self._pillows:
            print(pillow)


class BunkBed(Bed):
    max_safety_features = 10

    def _init_(self, size, material, has_storage=False,frame=None, filling=None, number_of_levels=1, safety_features=None):
        super()._init_(size, material, has_storage, frame, filling)
        self._number_of_levels = number_of_levels
        self._safety_features = safety_features[:BunkBed.max_safety_features] if safety_features else []
        self._safety_feature_count = len(self._safety_features)

    def set_number_of_levels(self, number_of_levels):
        self._number_of_levels = number_of_levels

    def set_safety_features(self, safety_features):
        self._safety_features = safety_features[:BunkBed.max_safety_features]
        self._safety_feature_count = len(self._safety_features)

    def get_number_of_levels(self):
        return self._number_of_levels

    def get_safety_features(self):
        return self._safety_features

    def display(self):
        super().display()
        print(f"Number of Levels: {self._number_of_levels}")
        print("Safety Features: " + ", ".join(self._safety_features))
class Bed_safety:
    def __init__(self, size, material, has_storage=False, frame=None, filling=None):
        self._size = size
        self._material = material
        self._has_storage = has_storage
        self._frame = frame
        self._filling = filling

    def display(self):
        print(f"Size: {self._size}")
        print(f"Material: {self._material}")
        print(f"Has Storage: {self._has_storage}")
        print(f"Frame: {self._frame}")
        print(f"Filling: {self._filling}")
class BunkBed(Bed_safety):
    max_safety_features = 10

    def __init__(self, size, material, has_storage=False, frame=None, filling=None, number_of_levels=1, safety_features=None):
        self._size = size
        self._material = material
        self._has_storage = has_storage
        self._frame = frame
        self._filling = filling
        self._number_of_levels = number_of_levels
        self._safety_features = safety_features[:BunkBed.max_safety_features] if safety_features else []

    def set_number_of_levels(self, number_of_levels):
        self._number_of_levels = number_of_levels

    def set_safety_features(self, safety_features):
        self._safety_features = safety_features[:BunkBed.max_safety_features]

    def get_number_of_levels(self):
        return self._number_of_levels

    def get_safety_features(self):
        return self._safety_features

    def display(self):
        print(f"Size: {self._size}")
        print(f"Material: {self._material}")
        print(f"Has Storage: {self._has_storage}")
        print(f"Frame: {self._frame}")
        print(f"Filling: {self._filling}")
        print(f"Number of Levels: {self._number_of_levels}")
        print("Safety Features: " + ", ".join(self._safety_features))


def create_bed():
    color = input("Enter the bed color: ")
    material = input("Enter the bed material: ")
    return Bed(color, material)

def create_bed_filling():
    material = input("Enter the bed filling material: ")
    type = input("Enter the bed filling type: ")
    return BedFilling(material, type)

def create_bed_frame():
    material = input("Enter the bed frame material: ")
    color = input("Enter the bed frame color: ")
    return BedFrame(material, color)

def create_bunk_bed():
    size = input("Enter the bunk bed size: ")
    material = input("Enter the bunk bed material: ")
    has_storage = input("Does the bunk bed have storage? (yes/no): ").lower() == 'yes'
    frame = create_bed_frame()
    filling = create_bed_filling()
    number_of_levels = int(input("Enter the number of levels: "))
    safety_features = input("Enter safety features (comma separated): ").split(", ")
    return BunkBed(size, material, has_storage, frame, filling, number_of_levels, safety_features)

def main():
    print("Dear sleep lover, time to create a bed ")
    bed = create_bed()
    bed.display()
    
    print("\nCreate a bunk bed:")
    bunk_bed = create_bunk_bed()
    bunk_bed.display()

if __name__ == "__main__":
    main()
