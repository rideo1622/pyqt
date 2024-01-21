# Gerekli olan kütüphaneler import edildi.
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

# Pencere sınıfı oluşturuldu.
class Window(QWidget):
    # Pencere özellikleri belirlendi.
    def __init__(self):
        # QWidget sınıfının özellikleri aktarıldı.
        super().__init__()

        # x , y , width , height 
        self.setGeometry(200, 200, 700, 400)
        # Pencere başlığı
        self.setWindowTitle("PyQt Window")
        # Pencere simgesi
        self.setWindowIcon(QIcon("./dosyalar/PartOne/images/python.png"))
        
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