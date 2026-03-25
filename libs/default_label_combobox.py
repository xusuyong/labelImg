from PyQt6.QtWidgets import QComboBox, QHBoxLayout, QWidget


class DefaultLabelComboBox(QWidget):
    def __init__(self, parent=None, items=None):
        super().__init__(parent)
        if items is None:
            items = []

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.items = items
        self.cb.addItems(self.items)
        layout.addWidget(self.cb)
        self.setLayout(layout)
