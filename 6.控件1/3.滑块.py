from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("6.控件\静音_mute.svg"))
        self.label.setGeometry(160,40,80,30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self,value):
        if value == 0:
            self.label.setPixmap(QPixmap("6.控件\静音_mute.svg"))
        elif value > 0 and value <= 50:
            self.label.setPixmap(QPixmap("6.控件\音量减小_volume-down.svg"))
        else:
            self.label.setPixmap(QPixmap("6.控件\音量增大_volume-up.svg"))
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
