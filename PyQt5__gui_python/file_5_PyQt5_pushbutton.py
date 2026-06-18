# PyQt5 pushbutton

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 150, 500, 400)
        self.setWindowTitle("Your first PyQt5 cool GUI")
        self.setWindowIcon(QIcon("C:\\Users\\abulb\\OneDrive\\Pictures\\Screenshots\\67.jpg"))
        self.button = QPushButton("Hello", self)
        self.label = QLabel("This is a label", self)
        self.initUI()
    
    def initUI(self):
        # button = QPushButton("Hello", self)
        # self.button = QPushButton("Hello", self)
        self.button.setGeometry(180, 150, 120, 60)
        self.button.setStyleSheet("background-color: black;"
                             "color: blue;"
                             "font-size: 20px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(25, 25, 150, 75)
        self.label.setStyleSheet("background-color: green;"
                                 "font-size: 20px;"
                                 "padding-left: 10px;")
    
    def on_click(self):
        # print("clicked")
        self.button.setText("Clicked")
        self.label.setText("Goodbye")
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    