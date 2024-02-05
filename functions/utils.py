import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QMessageBox, QStyle, QAction, QMenu, QDialog
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon, QPixmap
import random
from Interface import Ui_MainWindow
from gui.equalizer import Ui_Dialog

class Folders:
    
    @staticmethod
    def open_folder(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly)

        if folder_dialog.exec_():
            folder_paths = folder_dialog.selectedFiles()
            for folder_path in folder_paths:
                self.current_folder = folder_path
                self.load_playlist(folder_path)
    
    @staticmethod
    def open_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Music files (*.mp3 *.wav)")
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            self.load_playlist(track_paths=file_paths)
    
    @staticmethod
    def load_playlist(self, folder_path=None, track_paths=None):
        if folder_path:
            new_folder_tracks = []
            for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    if file_name.endswith(".mp3"):
                        full_path = os.path.join(root, file_name)
                        # Удаляем расширение из имени файла
                        track_name = os.path.splitext(file_name)[0]
                        item = QListWidgetItem(track_name)
                        item.setData(Qt.UserRole, full_path)
                        new_folder_tracks.append(item)

            self.media_playlist.extend(new_folder_tracks)

        if track_paths:
            new_tracks = []
            for file_path in track_paths:
                # Удаляем расширение из имени файла
                track_name = os.path.splitext(os.path.basename(file_path))[0]
                item = QListWidgetItem(track_name)
                item.setData(Qt.UserRole, file_path)
                new_tracks.append(item)

            self.media_playlist.extend(new_tracks)

        # Сортировка плейлиста в алфавитном порядке
        self.media_playlist.sort(key=lambda x: x.text())

        self.filtered_playlist = self.media_playlist
        self.update_duration()

        playlist_names = [item.text() for item in self.media_playlist]
        self.ui.playlist_widget.clear()
        self.ui.playlist_widget.addItems(playlist_names)

        self.update_play_button_icon()

    @staticmethod
    def save_playlist(self):
        if not self.filtered_playlist:
            return

        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Playlist files (*.m3u)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            try:
                with open(file_path, "w", encoding="utf-8") as f: 
                    for item in self.filtered_playlist:
                        file_path = item.data(Qt.UserRole)
                        f.write(file_path + "\n")

                QMessageBox.information(self, "Playlist Saved", "Playlist has been saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save playlist: {str(e)}")
    
    @staticmethod
    def open_playlist(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Playlist files (*.m3u)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            try:
                with open(file_path, "r", encoding="utf-8") as f:  
                    track_paths = [line.strip() for line in f.readlines()]

                self.load_playlist(track_paths=track_paths)
                QMessageBox.information(self, "Playlist Opened", "Playlist has been opened successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open playlist: {str(e)}")

    @staticmethod
    def delete_playlist(self):
        if self.filtered_playlist and 0 <= self.current_index < len(self.filtered_playlist):
            confirm_dialog = QMessageBox(self)
            confirm_dialog.setIcon(QMessageBox.Question)
            confirm_dialog.setWindowTitle("Delete Playlist")
            confirm_dialog.setText("Are you sure you want to delete the playlist?")
            confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_dialog.setDefaultButton(QMessageBox.No)

            if confirm_dialog.exec_() == QMessageBox.Yes:
                self.ui.playlist_widget.clear()
                self.filtered_playlist.clear()
                self.media_playlist.clear()
                self.current_index = 0
                self.media_initialized = False
                self.playing = False
                self.update_play_button_icon()
                self.ui.song_label.setText("")
                self.media_player.stop()

        else:
            return

class Playliste:

    @staticmethod
    def update_playlist_selection(self):
        previous_item = self.ui.playlist_widget.item(self.current_index - 1)
        if previous_item:
            previous_item.setSelected(False)

        current_item = self.ui.playlist_widget.item(self.current_index)
        if current_item:
            current_item.setSelected(True)

    @staticmethod
    def filter_playlist(self, keyword):
        keyword = keyword.lower()
        if keyword:
            self.filtered_playlist = [
                item for item in self.media_playlist if keyword.lower() in item.text().lower()
            ]
        else:
            self.filtered_playlist = self.media_playlist[:]

        current_item = self.ui.playlist_widget.currentItem()
        current_track = current_item.data(Qt.UserRole) if current_item else None
        self.ui.playlist_widget.clear()
        self.ui.playlist_widget.addItems([item.text() for item in self.filtered_playlist])
        if current_track:
            for index, item in enumerate(self.filtered_playlist):
                if item.data(Qt.UserRole) == current_track:
                    self.current_index = index
                    break
        else:
            self.current_index = 0

    @staticmethod
    def handle_media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            if self.replay_mode:
                self.media_player.setPosition(0)
                self.media_player.play()
            else:
                self.next()
                self.playing = True  
        self.update_play_button_icon()

class Multimedia:

    @staticmethod
    def set_volume(self, volume):
        self.media_player.setVolume(volume)

    @staticmethod
    def volume_mute(self):
        if self.muted:
            self.media_player.setMuted(True)  
            self.ui.volume_slider.setValue(0)
            self.ui.sound_button.setIcon(QIcon(":/icons/icons/volume-x.svg"))
            self.muted = False
        else:
            self.media_player.setMuted(False)  
            self.ui.volume_slider.setValue(50)
            self.ui.sound_button.setIcon(QIcon(":/icons/icons/volume-2.svg"))
            self.muted = True

    @staticmethod
    def update_duration(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            if self.media_player.duration() > 0:
                duration = self.media_player.duration() / 1000
                position = self.media_player.position() / 1000
                self.ui.duration_label.setText(
                    f"{self.format_time(position)}"
                )
                self.ui.duration_label_2.setText(
                    f"{self.format_time(duration)}"
                )
                progress = int((position / duration) * 100)
                self.ui.duration_slider.setRange(0, int(duration))
                self.ui.duration_slider.setValue(int(position))
        else:
            self.duration_timer.stop()

        QTimer.singleShot(10, self.update_duration)

    @staticmethod
    def seek_track(self, position):
        self.media_player.setPosition(position * 1000)
        self.duration_timer.start()

    @staticmethod
    def toggle_replay_mode(self):
        self.replay_mode = not self.replay_mode
    
    @staticmethod
    def play(self):
        if not self.filtered_playlist:
            return

        if not self.media_initialized:
            self.media_initialized = True
            self.play_track(self.current_index)
        else:
            if self.media_player.state() == QMediaPlayer.PlayingState:
                self.media_player.pause()
            else:
                self.media_player.play()

            self.playing = not self.playing 
            self.update_play_button_icon()
    
    @staticmethod
    def update_play_button_icon(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.ui.play_button.setIcon(QIcon(":/icons/icons/pause-circle.svg"))
        else:
            self.ui.play_button.setIcon(QIcon(":/icons/icons/play-circle.svg"))
        
    @staticmethod
    def previous(self):
        if self.ui.playlist_widget.count() > 0:
            self.current_index -= 1
            if self.current_index < 0:
                self.current_index = self.ui.playlist_widget.count() - 1
            self.play_track(self.current_index)
            self.ui.song_label.setText(self.filtered_playlist[self.current_index].text())
            self.update_playlist_selection()
            self.duration_timer.start() 
            self.update_play_button_icon()

    @staticmethod
    def next(self):
        if self.ui.playlist_widget.count() > 0:
            self.current_index += 1
            if self.current_index >= self.ui.playlist_widget.count():
                self.current_index = 0
            self.play_track(self.current_index)
            self.ui.song_label.setText(self.filtered_playlist[self.current_index].text()) 
            self.update_playlist_selection()
            self.duration_timer.start()
            self.update_play_button_icon()

    @staticmethod
    def seek_forward(self):
        position = self.media_player.position()
        self.media_player.setPosition(position + 15000)  

    @staticmethod
    def seek_backward(self):
        position = self.media_player.position()
        self.media_player.setPosition(position - 15000)  

    @staticmethod
    def play_track(self, index=None):
        if index is not None:
            self.current_index = index

        if self.filtered_playlist and 0 <= self.current_index < len(self.filtered_playlist):
            if self.media_player.state() == QMediaPlayer.PlayingState:
                self.media_player.stop()

            track_path = self.filtered_playlist[self.current_index].data(Qt.UserRole)
            media_content = QMediaContent(QUrl.fromLocalFile(track_path))
            self.media_player.setMedia(media_content)
            self.ui.song_label.setText(self.filtered_playlist[self.current_index].text())  

            self.media_initialized = True

            self.media_player.play()  

            self.update_playlist_selection()
            self.duration_timer.start()

            if self.replay_mode and self.current_index > 0:
                self.media_player.setPosition(0)

    @staticmethod
    def show_sound_menu(self):
        self.sound_menu = QMenu(self)
        # Add actions to the sound menu
        option1_menu = QMenu("Speed:", self)
        option1_menu.addAction("0.5", self.option1_suboption1_action)
        option1_menu.addAction("0.75", self.option1_suboption2_action)
        option1_menu.addAction("1", self.option1_suboption3_action)
        option1_menu.addAction("1.25", self.option1_suboption4_action)
        option1_menu.addAction("1.50", self.option1_suboption5_action)
        option1_menu.addAction("1.75", self.option1_suboption6_action)
        option1_menu.addAction("2", self.option1_suboption7_action)
        self.sound_menu.addMenu(option1_menu) 
        # self.sound_menu.addAction("Equalizer", self.show_equalizer_dialog)
        self.sound_menu.addSeparator()
        self.sound_menu.exec_(self.ui.sound_menu_button.mapToGlobal(self.ui.sound_menu_button.rect().bottomLeft()))

    @staticmethod
    def show_theme_menu(self):
        self.theme_menu = QMenu(self)
        option2_menu = QMenu("Theme", self)
        option2_menu.addAction("Default Theme", self.option2_suboption1_action)
        option2_menu.addAction("Blue Theme", self.option2_suboption2_action)
        option2_menu.addAction("Purple Theme", self.option2_suboption3_action)
        self.theme_menu.addMenu(option2_menu) 
        self.theme_menu.addSeparator()
        self.theme_menu.exec_(self.ui.change_theme_button.mapToGlobal(self.ui.change_theme_button.rect().bottomLeft()))

    @staticmethod
    def show_equalizer_dialog(self):
        equalizer_dialog = QDialog()
        equalizer_ui = Ui_Dialog()
        equalizer_ui.setupUi(equalizer_dialog)
        equalizer_dialog.setWindowTitle("Equalizer Settings")
        equalizer_dialog.setWindowIcon(QIcon("logo/ico.ico"))

        # Connect the default button to reset the sliders
        equalizer_ui.pushButton_2.clicked.connect(equalizer_ui.reset_sliders)

        equalizer_dialog.exec_()

    @staticmethod
    def option2_suboption1_action(self):
        self.ui.open_folder_button.setStyleSheet(open("style/default.qss").read())
        self.ui.open_file_button.setStyleSheet(open("style/default.qss").read())
        self.ui.save_playlist_button.setStyleSheet(open("style/default.qss").read())
        self.ui.open_playlist_button.setStyleSheet(open("style/default.qss").read())
        self.ui.delete_playlist.setStyleSheet(open("style/default.qss").read())
        self.ui.change_theme_button.setStyleSheet(open("style/default.qss").read())
        self.ui.search_line_edit.setStyleSheet(open("style/default.qss").read())
        self.ui.scrollArea.setStyleSheet(open("style/default.qss").read())
        self.ui.playlist_widget.setStyleSheet(open("style/default.qss").read())
        self.ui.song_label.setStyleSheet(open("style/default.qss").read())
        self.ui.duration_label.setStyleSheet(open("style/default.qss").read())
        self.ui.duration_label_2.setStyleSheet(open("style/default.qss").read())
        self.ui.duration_slider.setStyleSheet(open("style/default.qss").read())
        self.ui.language_button.setStyleSheet(open("style/default.qss").read())
        self.ui.sound_button.setStyleSheet(open("style/default.qss").read())
        self.ui.volume_slider.setStyleSheet(open("style/default.qss").read())
        self.ui.replay_button.setStyleSheet(open("style/default.qss").read())
        self.ui.shuffle_button.setStyleSheet(open("style/default.qss").read())
        self.ui.sound_menu_button.setStyleSheet(open("style/default.qss").read())
        self.ui.following_button.setStyleSheet(open("style/default.qss").read())
        self.ui.forw_button.setStyleSheet(open("style/default.qss").read())
        self.ui.play_button.setStyleSheet(open("style/default.qss").read())
        self.ui.pre_button.setStyleSheet(open("style/default.qss").read())
        self.ui.previous_button.setStyleSheet(open("style/default.qss").read())

        style_sheet_file = "style/default.qss"
        with open(style_sheet_file, "r") as f:
            self.setStyleSheet(f.read())

    @staticmethod
    def option2_suboption2_action(self):
        self.ui.open_folder_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.open_file_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.save_playlist_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.open_playlist_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.delete_playlist.setStyleSheet(open("style/blue.qss").read())
        self.ui.change_theme_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.search_line_edit.setStyleSheet(open("style/blue.qss").read())
        self.ui.scrollArea.setStyleSheet(open("style/blue.qss").read())
        self.ui.playlist_widget.setStyleSheet(open("style/blue.qss").read())
        self.ui.song_label.setStyleSheet(open("style/blue.qss").read())
        self.ui.duration_label.setStyleSheet(open("style/blue.qss").read())
        self.ui.duration_label_2.setStyleSheet(open("style/blue.qss").read())
        self.ui.duration_slider.setStyleSheet(open("style/blue.qss").read())
        self.ui.language_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.sound_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.volume_slider.setStyleSheet(open("style/blue.qss").read())
        self.ui.replay_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.shuffle_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.sound_menu_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.following_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.forw_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.play_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.pre_button.setStyleSheet(open("style/blue.qss").read())
        self.ui.previous_button.setStyleSheet(open("style/blue.qss").read())

        style_sheet_file = "style/blue.qss"
        with open(style_sheet_file, "r") as f:
            self.setStyleSheet(f.read())

    @staticmethod
    def option2_suboption3_action(self):
        self.ui.open_folder_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.open_file_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.save_playlist_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.open_playlist_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.delete_playlist.setStyleSheet(open("style/purple.qss").read())
        self.ui.change_theme_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.search_line_edit.setStyleSheet(open("style/purple.qss").read())
        self.ui.scrollArea.setStyleSheet(open("style/purple.qss").read())
        self.ui.playlist_widget.setStyleSheet(open("style/purple.qss").read())
        self.ui.song_label.setStyleSheet(open("style/purple.qss").read())
        self.ui.duration_label.setStyleSheet(open("style/purple.qss").read())
        self.ui.duration_label_2.setStyleSheet(open("style/purple.qss").read())
        self.ui.duration_slider.setStyleSheet(open("style/purple.qss").read())
        self.ui.language_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.sound_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.volume_slider.setStyleSheet(open("style/purple.qss").read())
        self.ui.replay_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.shuffle_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.sound_menu_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.following_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.forw_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.play_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.pre_button.setStyleSheet(open("style/purple.qss").read())
        self.ui.previous_button.setStyleSheet(open("style/purple.qss").read())

        style_sheet_file = "style/purple.qss"
        with open(style_sheet_file, "r") as f:
            self.setStyleSheet(f.read())

    @staticmethod
    def option1_suboption1_action(self):
        self.change_playback_speed(0.5)

    @staticmethod
    def option1_suboption2_action(self):
        self.change_playback_speed(0.75)

    @staticmethod
    def option1_suboption3_action(self):
        self.change_playback_speed(1)

    @staticmethod
    def option1_suboption4_action(self):
        self.change_playback_speed(1.25)

    @staticmethod
    def option1_suboption5_action(self):
        self.change_playback_speed(1.5)

    @staticmethod
    def option1_suboption6_action(self):
        self.change_playback_speed(1.75)

    @staticmethod
    def option1_suboption7_action(self):
        self.change_playback_speed(2)

    @staticmethod
    def change_playback_speed(self, speed):
        self.media_player.setPlaybackRate(speed)