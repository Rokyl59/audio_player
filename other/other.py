import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QMessageBox, QStyle, QMenu, QAction
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon, QPixmap
import random
from Interface import Ui_MainWindow
from functions.utils import Folders, Playliste, Multimedia
from translations.update_language import Translate