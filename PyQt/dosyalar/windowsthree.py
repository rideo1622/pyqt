# Gerekli olan kütüphaneler import edildi.
from PyQt6.QtWidgets import QApplication, QDialog
import sys

# Uygulama oluşturuldu.
app = QApplication(sys.argv)

# QMainWindow sınıfından bir pencere oluşturuldu. 
#  QDialog Kısa süreli görevler ve kullanıcıyla kısa iletişimler için kullanılan bir iletişim penceresi sınıfıdır 
window = QDialog()

# Pencere başlığı belirlendi.
window.show()

# Uygulama başlatıldı.
sys.exit(app.exec())