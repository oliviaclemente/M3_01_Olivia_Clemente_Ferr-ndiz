class Producto:
  def constructor(self, codigo, nombre, precio, tipo):
    self.codigo=codigo
    self.nombre= nombre
    self.precio=precio
    self.tipo=tipo
  def mostrar(self):
    print("Codigo:",self.codigo)
    print("Nombre:",self.nombre)
    print("Precio:",self.precio)
    print("Tipo:",self.tipo)
  def _str_cons(self):
    print("El producto se ha creado con éxito")

producto1=Producto()
producto1.constructor("C2CR", "Gambas", 80, "Roja")
producto1.mostrar()

producto1=Producto()
producto1.constructor("C3CT", "Tellinas", 40, "Mediterraneas")
producto1.mostrar()

print(producto1.strip("C45T", "Gambas", 100, "Roja"))
