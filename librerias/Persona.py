class Persona:
    def __init__(self,nombre,edad,colorpelo):
       self.edad = edad
       self.nombre = nombre
       self.colorpelo = colorpelo
       
    def saludaMe(self):
        return "Hola, me llamo "+self.nombre+" y yo te saludo"


