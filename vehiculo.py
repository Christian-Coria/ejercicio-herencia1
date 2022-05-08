class Vehiculo:
    def __init__(self,color,ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return "color " + self._color + ", ruedas " + str(self._ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + " , velocidad km/h: " + str(self._velocidad)


class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self._tipo = tipo

    def __str__(self):
        return super().__str__() + ", tipo : "+ self._tipo

vehiculo1 = Vehiculo("rojo",4)
print(vehiculo1)
coche1 = Coche("negro",4,60)
print(coche1)
bicicleta1 = Bicicleta("blanca",2,"playera")
print(bicicleta1)