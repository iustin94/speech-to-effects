from PySide6.QtWidgets import QMainWindow
from src.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.show()
