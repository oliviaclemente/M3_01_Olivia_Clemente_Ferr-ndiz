class Alumno:
  def constructor(self, nombre, nota):
    self.nombre= nombre
    self.nota=nota
  def mostrar(self):
    print("Nombre:",self.nombre)
    print("Nota:",self.nota)
    
alumno1=Alumno()
alumno1.constructor("Lau")
alumno1.mostrar()

alumno2=Alumno()
alumno2.constructor("Juls")
alumno2.mostrar()