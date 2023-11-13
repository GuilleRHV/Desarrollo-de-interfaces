from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QPushButton,
    QComboBox,
    QDoubleSpinBox
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout formulario")

        # Creamos un objeto layout formulario
        layout_formulario = QFormLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_formulario)
        self.setCentralWidget(componente_principal)
        self.combo_box = QComboBox(self)
        
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre","Noviembre", "Diciembre" ]
        self.combo_box.addItems(meses)
        layout_formulario.addRow(QLabel('Meses: '), self.combo_box)
        # Cada fila contendrá una etiqueta y un componente de entrda
        button = QPushButton("Mostrar select e index")
        layout_formulario.addRow(button)
        
        button.clicked.connect(self.mostrar_dialogo)

    def mostrar_dialogo(self):
        content = self.combo_box.currentText()
        index = self.combo_box.currentIndex()
        print("--------------------")
        print("Contenido: ", content)
        print("Index: ", index)
        print("--------------------")
        
app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
