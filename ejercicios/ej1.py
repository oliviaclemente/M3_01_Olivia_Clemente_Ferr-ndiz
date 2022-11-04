class Alumno:
  def constructor(self, nombre):
    self.nombre= nombre
  def mostrar(self):
    print("Nombre:",self.nombre)
    
alumno1=Alumno()
alumno1.constructor("Laura")
alumno1.mostrar()