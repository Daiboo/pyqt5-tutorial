import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。
    # Python可以在shell里运行，这个参数提供对脚本控制的功能。

    w = QWidget()   
    # QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。
    # 默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。
    w.resize(250,150)
    # resize()方法能改变控件的大小，这里的意思是窗口宽250px，高150px。
    w.move(1000,300)
    # move()是修改控件位置的方法。它把控件放置到屏幕坐标的(300, 300)的位置。注：屏幕坐标系的原点是屏幕的左上角。
    w.setWindowTitle("Simple")
    # 我们给这个窗口添加了一个标题，标题在标题栏展示
    w.show()
    # show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    sys.exit(app.exec_())
    # 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作
    # 主循环从窗口上接收事件，并把事件派发到应用控件里。当调用exit()方法或直接销毁主控件时，主循环就会结束。
    # sys.exit()方法能确保主循环安全退出。外部环境会收到主控件如何结束的信息。
    # exec_()之所以有个下划线，是因为exec是一个Python的关键字。


