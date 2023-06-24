import tkinter as tk

class InterfazListaDeseos:
    def __init__(self, conexion):
        self.conexion = conexion

        self.ventana = tk.Tk()
        self.ventana.title("Lista de Deseos")
        self.ventana.configure(bg="black")  # Configurar el color de fondo para tema oscuro

        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear los elementos de la interfaz
        self.titulo_label = tk.Label(self.ventana, text="Lista de Deseos", font=("Arial", 16), bg="black", fg="white")
        self.titulo_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.producto_label = tk.Label(self.ventana, text="Producto:", bg="black", fg="white")
        self.producto_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.producto_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.producto_entry.grid(row=1, column=1, padx=5, pady=5)

        self.cantidad_label = tk.Label(self.ventana, text="Cantidad:", bg="black", fg="white")
        self.cantidad_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.cantidad_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5)

        self.precio_label = tk.Label(self.ventana, text="Precio:", bg="black", fg="white")
        self.precio_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.precio_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)

        self.agregar_button = tk.Button(self.ventana, text="Agregar", command=self.agregar_deseo, bg="black", fg="white")
        self.agregar_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.lista_deseos_text = tk.Text(self.ventana, bg="black", fg="white")  # Configurar colores para tema oscuro
        self.lista_deseos_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.actualizar_lista_deseos()  # Mostrar la lista de deseos al iniciar la interfaz

    def actualizar_lista_deseos(self):
        deseos = self.conexion.obtener_deseos()

        self.lista_deseos_text.delete("1.0", tk.END)  # Limpiar el campo de texto

        if deseos:
            for deseo in deseos:
                texto = f"ID: {deseo[0]}, Producto: {deseo[1]}, Cantidad: {deseo[2]}, Precio: {deseo[3]}\n"
                self.lista_deseos_text.insert(tk.END, texto)
        else:
            self.lista_deseos_text.insert(tk.END, "No hay elementos en la lista de deseos.")

    def agregar_deseo(self):
        producto = self.producto_entry.get()
        cantidad = int(self.cantidad_entry.get())
        precio = float(self.precio_entry.get())

        self.conexion.agregar_deseo(producto, cantidad, precio)
        print("Deseo agregado exitosamente.")

        self.actualizar_lista_deseos()  # Actualizar la lista mostrada en la interfaz

    def iniciar(self):
        self.ventana.mainloop()
