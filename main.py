import os
from PyQt5.QtWidgets import QApplication,QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
from multiprocessing import Process, Pipe,freeze_support
import signal
import sys
import obavestenja
#from gui import app_options

def st(pipe):
    def gasi(pipe):
        p2_pid = pipe.recv()
        os.kill(p2_pid, signal.SIGTERM)
        app.quit()

    app = QApplication(sys.argv)
    trayIcon = QSystemTrayIcon(QIcon("icon.ico"), parent=app)
    trayIcon.setToolTip('Battery Notifier')
    trayIcon.show()

    menu = QMenu()
    optionAction = menu.addAction('Options')
    optionAction.triggered.connect(lambda: os.startfile("options.exe"))
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(lambda: gasi(pipe))

    trayIcon.setContextMenu(menu)
    app.exec_()


conn1, conn2 = Pipe()
p1 = Process(target=st, args=(conn1,))
p2 = Process(target=obavestenja.main_app)

if __name__ == '__main__':
    freeze_support()
    p1.start()
    p2.start()
    conn1.send(p1.pid)
    conn2.send(p2.pid)