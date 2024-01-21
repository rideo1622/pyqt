# Gerekli olan kütüphaneler import edildi.
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Uygulama oluşturuldu.
app = QApplication(sys.argv)

# QMainWindow sınıfından bir pencere oluşturuldu. 
# QMainWindow Ana uygulama penceresini sağlar ve kullanıcı arayüzü oluşturmak için bir çerçeve sunar. 
window = QMainWindow()

# Pencere başlığı belirlendi.
window.statusBar().showMessage("Welcome to PyQt6")

# Menü oluşturuldu.
window.menuBar().addMenu("File")

# Pencere görüntülendi
window.show()

# Uygulama başlatıldı.
sys.exit(app.exec())