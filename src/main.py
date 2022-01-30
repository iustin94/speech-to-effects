from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow
from src.Recorder import Recorder

app = QApplication([])
recorder = Recorder(None)
recorder.start()

# window = MainWindow()
app.exec()
