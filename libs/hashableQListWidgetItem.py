#!/usr/bin/env python
from PyQt6.QtWidgets import QListWidgetItem


class HashableQListWidgetItem(QListWidgetItem):
    def __init__(self, *args):
        super().__init__(*args)
        self._hash = hash(id(self))

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return self is other
