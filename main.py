import sys, os
sys.path.insert(0,'.')

#Check dependencies
try:
    from main_window import MainWindow
except ModuleNotFoundError:
    os.system("python -m pip install -r requirements.txt")
    sys.exit()

from PySide6 import QtWidgets


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    app.exec()
    os._exit(1)