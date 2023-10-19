from ast import If
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
    QProgressBar,
    QDial,
QLCDNumber,
QTextEdit


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
        
        progress_bar = QProgressBar()
        progress_bar.setMinimum(1)
        progress_bar.setMaximum(100)
        progress_bar.setValue(33)
 
      
        layout_formulario.addRow(QLabel("QProgressbar:"),progress_bar)



        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(50)
       # slider.orientation(Qt.Orientation)
        slider.setTickInterval(2)
        layout_formulario.addRow(QLabel("QSlider:"),slider)
        
        qdial = QDial()
        qdial.setMinimum(0)
        qdial.setMaximum(100)
        qdial.setValue(40)
        qdial.setRange(0,100)
        qdial.setWrapping(True)
        qdial.setNotchesVisible(True)
        lcd = QLCDNumber(qdial)
        

        qdial.valueChanged.connect(lcd.display)
        layout_formulario.addRow(QLabel("Qdial: "),qdial)
        layout_formulario.addRow(QLabel("Contador: "),lcd)
     

        layout_formulario.addRow(QLabel("QTextEdit"))
        qtextedit = QTextEdit()
        qtextedit.setText("Texto por default")
        layout_formulario.addRow(qtextedit)

        boton = QPushButton("Boton")
        boton.setFixedSize(100,60)
        layout_formulario.addRow(boton)


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()



app.exec()
