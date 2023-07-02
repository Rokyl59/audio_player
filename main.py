import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider, QPushButton, QLabel, QWidget, QFileDialog, \
    QStyle, QSizePolicy, QHBoxLayout, QListWidget, QAbstractItemView, QLineEdit
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer, pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPalette, QColor, QPainter

class ScrollingLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scroll_speed = 100  # pixels per second
        self.scroll_timer = QTimer(self)
        self.scroll_timer.timeout.connect(self.scroll_text)
        self.scroll_position = self.width()

    def start_scroll(self, duration):
        self.scroll_position = self.width()
        self.scroll_timer.stop()
        if self.width() < self.fontMetrics().width(self.text()):
            self.scroll_timer.start(duration)

    def stop_scroll(self):
        self.scroll_timer.stop()

    def scroll_text(self):
        self.scroll_position -= self.scroll_speed / 1000 * self.scroll_timer.interval()
        self.update()

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     painter.setPen(Qt.white)
    #     painter.setFont(self.font())
    #     text_width = self.fontMetrics().width(self.text())
    #     text_height = self.fontMetrics().height()
    #     painter.drawText(QRect(self.scroll_position, text_width, text_height), self.text())

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

        self.duration_timer = QTimer()
        self.duration_timer.setInterval(1000)  # Update duration every second
        self.duration_timer.timeout.connect(self.update_duration)

    def setup_ui(self):
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.play_button = QPushButton()
        self.stop_button = QPushButton()
        self.previous_button = QPushButton()
        self.next_button = QPushButton()
        self.open_button = QPushButton("Open Folder")
        self.playlist_widget = QListWidget()
        self.playlist_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.playlist_widget.setSpacing(5)
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.duration_label = QLabel("00:00 / 00:00")
        self.scroll_label = ScrollingLabel()

        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.previous_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.next_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))

        main_layout = QVBoxLayout()
        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.previous_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.next_button)

        search_layout = QHBoxLayout()
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        main_layout.addWidget(self.volume_slider)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.open_button)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.playlist_widget)
        main_layout.addWidget(self.duration_label)
        main_layout.addWidget(self.scroll_label)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def update_song_name(self, song_name):
        self.scroll_label.setText(song_name)
        self.scroll_label.start_scroll(200)

    def setup_player(self):
        self.media_player.setVolume(self.volume_slider.value())

    def update_scroll_label(self, song_name):
        self.scroll_label.setText(song_name)
        self.scroll_label.start_scroll(5000)

    def setup_signals(self):
        self.play_button.clicked.connect(self.play)
        self.stop_button.clicked.connect(self.stop)
        self.previous_button.clicked.connect(self.previous)
        self.next_button.clicked.connect(self.next)
        self.open_button.clicked.connect(self.open_folder)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.media_player.mediaStatusChanged.connect(self.media_status_changed)
        self.playlist_widget.itemDoubleClicked.connect(self.change_song)
        self.search_button.clicked.connect(self.search)
        self.search_input.textChanged.connect(self.filter_playlist)
        self.song_changed.connect(self.update_scroll_label)
        self.song_changed.connect(self.update_song_name)

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            if self.media_player.state() == QMediaPlayer.StoppedState:
                if len(self.filtered_playlist) > 0:
                    self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
                    self.media_player.play()
                    song_path = self.filtered_playlist[self.current_index]
                    song_name = os.path.basename(song_path)
                    self.update_scroll_label(song_name)
                    self.duration_timer.start()

            else:
                self.media_player.play()
                self.scroll_label.start_scroll(200)  # Start scrolling label with a duration of 200 milliseconds
                self.duration_timer.start()

    def stop(self):
        self.media_player.stop()
        self.scroll_label.stop_scroll()
        self.duration_timer.stop()
        self.slider.setValue(0)
        self.update_duration()

    def previous(self):
        self.current_index = (self.current_index - 1) % len(self.filtered_playlist)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
        song_path = self.filtered_playlist[self.current_index]
        song_name = os.path.basename(song_path)
        self.update_scroll_label(song_name)
        self.media_player.play()
        self.duration_timer.start()

    def next(self):
        self.current_index = (self.current_index + 1) % len(self.filtered_playlist)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
        song_path = self.filtered_playlist[self.current_index]
        song_name = os.path.basename(song_path)
        self.update_scroll_label(song_name)
        self.media_player.play()
        self.duration_timer.start()

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
            self.scroll_label.start_scroll(200)  # Start scrolling label with a duration of 200 milliseconds
            self.duration_timer.start()

    def update_duration(self):
        if self.media_player.duration() > 0:
            current_time = self.media_player.position() // 1000
            total_time = self.media_player.duration() // 1000
            current_time_string = "{:02d}:{:02d}".format(current_time // 60, current_time % 60)
            total_time_string = "{:02d}:{:02d}".format(total_time // 60, total_time % 60)
            self.duration_label.setText(f"{current_time_string} / {total_time_string}")
        else:
            self.duration_label.setText("00:00 / 00:00")

    def set_volume(self, volume):
        self.media_player.setVolume(volume)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next()

    song_changed = pyqtSignal(str)

    def change_song(self):
        self.current_index = self.playlist_widget.currentRow()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filtered_playlist[self.current_index])))
        self.media_player.play()
        self.scroll_label.start_scroll(200)  # Start scrolling label with a duration of 200 milliseconds
        self.duration_timer.start()
        
        # Отправить сигнал с полным именем текущей песни
        song_path = self.filtered_playlist[self.current_index]
        song_name = os.path.basename(song_path)
        self.song_changed.emit(song_name)
        self.scroll_label.stop_scroll()


    def search(self):
        keyword = self.search_input.text()
        self.filtered_playlist = [song for song in self.media_playlist if keyword.lower() in song.lower()]
        self.playlist_widget.clear()
        for song_path in self.filtered_playlist:
            song_name = os.path.basename(song_path)
            self.playlist_widget.addItem(song_name)

    def filter_playlist(self, keyword):
        self.filtered_playlist = [song for song in self.media_playlist if keyword.lower() in song.lower()]
        self.playlist_widget.clear()
        for song_path in self.filtered_playlist:
            song_name = os.path.basename(song_path)
            self.playlist_widget.addItem(song_name)

def run_application():
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec_())


