print("Estoy probando python")
comida = ['platano','manzana','fresa']
for a in comida:
    print(a)
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
# Clase Ventana, hereda de QWidget, componente base.
class VentanaPrincipal(QMainWindow):
    # Constructor de la clase Ventana
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana")
        self.boton1 = QPushButton("Haz clic!", self)
        # Configuramos el botón como el elemento principal de la ventana.
        # Esto es porque estamos usando un QMainWindow. No era necesario
        # pasarle el parent en su creación.
        self.setCentralWidget(self.boton1)
        # Conectamos el evento clic del botón a la ranura clic_de_boton
        self.boton1.clicked.connect(self.clic_de_boton)

    # Definimos la ranura que se ejecutará con el clic del botón
    def clic_de_boton(self):
        print("Señal de clic recibida -> Ejecución de la ranura")

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
