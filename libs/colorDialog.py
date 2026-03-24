from PyQt6.QtWidgets import QColorDialog, QDialogButtonBox

BB = QDialogButtonBox


class ColorDialog(QColorDialog):
    def __init__(self, parent=None):
        super(ColorDialog, self).__init__(parent)
        self.setOption(QColorDialog.ColorDialogOption.ShowAlphaChannel)
