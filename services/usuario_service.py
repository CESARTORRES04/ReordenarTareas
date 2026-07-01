from models.usuario import crear_usuario

usuarios = []

def registrar_usuario(nombre, edad):
    usuario = crear_usuario(nombre, edad)
    usuarios.append(usuario)

    return usuario


def buscar_usuario(nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario
    return None

