from PyQt6.QtWidgets import QComboBox, QHBoxLayout, QWidget


class DefaultLabelComboBox(QWidget):
    def __init__(self, parent=None, items=[]):
        super(DefaultLabelComboBox, self).__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.items = items
        self.cb.addItems(self.items)
