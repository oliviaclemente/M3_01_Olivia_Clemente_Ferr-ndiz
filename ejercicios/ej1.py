class Alumno:
  def constructor(self, nombre):
    self.nombre= nombre
  def mostrar(self):
    print("Nombre:",self.nombre)
    
alumno1=Alumno()
alumno1.constructor("Lau")
alumno1.mostrar()

alumno2=Alumno()
alumno2.constructor("Juls")
alumno2.mostrar()