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
  def cons(self):
    print("El producto se ha creado con éxito")
  def__str__