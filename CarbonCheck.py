from PyQt6.QtWidgets import QApplication, QLabel
import ph_units

app = QApplication([])
label = QLabel(f"{ph_units}")
label.show()
app.exec()
