from conexionInterface import ConexionDB
from interfaz import InterfazListaDeseos

if __name__ == '__main__':
    conexion = ConexionDB()
    interfaz = InterfazListaDeseos(conexion)
    interfaz.iniciar()
