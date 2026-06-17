# PyQt5 QLabels
# PyQt5 Qt alignments

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200, 500, 400)
        self.setWindowTitle("Your first PyQt5 cool GUI")
        self.setWindowIcon(QIcon("C:\\Users\\abulb\\OneDrive\\Pictures\\Screenshots\\67.jpg"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: grey;"
                             "background-color: cyan;"
                             "font-weight: bold;"
                             "text-decoration: underline")
        
        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom)  # vertically bottom
        # label.setAlignment(Qt.AlignVCenter) # vertically center
        # label.setAlignment(Qt.AlignRight) # Horizontally right
        # label.setAlignment(Qt.AlignLeft) # Horizontally left
        # label.setAlignment(Qt.AlignHCenter) # Horizontally center

        # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter) # Vertically center and Horizontally center
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # horizontally center and vertically top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Horizontally center and vertically bottom
        # label.setAlignment(Qt.AlignCenter) # Align vertically and Horizontally center



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    