from PyQt5.QtWidgets import QWidget,QHBoxLayout,QFrame,QSplitter,QStyleFactory,QApplication
from PyQt5.QtCore import Qt
import sys
"""
QSplitter组件能让用户通过拖拽分割线的方式改变子窗口大小的组件。本例中我们展示用两个分割线隔开的三个QFrame组件。
三个窗口和两个分割线的布局创建完成了，但是要注意，有些主题下，分割线的显示效果不太好
"""
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        # 为了更清楚的看到分割线，我们使用了设置好的子窗口样式。

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        # 创建一个QSplitter组件，并在里面添加了两个框架。

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        # 也可以在分割线里面再进行分割。

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


