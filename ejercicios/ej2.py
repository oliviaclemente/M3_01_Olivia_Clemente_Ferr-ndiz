class Alumno:
  def constructor(self, nombre, nota):
    self.nombre= nombre
    self.nota=nota
  def mostrar(self):
    print("Nombre:",self.nombre)
    print("Nota:",self.nota)
  def _str_calificacion(self):
      if self.nota<5:
        print("El alumno tiene un suspenso")
      else:
        print("El alumno tiene un aprobado")

    
alumno1=Alumno()
alumno1.constructor("Lau",9)
alumno1.mostrar()
alumno1.calificacion()

alumno2=Alumno()
alumno2.constructor("Juls",4)
alumno2.mostrar()
alumno2.calificacion()
