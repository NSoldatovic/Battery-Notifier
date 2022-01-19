import os
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
from multiprocessing import Process, Pipe,freeze_support
import signal
import sys
import obavestenja
import time
from gui import app_options
def oap():
    while True:
        print("radi Program")
        time.sleep(2)

def st(pipe):
    def gasi(pipe):
        p2_pid = pipe.recv()
        os.kill(p2_pid, signal.SIGTERM)
        app.quit()

    app = QApplication(sys.argv)
    trayIcon = QSystemTrayIcon(QIcon("min_icon.png"), parent=app)
    trayIcon.setToolTip('Battery Notifier')
    trayIcon.show()

    menu = QMenu()
    optionAction = menu.addAction('Options')
    optionAction.triggered.connect(app_options)
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(lambda: gasi(pipe))

    trayIcon.setContextMenu(menu)
    app.exec_()


conn1, conn2 = Pipe()
p1 = Process(target=st, args=(conn1,))
p2 = Process(target=oap)

if __name__ == '__main__':
    freeze_support()
    while True:
        p1.start()
        p2.start()
        conn1.send(p1.pid)
        conn2.send(p2.pid)
        time.sleep(2)
        print("loop")