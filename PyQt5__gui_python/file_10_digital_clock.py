# PyQt5 Digital Clock program

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        font_id = QFontDatabase.addApplicationFont("C:\\Python_and_C\\PyQt5__gui_python\\DS-DIGIB.TTF")

        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)

        self.time_label.setFont(my_font)


        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 120px;"
                                    #   "font-family: Arial;"
                                      "color: hsl(120, 100%, 51%);")
        self.setStyleSheet("background-color: black;")
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())