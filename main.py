import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider, QPushButton, QLabel, QWidget, QFileDialog, \
    QStyle, QSizePolicy, QHBoxLayout, QListWidget, QAbstractItemView, QMessageBox, QLineEdit
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtGui import QIcon



class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio Player")
        self.setWindowIcon(QIcon("ico.ico"))
        self.setGeometry(100, 100, 600, 400)

        self.media_player = QMediaPlayer()
        self.media_playlist = []
        self.filtered_playlist = []
        self.current_index = 0

        self.setup_ui()
        self.setup_player()
        self.setup_signals()

    def setup_ui(self):
        # Создаем виджеты
        self.label = QLabel("Выберите файл")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.play_button = QPushButton()
        self.stop_button = QPushButton()
        self.previous_button = QPushButton()
        self.next_button = QPushButton()
        self.open_button = QPushButton("Открыть папку")
        self.playlist_widget = QListWidget()
        self.playlist_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.playlist_widget.setSpacing(5)
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Поиск")

        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.previous_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.next_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))

        # Создаем главный вертикальный layout
        main_layout = QVBoxLayout()

        # Создаем вертикальный layout для кнопок воспроизведения
        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.previous_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.next_button)

        # Создаем горизонтальный layout для ползунков громкости и позиции
        sliders_layout = QHBoxLayout()
        sliders_layout.setContentsMargins(0, 0, 0, 0)
        sliders_layout.addWidget(self.volume_slider)
        sliders_layout.addWidget(self.slider)

        # Создаем горизонтальный layout для строки поиска и кнопки
        search_layout = QHBoxLayout()
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # Добавляем виджеты в главный layout
        main_layout.addWidget(self.label)
        main_layout.addLayout(sliders_layout)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.open_button)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.playlist_widget)

        # Создаем виджет и устанавливаем layout
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def setup_player(self):
        self.media_player.setVolume(self.volume_slider.value())

    def setup_signals(self):
        self.play_button.clicked.connect(self.play)
        self.stop_button.clicked.connect(self.stop)
        self.previous_button.clicked.connect(self.previous)
        self.next_button.clicked.connect(self.next)
        self.open_button.clicked.connect(self.open_folder)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.slider.sliderMoved.connect(self.set_position)
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.mediaStatusChanged.connect(self.media_status_changed)
        self.playlist_widget.itemDoubleClicked.connect(self.change_song)
        self.search_button.clicked.connect(self.search)
        self.search_input.textChanged.connect(self.filter_playlist)

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            if self.media_player.state() == QMediaPlayer.StoppedState:
                if len(self.filtered_playlist) > 0:
                    self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
                    self.media_player.play()
            else:
                self.media_player.play()

    def stop(self):
        self.media_player.stop()

    def previous(self):
        self.current_index = (self.current_index - 1) % len(self.filtered_playlist)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
        self.media_player.play()

    def next(self):
        self.current_index = (self.current_index + 1) % len(self.filtered_playlist)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
        self.media_player.play()

    def open_folder(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        if folder_dialog.exec_():
            folder_path = folder_dialog.selectedFiles()[0]
            self.load_folder(folder_path)

    def load_folder(self, folder_path):
        self.media_playlist.clear()
        self.filtered_playlist.clear()
        self.playlist_widget.clear()

        for file_name in os.listdir(folder_path):
            if file_name.endswith(".mp3") or file_name.endswith(".wav"):
                self.media_playlist.append(os.path.join(folder_path, file_name))
                self.filtered_playlist.append(os.path.join(folder_path, file_name))
                self.playlist_widget.addItem(file_name)

        if len(self.filtered_playlist) > 0:
            self.current_index = 0
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
            self.media_player.play()

    def change_song(self, item):
        row = self.playlist_widget.row(item)
        if row != self.current_index:
            self.current_index = row
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
            self.media_player.play()

    def set_volume(self, volume):
        self.media_player.setVolume(volume)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_slider(self, position):
        self.slider.setValue(position)

    def media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next()

    def search(self):
        query = self.search_input.text()
        if query:
            matching_items = self.playlist_widget.findItems(query, Qt.MatchContains)
            if matching_items:
                self.playlist_widget.setCurrentItem(matching_items[0])
                self.playlist_widget.scrollToItem(matching_items[0])
                self.current_index = self.playlist_widget.row(matching_items[0])
                self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
                self.media_player.play()

    def filter_playlist(self, text):
        if text:
            self.filtered_playlist = [song for song in self.media_playlist if text.lower() in song.lower()]
        else:
            self.filtered_playlist = self.media_playlist
        self.playlist_widget.clear()
        for file_path in self.filtered_playlist:
            file_name = os.path.basename(file_path)
            self.playlist_widget.addItem(file_name)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Закрыть', 'Вы уверены, что хотите закрыть приложение?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec_())
