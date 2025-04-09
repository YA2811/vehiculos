class vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"
    
class auto(vehiculo):
    def descripcion(self):
        return f"auto.{self.marca} {self.modelo} con 4 ruedas"
    
class motocicleta(vehiculo):
    def desccripcion(self):
        return f"motocicleta: {self.marca} {self.modelo} con 2 ruedas"
