from Vehicle import Vehicle  

class Bus(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load  

    def display_info(self):
        """Override the parent class method to display Bus-specific information."""
        return f"Bus: {self.brand} {self.model}, Max load: {self.max_load} tons ({self.year})"

    def honk(self):
        """Specific honk sound for the Bus."""
        return "HONK HONK!"
