# Bu dosyada PyQt6 ile tasarladığımız arayüzü yüklüyoruz.
from PyQt6.QtWidgets import QApplication, QWidget
# sys modülünü kullanarak uygulamamızı kapatmak için kullanıyoruz.
import sys
# uic modülünü kullanarak tasarladığımız arayüzü yüklüyoruz.
from PyQt6 import uic

# UI sınıfımızı QWidget sınıfından miras alarak oluşturuyoruz.
class UI(QWidget):

    # UI sınıfımızın yapıcı metodunu oluşturuyoruz.
    def __init__(self):

        # QWidget sınıfının yapıcı metodunu miras alıyoruz.
        super().__init__()
        # Tasarladığımız arayüzü yüklüyoruz.
        uic.loadUi("./WindowUI.ui", self)

# Uygulamamızı çalıştırıyoruz.
app = QApplication(sys.argv)
# UI sınıfımızdan bir nesne oluşturuyoruz.
window = UI()
# Uygulamamızı çalıştırıyoruz.
window.show ()
app.exec()