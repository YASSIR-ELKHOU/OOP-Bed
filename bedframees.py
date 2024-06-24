class BedFrame:
    def _initial_(self, color="Default Color", material="Default Material"):
        self.color = color
        self.material = material

    def set_color(self, color):
        self.color = color

    def set_material(self, material):
        self.material = material

    def get_color(self):
        return self.color

    def get_material(self):
        return self.material

    def display(self):
        print(f"Bed Frame Color: {self.color}")
        print(f"Bed Frame Material: {self.material}")
