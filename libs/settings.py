import os
from enum import Enum

import yaml

from libs.logger import logger


def convert_qt_type(obj):
    """Convert Qt types and Enum types to YAML-serializable types"""
    from PyQt6.QtCore import QByteArray, QPoint, QSize
    from PyQt6.QtGui import QColor

    if isinstance(obj, Enum):
        return {"__type__": obj.__class__.__name__, "value": obj.value}
    elif isinstance(obj, QSize):
        return {"__type__": "QSize", "width": obj.width(), "height": obj.height()}
    elif isinstance(obj, QPoint):
        return {"__type__": "QPoint", "x": obj.x(), "y": obj.y()}
    elif isinstance(obj, QByteArray):
        return {"__type__": "QByteArray", "data": obj.toBase64().data().decode("ascii")}
    elif isinstance(obj, QColor):
        return {
            "__type__": "QColor",
            "red": obj.red(),
            "green": obj.green(),
            "blue": obj.blue(),
            "alpha": obj.alpha(),
        }
    elif isinstance(obj, (list, tuple)):
        return [convert_qt_type(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_qt_type(val) for key, val in obj.items()}
    return obj


def convert_from_yaml(obj):
    """Convert YAML-serializable types back to Qt types"""
    from PyQt6.QtCore import QByteArray, QPoint, QSize
    from PyQt6.QtGui import QColor

    from libs.labelFile import LabelFileFormat

    if isinstance(obj, dict):
        if obj.get("__type__") == "LabelFileFormat":
            return LabelFileFormat(obj["value"])
        elif obj.get("__type__") == "QSize":
            return QSize(obj["width"], obj["height"])
        elif obj.get("__type__") == "QPoint":
            return QPoint(obj["x"], obj["y"])
        elif obj.get("__type__") == "QByteArray":
            return QByteArray.fromBase64(obj["data"].encode("ascii"))
        elif obj.get("__type__") == "QColor":
            return QColor(obj["red"], obj["green"], obj["blue"], obj["alpha"])
        else:
            return {key: convert_from_yaml(val) for key, val in obj.items()}
    elif isinstance(obj, list):
        return [convert_from_yaml(item) for item in obj]
    return obj


class Settings:
    def __init__(self):
        home = os.path.expanduser("~")
        self.data = {}
        self.path = os.path.join(home, ".NineSkyLabelImgSettings.yaml")

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def get(self, key, default=None):
        if key in self.data:
            return self.data[key]
        return default

    def save(self):
        if self.path:
            with open(self.path, "w", encoding="utf-8") as f:
                yaml.dump(
                    convert_qt_type(self.data),
                    f,
                    default_flow_style=False,
                    allow_unicode=True,
                )
                logger.info(f"Settings saved to {self.path}")
                return True
        return False

    def load(self):
        try:
            if os.path.exists(self.path):
                with open(self.path, encoding="utf-8") as f:
                    self.data = convert_from_yaml(yaml.safe_load(f))
                    logger.info(f"Settings loaded from {self.path}")
                    return True
        except Exception as e:
            logger.error(f"Loading setting failed: {e}")
        return False

    def reset(self):
        if os.path.exists(self.path):
            os.remove(self.path)
            logger.info(f"Remove setting yaml file {self.path}")
        self.data = {}
        self.path = None
