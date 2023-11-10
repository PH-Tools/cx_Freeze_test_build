from PyQt6.QtWidgets import QApplication, QLabel

import honeybee
import ladybug
import ladybug_rhino
import honeybee_energy
import honeybee_ph
import PHX
import ph_units
import ph_baseliner

app = QApplication([])
label = QLabel(f"This is a test: {ph_units}")
label.show()
app.exec()
