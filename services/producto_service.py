from models.productos import crear_producto
productos = []


def registrar(nombre, precio, stock):
    producto = crear_producto(nombre, precio, stock)
    productos.append(producto)
    print("Producto agregado correctamente")
    return producto

def listar():
    for producto in productos:
        print(producto)

def consultar_por_precio(precio):
    for producto in productos:
        if producto["precio"] == precio:
            print(producto)



