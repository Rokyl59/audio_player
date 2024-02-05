import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QMessageBox, QStyle
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon, QPixmap
import random
from Interface import Ui_MainWindow
from translations.language import EN_TRANSLATIONS, RU_TRANSLATIONS

class Translate:
    @staticmethod
    def update_ui_language(self):
        translations = EN_TRANSLATIONS if self.current_language == self.ENGLISH else RU_TRANSLATIONS
        self.ui.open_folder_button.setToolTip(translations["Open folder"])
        self.ui.open_file_button.setToolTip(translations["Open file"])
        self.ui.save_playlist_button.setToolTip(translations["Save playlist"])
        self.ui.open_playlist_button.setToolTip(translations["Open playlist"])
        self.ui.delete_playlist.setToolTip(translations["Delete playlist"])
        self.ui.search_line_edit.setPlaceholderText(translations["Search"])
        self.ui.duration_label.setText(translations["00:00"])
        self.ui.duration_label_2.setText(translations["00:00"])
        self.ui.language_button.setToolTip(translations["Switch language"])
        self.ui.sound_button.setToolTip(translations["Mute"])
        self.ui.previous_button.setToolTip(translations["Previous"])
        self.ui.pre_button.setToolTip(translations["- 15"])
        self.ui.play_button.setToolTip(translations["Play"])
        self.ui.forw_button.setToolTip(translations["+ 15 "])
        self.ui.following_button.setToolTip(translations["Following"])
        self.ui.shuffle_button.setToolTip(translations["Shuffle"])
        self.ui.replay_button.setToolTip(translations["Replay"])
        self.ui.sound_menu_button.setToolTip(translations["Additional parameters"])
        self.ui.change_theme_button.setToolTip(translations["Change theme"])

    @staticmethod
    def switch_language(self):
        if self.current_language == self.ENGLISH:
            self.current_language = self.RUSSIAN
        else:
            self.current_language = self.ENGLISH
        self.update_ui_language()
