# PyQt5 Line-edit (text box) functionality

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200, 500, 400)
        self.setWindowTitle("Your first PyQt5 cool GUI")
        self.setWindowIcon(QIcon("C:\\Users\\abulb\\OneDrive\\Pictures\\Screenshots\\67.jpg"))

        self.line_edit = QLineEdit("", self)
        self.line_edit.setPlaceholderText("Enter your name")
        self.button = QPushButton("Submit", self)
        self.initUI()
    
    def initUI(self):
        
        self.line_edit.setGeometry(10, 10, 200, 30)
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     "font-family: Arial;")
        
        self.button.setGeometry(210,10, 100, 30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print(f"Hello {self.line_edit.text()}")    


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    