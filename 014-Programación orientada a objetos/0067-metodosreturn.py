class Persona:
    def __init__(self,nombre,edad,colorpelo):
       self.edad = edad
       self.nombre = nombre
       self.colorpelo = colorpelo
       
    def saludaMe(self):
        return "Hola, yo te saludo"

Juan = Persona("Juan",34,"moreno")
print(Juan.nombre)
print(Juan.edad)
print(Juan.colorpelo)
print(Juan.saludaMe())
