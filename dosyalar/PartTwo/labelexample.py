# Gerekli olan kütüphaneler import edildi.
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
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
        self.setWindowIcon(QIcon("./dosyalar/PartTwo/images/python.png"))


        '''
        # Ekrana yazı yazdırma
        label = QLabel("Merhaba Dünya", self) 

        # İlk yazının yerine yenisini yazdırma 
        #label.setText("Hello World")
        
        # Yazının konumunu belirleme
        label.move(100, 100)
        # Yazının yazı tipini belirleme
        label.setFont(QFont("Times New Roman", 12))
        # Yazının rengini belirleme
        label.setStyleSheet('color.red')

        # Yazının sayısal değerini belirleme
        #label.setText(str(12))
        label.setNum(15)

        # Ekrandaki tüm yazıları silme
        label.clear()
        
        '''


        '''
        # Resim ekleme
        label = QLabel (self)
        pixmap = QPixmap("./dosyalar/PartTwo/images/python.png")
        label.setPixmap(pixmap)
        
        '''
        

        # Gif ekleme
        label = QLabel(self)
        # Dosya yolunu belirleme
        movie = QMovie("./dosyalar/PartTwo/images/python.gif")
        # Gif'in hızını belirleme
        movie.setSpeed(250)
        # Gif'i ekrana yazdırma
        label.setMovie(movie)
        # Gif'i başlatma
        movie.start()


app  = QApplication(sys.argv) 
Window = Window()
Window.show()
sys.exit(app.exec())