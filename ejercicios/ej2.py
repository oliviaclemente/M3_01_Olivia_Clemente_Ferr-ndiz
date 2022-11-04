class Alumno:
  def constructor(self, nombre, nota):
    self.nombre= nombre
    self.nota=nota
  def mostrar(self):
    print("Nombre:",self.nombre)
    print("Nota:",self.nota)
  def _str_calificacion(self): 
    return"Lo que quiero mostar"

    
alumno1=Alumno()
alumno1.constructor("Lau",9)
alumno1.mostrar()

alumno2=Alumno()
alumno2.constructor("Juls",4)
alumno2.mostrar()