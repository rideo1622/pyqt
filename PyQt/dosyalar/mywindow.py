from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class ReverseTextApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Arayüz bileşenlerini ayarla
        self.layout = QVBoxLayout()

        # Metin giriş alanı
        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Metin girin")
        self.inputField.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.inputField)

        # Buton
        self.reverseButton = QPushButton("Metni Ters Çevir")
        self.reverseButton.setFont(QFont("Arial", 12))
        self.reverseButton.clicked.connect(self.reverseText)
        self.layout.addWidget(self.reverseButton)

        # Sonuç etiketi
        self.resultLabel = QLabel("Ters çevrilmiş metin burada görünecek")
        self.resultLabel.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.resultLabel)

        # Ana pencere ayarları
        self.setLayout(self.layout)
        self.setWindowTitle("Metin Ters Çevirici")
        self.setWindowIcon(QIcon('app_icon.png'))  # Özel bir ikon ekleyin
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            QLineEdit {
                border: 2px solid #34495e;
                border-radius: 10px;
                padding: 5px;
                margin: 10px;
            }
            QPushButton {
                background-color: #3498db;
                border-radius: 10px;
                padding: 10px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

    def reverseText(self):
        # Metni ters çevirme işlemi
        input_text = self.inputField.text()
        reversed_text = input_text[::-1]
        self.resultLabel.setText(reversed_text)

# Uygulamayı başlat
app = QApplication([])
app.setStyle("Fusion")  # Modern görünüm için Fusion stili
window = ReverseTextApp()
window.show()
app.exec()
