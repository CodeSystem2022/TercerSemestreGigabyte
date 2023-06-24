import speech_recognition as sr
from conexion import ConexionDB

class ListaDeseos:
    def __init__(self):
        self.conexion = ConexionDB()

    def reconocer_comandos(self):
        r = sr.Recognizer()
        r.energy_threshold = 300  # Ajustar el umbral de activación

        while True:
            with sr.Microphone() as source:
                print("Di un comando:")
                r.adjust_for_ambient_noise(source, duration=1)  # Ajustar al ruido ambiente
                audio = r.listen(source, timeout=5)

            try:
                command = r.recognize_google(audio, language="es-AR")
                print("Comando reconocido (voz): " + command)
                return command.lower()
            except sr.UnknownValueError:
                print("No se pudo reconocer el comando por voz.")
                break
            except sr.WaitTimeoutError:
                print("Tiempo de espera agotado para el comando por voz.")

            print("Di un comando (texto):")
            command = input().lower()
            print("Comando ingresado (texto): " + command)
            return command

    def ejecutar(self):
        while True:
            print("\n--- Lista de Deseos ---")
            print("Di 'agregar' para agregar un deseo")
            print("Di 'mostrar' para mostrar los deseos")
            print("Di 'eliminar' para eliminar un deseo")
            print("Di 'eliminar todo' para eliminar todos los deseos")
            print("Di 'salir' para salir")

            command = self.reconocer_comandos()

            if command == "agregar":
                producto = input("Producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                self.conexion.agregar_deseo(producto, cantidad, precio)
                print("Deseo agregado exitosamente.")

            elif command == "mostrar":
                self.conexion.mostrar_deseos()

            elif command == "eliminar":
                deseo_id = int(input("Ingrese el ID del deseo a eliminar: "))
                self.conexion.eliminar_deseo(deseo_id)
                print("Deseo eliminado exitosamente.")

            elif command == "eliminar todo":
                confirmacion = input("¿Está seguro de que desea eliminar todos los deseos? (s/n): ")
                if confirmacion.lower() == "s":
                    self.conexion.eliminar_todo()
                    print("Todos los deseos han sido eliminados.")
                else:
                    print("Operación cancelada.")

            elif command == "salir":
                self.conexion.cerrar_conexion()
                break

            else:
                print("Comando inválido. Por favor, ingresa un comando válido.")

if __name__ == '__main__':
    lista_deseos = ListaDeseos()
    lista_deseos.ejecutar()