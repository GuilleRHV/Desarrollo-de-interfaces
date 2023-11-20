from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget,QMessageBox,QDialogButtonBox,QLineEdit,QLabel,QVBoxLayout, QApplication, QDialog, QMainWindow, QPushButton

class Formulario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario")
        layout = QVBoxLayout()
        label_nombre = QLabel("Nombre:")
        self.campo_nombre = QLineEdit()
        label_contraseña = QLabel("Contraseña:")
        self.campo_contraseña = QLineEdit()
        self.campo_contraseña.setEchoMode(QLineEdit.Password)
        self.label_msm = QLabel("")

        #Crear boton enviar
        boton_envio = QPushButton("Login")
        boton_envio.clicked.connect(self.autenticar)

        layout.addWidget(label_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(label_contraseña)
        layout.addWidget(self.campo_contraseña)
        layout.addWidget(boton_envio)
        layout.addWidget(self.label_msm)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def autenticar(self):
        nombre = self.campo_nombre.text()
        contraseña = self.campo_contraseña.text()
        if (nombre == "juan" and contraseña =="password"):
            self.label_msm.setText("Correcto")
            self.label_msm.setStyleSheet("color: green")
            print(self.label_msm.text())
        else:
            self.label_msm.setText("Incorrecto")
            self.label_msm.setStyleSheet("color: red")
            print(self.label_msm.text())
            self.pesatnya_error()

    def pesatnya_error(self):
        #ventanadialog = DialogoPersonalizado(self)
        #ventanadialog.exec()
        boton_pulsado = QMessageBox.information(
            self,
            "Informacion usuario",
            "Usuario/contraseña incorrectas",
            buttons=QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard
        )
        


class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dialogo personalizado")
        # Definimos los botones Ok i Cancel en nuestra variable
        botones = QDialogButtonBox.Ok
        # Pasamos la variable de botones al constructor de QDialogButtonBox
        self.caja_botones = QDialogButtonBox(botones)
        # Conectamos las señales de los botones con las ranuras de QDialog
        self.caja_botones.accepted.connect(self.accept)
        # Añadimos un QLabel y el QDialogButtonBox en un layout vertical
        self.layout_dialogo = QVBoxLayout()
        self.layout_dialogo.addWidget(
            QLabel("Los datos son incorrectos"))
        self.layout_dialogo.addWidget(self.caja_botones)
        self.setLayout(self.layout_dialogo)

if __name__ == "__main__":
    app = QApplication([])
    formulario = Formulario()
    formulario.show()
    app.exec()