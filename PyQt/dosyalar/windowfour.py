# Gerekli olan kütüphaneler import edildi.
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # x , y , width , height 
        self.setGeometry(200, 200, 700, 400)
        # Pencere başlığı
        self.setWindowTitle("PyQt Window")
        # Pencere simgesi
        self.setWindowIcon(QIcon("images/python.png"))
        
        # Pencere boyutu değiştirilemez.
         #self.setFixedWidth(700)
         #self.setFixedHeight(400)
        
        # Arkaplan rengi
        self.setStyleSheet("background-color: dark;")
        # Pencere opacity
        self.setWindowOpacity(0.2)

app  = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())