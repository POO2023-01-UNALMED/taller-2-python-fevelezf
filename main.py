class Asiento:
    def __init__(self,color,precio,registro):
        self.color= color
        self.precio= precio
        self.registro= registro

    def cambiarColor(self,color):
        if color=="rojo":
            self.color="rojo"
        elif color=="verde":
            self.color="verde"
        elif color=="amarillo":
            self.color="amarillo"
        elif color=="negro":
            self.color="negro"
        elif color=="blanco":
            self.color="blanco"
    
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro= registro

    def cambiarRegistro(self,registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        if tipo=="electrico":
            self.tipo="electrico"
        elif tipo =="gasolina":
            self.tipo="gasolina"

class Auto:
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos= asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreados=cantidadCreados
    
    def cantidadAsientos(self):
        contador=0
        for asi in self.asientos:
            if(type(asi)==Asiento):
                contador+=1
        return contador

    def verificarIntegridad(self):
        if self.registro== self.motor.registro:
            for asi in self.asientos:
                if(type(asi)==Asiento):
                    if asi.registro != self.motor.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"



