from PyQt6.QtWidgets import QApplication, QLabel
import ph_units

app = QApplication([])
label = QLabel(f"This is a test: {ph_units}")
label.show()
app.exec()
