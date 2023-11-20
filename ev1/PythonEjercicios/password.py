from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget,QLineEdit,QLabel,QVBoxLayout, QApplication, QDialog, QMainWindow, QPushButton

class Formulario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario")
        layout = QVBoxLayout()
        label_nombre = QLabel("Nombre:")
        self.campo_nombre = QLineEdit()
        label_contraseña = QLabel("COntraseña:")
        self.campo_contraseña = QLineEdit()
        self.campo_contraseña.setEchoMode(QLineEdit.Password)
        self.label_msm = QLabel("")

        #Crear boton enviar
        boton_envio = QPushButton("Login")
        boton_envio.clicked.connect(self.enviar_todo)

        layout.addWidget(label_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(label_contraseña)
        layout.addWidget(self.campo_contraseña)
        layout.addWidget(boton_envio)
        layout.addWidget(self.label_msm)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def enviar_todo(self):
        nombre = self.campo_nombre.text()
        contraseña = self.campo_contraseña.text()
        if (nombre == "juan" and contraseña =="password"):
            self.label_msm.setText("Correcto")
            self.label_msm.setStyleSheet("color: green")
            
        else:
            self.label_msm.setText("Incorrecto")
            self.label_msm.setStyleSheet("color: red")
        
if __name__ == "__main__":
    app = QApplication([])
    formulario = Formulario()
    formulario.show()
    app.exec()