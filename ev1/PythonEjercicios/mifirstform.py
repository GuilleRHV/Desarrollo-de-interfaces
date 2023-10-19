from PySide6.QtCore import *

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QComboBox,
    QCheckBox,
    QGroupBox,
    QVBoxLayout,
    QRadioButton,
    QDateTimeEdit,
    QSlider,
    QProgressBar

)


from datetime import date

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()


        
        self.setWindowTitle("Layout formulario")

        # Creamos un objeto layout formulario
        layout_formulario = QFormLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_formulario)
        self.setCentralWidget(componente_principal)

        # Cada fila contendrá una etiqueta y un componente de entrda
        layout_formulario.addRow(QLabel("Nombre: "), QLineEdit())
        layout_formulario.addRow(QLabel("Texto: "), QLineEdit())
        layout_formulario.addRow(QLabel("Entero: "), QSpinBox())
        layout_formulario.addRow(QLabel("Decimal: "), QDoubleSpinBox())
        #layout_formulario.addRow(QLabel('test: '), QComboBox.addItems(["Opcion 1","Opcion 2","Opcion 3","Opcion 4"]))
        layout_formulario.addRow(QLabel(),QCheckBox("I agree") )
        layout_formulario.addWidget(QGroupBox('test'))
        layout_formulario.addWidget(QPushButton('opcion 1'))
        layout_formulario.addWidget(QPushButton('opcion 2'))
        layout_formulario.addWidget(QPushButton('opcion 3'))
        layout_formulario.addRow(QPushButton("Boton"))
        
        layout_vertical = QVBoxLayout()
        groupbox = QGroupBox("Radio buton group")
        radio1 = QRadioButton("Ex1")
        radio2 = QRadioButton("Ex2")
        radio3 = QRadioButton("Ex3")
        radio2.setChecked(True)


        layout_vertical.addWidget(radio1)
        layout_vertical.addWidget(radio2)
        layout_vertical.addWidget(radio3)
        groupbox.setLayout(layout_vertical)
        layout_formulario.addRow(groupbox)
        calendario = QDateTimeEdit(date.today(),self,calendarPopup=True)
        layout_formulario.addRow(QLabel("Fecha de nacimiento: "),calendario)
        
        barra_deslizante = QProgressBar()
        barra_deslizante.setMinimum(1)
        barra_deslizante.setMaximum(100)
        barra_deslizante.setValue(33)
      
        layout_formulario.addRow(QLabel("QProgressbar:"),barra_deslizante)



        slider = QSlider()
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(100)
        slider.orientation(Qt.Orientation)
        layout_formulario.addRow(QLabel("QSlider:"),slider)
        

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
