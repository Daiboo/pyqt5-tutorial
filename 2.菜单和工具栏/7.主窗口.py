import sys
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QApplication
from PyQt5.QtGui import QIcon
"""
主窗口就是上面三种栏目的总称，现在我们把上面的三种栏在一个应用里展示出来。
"""

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        # 这里创建了一个文本编辑区域，并把它放在QMainWindow的中间区域。这个组件会占满所有剩余的区域。
        
        exitAct = QAction("exit",self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)
        
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

