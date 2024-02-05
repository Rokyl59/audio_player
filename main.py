import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QMessageBox, QStyle, QMenu, QAction, QDialog
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon, QPixmap
import random
from Interface import Ui_MainWindow
from functions.utils import Folders, Playliste, Multimedia
from translations.update_language import Translate
import pickle

class MainWindow(QMainWindow):
    ENGLISH = "en"
    RUSSIAN = "ru"
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        style_sheet_file = "style/default.qss"
        with open(style_sheet_file, "r") as f:
            self.setStyleSheet(f.read())

        self.media_player = QMediaPlayer()
        self.media_playlist = []
        self.filtered_playlist = []
        self.current_index = 0
        self.current_position = 0

        self.duration_timer = QTimer()
        self.duration_timer.setInterval(1000)  
        self.duration_timer.timeout.connect(self.update_duration)

        self.replay_mode = False
        self.media_initialized = False
        self.playing = False
        self.muted = True
        
        self.current_language = self.ENGLISH  
        self.update_ui_language()

        self.load_state()
        self.setup_signals()
        self.update_play_button_icon()

    def save_state(self):
        state = {
            "last_playlist": [(item.text(), item.data(Qt.UserRole)) for item in self.filtered_playlist],
            "last_track_index": self.current_index,
            "current_language": self.current_language,
            # Add other data you want to save, e.g., selected theme, etc.
        }

        with open("app_state.pkl", "wb") as f:
            pickle.dump(state, f)

    def load_state(self):
        try:
            with open("app_state.pkl", "rb") as f:
                state = pickle.load(f)

            track_data_list = state.get("last_playlist", [])
            self.filtered_playlist = [QListWidgetItem(name) for name, path in track_data_list]
            for item, (_, path) in zip(self.filtered_playlist, track_data_list):
                item.setData(Qt.UserRole, path)

            self.current_index = state.get("last_track_index", 0)
            self.current_language = state.get("current_language", self.ENGLISH)
            # Load other data you want to restore, e.g., selected theme, etc.

            if self.filtered_playlist:
                self.ui.playlist_widget.clear()
                self.ui.playlist_widget.addItems([item.text() for item in self.filtered_playlist])
                self.play_track(self.current_index)
                self.media_player.stop()

            self.update_ui_language()  # Update the interface based on the current language
            # Update other states you want to restore, e.g., selected theme, etc.
        except FileNotFoundError:
            pass  # File not found, ignore and continue

        # Add handling for other exceptions that may occur during state loading

    def closeEvent(self, event):
        self.save_state()
        super().closeEvent(event)

    def setup_signals(self):
        self.ui.open_folder_button.clicked.connect(self.open_folder)
        self.ui.open_file_button.clicked.connect(self.open_file)
        self.ui.save_playlist_button.clicked.connect(self.save_playlist)
        self.ui.open_playlist_button.clicked.connect(self.open_playlist)
        self.ui.search_line_edit.textChanged.connect(self.filter_playlist)
        self.ui.duration_slider.sliderMoved.connect(self.seek_track)
        self.ui.sound_button.clicked.connect(self.volume_mute)
        self.ui.volume_slider.valueChanged.connect(self.set_volume)
        self.ui.play_button.clicked.connect(self.play)
        self.ui.previous_button.clicked.connect(self.previous)
        self.ui.following_button.clicked.connect(self.next)
        self.ui.pre_button.clicked.connect(self.seek_backward)
        self.ui.forw_button.clicked.connect(self.seek_forward)
        self.ui.playlist_widget.itemClicked.connect(lambda item: self.play_track(self.ui.playlist_widget.row(item)))
        self.media_player.mediaStatusChanged.connect(self.handle_media_status_changed)
        self.ui.shuffle_button.clicked.connect(self.shuffle_tracks)
        self.ui.delete_playlist.clicked.connect(self.delete_playlist)
        self.ui.replay_button.clicked.connect(self.toggle_replay_mode)
        self.ui.language_button.clicked.connect(self.switch_language)
        self.ui.sound_menu_button.clicked.connect(self.show_sound_menu)
        self.ui.change_theme_button.clicked.connect(self.show_theme_menu)
        self.ui.playlist_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.playlist_widget.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, point):
        # Создаем контекстное меню
        context_menu = QMenu(self)

        # Добавляем опцию удаления трека
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_track)
        context_menu.addAction(delete_action)

        # Показываем контекстное меню в точке нажатия правой кнопкой мыши
        context_menu.exec_(self.ui.playlist_widget.mapToGlobal(point))

    def delete_track(self):
        # Получаем выделенный трек из плейлиста
        selected_item = self.ui.playlist_widget.currentItem()
        if selected_item:
            row = self.ui.playlist_widget.row(selected_item)

            # Удаляем трек из плейлиста
            if row >= 0 and row < len(self.filtered_playlist):
                del self.filtered_playlist[row]
                self.update_duration()

                # Если удаляем трек, который находится перед текущим индексом,
                # уменьшаем текущий индекс на 1
                if row < self.current_index:
                    self.current_index -= 1

                # Удаляем выделенный трек из виджета плейлиста
                self.ui.playlist_widget.takeItem(row)

                # Если после удаления плейлист стал пустым, останавливаем проигрывание
                if not self.filtered_playlist:
                    self.stop()
                else:
                    # Если текущий индекс больше или равен длине плейлиста,
                    # устанавливаем текущий индекс в конец плейлиста минус 1
                    if self.current_index >= len(self.filtered_playlist):
                        self.current_index = len(self.filtered_playlist) - 1

                    # Воспроизводим трек с обновленным индексом
                    self.play_track(self.current_index)

    def show_equalizer_dialog(self):
        multimediautils = Multimedia()
        multimediautils.show_equalizer_dialog(self)

    def show_sound_menu(self):
        multimediautils = Multimedia()
        multimediautils.show_sound_menu(self)

    def show_theme_menu(self):
        multimediautils = Multimedia()
        multimediautils.show_theme_menu(self)

    def option2_suboption1_action(self):
        multimediautils = Multimedia()
        multimediautils.option2_suboption1_action(self)

    def option2_suboption2_action(self):
        multimediautils = Multimedia()
        multimediautils.option2_suboption2_action(self)

    def option2_suboption3_action(self):
        multimediautils = Multimedia()
        multimediautils.option2_suboption3_action(self)

    def option1_suboption1_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption1_action(self)

    def option1_suboption2_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption2_action(self)

    def option1_suboption3_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption3_action(self)

    def option1_suboption4_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption4_action(self)

    def option1_suboption5_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption5_action(self)

    def option1_suboption6_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption6_action(self)

    def option1_suboption7_action(self):
        multimediautils = Multimedia()
        multimediautils.option1_suboption7_action(self)

    def change_playback_speed(self, speed):
        multimediautils = Multimedia()
        multimediautils.change_playback_speed(self, speed)

    def handle_media_status_changed(self, status):
        playlistutils = Playliste()
        playlistutils.handle_media_status_changed(self, status)

    def set_volume(self, volume):
        multimediautils = Multimedia()
        multimediautils.set_volume(self, volume)

    def volume_mute(self):
        multimediautils = Multimedia()
        multimediautils.volume_mute(self)

    def update_duration(self):
        multimediautils = Multimedia()
        multimediautils.update_duration(self)

    def seek_track(self, position):
        multimediautils = Multimedia()
        multimediautils.seek_track(self, position)

    def format_time(self, time_seconds):
        minutes = int(time_seconds / 60)
        seconds = int(time_seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def toggle_replay_mode(self):
        multimediautils = Multimedia()
        multimediautils.toggle_replay_mode(self)

    def shuffle_tracks(self):
        if self.filtered_playlist and self.current_index >= 0 and self.current_index < len(self.filtered_playlist):
            random.shuffle(self.filtered_playlist)
            self.ui.playlist_widget.clear()
            self.ui.playlist_widget.addItems([item.text() for item in self.filtered_playlist])
            self.current_index = 0
            self.play_track()
            self.update_playlist_selection()
            self.ui.song_label.setText(self.filtered_playlist[self.current_index].text())
        else:
            print("No tracks")

    def filter_playlist(self, keyword):
        playlistutils = Playliste()
        playlistutils.filter_playlist(self, keyword)

    def open_folder(self):
        foldersutils = Folders()
        foldersutils.open_folder(self)

    def open_file(self):
        foldersutils = Folders()
        foldersutils.open_file(self)

    def load_playlist(self, folder_path=None, track_paths=None):
        folders_utils = Folders()  
        folders_utils.load_playlist(self, folder_path, track_paths)  

    def save_playlist(self):
        foldersutils = Folders()
        foldersutils.save_playlist(self)

    def open_playlist(self):
        foldersutils = Folders()
        foldersutils.open_playlist(self)

    def play(self):
        multimediautils = Multimedia()
        multimediautils.play(self)
        
    def update_play_button_icon(self):
        multimediautils = Multimedia()
        multimediautils.update_play_button_icon(self)
        
    def previous(self):
        multimediautils = Multimedia()
        multimediautils.previous(self)

    def next(self):
        multimediautils = Multimedia()
        multimediautils.next(self)

    def seek_forward(self):
        multimediautils = Multimedia()
        multimediautils.seek_forward(self) 

    def seek_backward(self):
        multimediautils = Multimedia()
        multimediautils.seek_backward(self) 

    def play_track(self, index=None):
        multimediautils = Multimedia()
        multimediautils.play_track(self, index)

    def delete_playlist(self):
        foldersutils = Folders()
        foldersutils.delete_playlist(self)

    def update_playlist_selection(self):
        playlistutils = Playliste()
        playlistutils.update_playlist_selection(self)

    def switch_language(self):
        translation = Translate()
        translation.switch_language(self)

    def update_ui_language(self):
        translation = Translate()
        translation.update_ui_language(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Audio Player")
    window.setWindowIcon(QIcon("logo/ico.ico"))
    window.show()

    sys.exit(app.exec_())
