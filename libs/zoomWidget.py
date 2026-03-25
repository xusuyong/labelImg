from PyQt6.QtWidgets import QSpinBox


class ZoomWidget(QSpinBox):
    def __init__(self, value=100):
        super().__init__()
        self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.setRange(1, 500)
        self.setSuffix(" %")
