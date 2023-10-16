from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QLabel


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo uso slot predefinido")
        
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setFixedSize(50,30)
        self.line_edit1.setMaxLength(5)
        

        self.etiqueta1 = QLabel(self)
        self.etiqueta1.setFixedSize(50, 30)
        self.etiqueta1.move(50, 0)
        # Conectamos el evento textChanged del lineEdit al slot setText del label
        self.line_edit1.textChanged.connect(self.etiqueta1.setText)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
