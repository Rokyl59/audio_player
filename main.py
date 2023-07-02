import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QSlider, QPushButton, QLabel, QWidget, QFileDialog,
    QStyle, QSizePolicy, QHBoxLayout, QListWidget, QAbstractItemView, QLineEdit, QListWidgetItem
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer, pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPalette, QColor, QPainter, QLinearGradient

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

        self.playing = False  # Флаг состояния воспроизведения
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)

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
        self.search_button = QPushButton()
        search_icon = QIcon("search.png")  # Замените "search_icon.png" на путь к вашей иконке поиска
        self.search_button.setIcon(search_icon)
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
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        main_layout.addWidget(self.open_button)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.volume_slider)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.playlist_widget)
        main_layout.addWidget(self.duration_label)
        main_layout.addWidget(self.scroll_label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

         # Добавьте следующий код для создания скругленных краев
        self.setStyleSheet("border-radius: 10px;")

        # Установка главного макета
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        # Стиль для элементов списка плейлиста
        self.playlist_widget.setStyleSheet("""
        QListWidget {
            background-color: #353535;
            padding: 5px;
            border: none;
            border-radius: 10px;
        }

        QListWidget::item {
            background-color: #353535;
            padding: 5px;
            border: none;
            border-radius: 10px;
        }

        QListWidget::item:hover {
            background-color: #5d3990;
        }

        QListWidget::item:selected {
            background-color: #6b47a8;
        }
        """)

        # Стиль для полосы прокрутки
        self.playlist_widget.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            background-color: #3f3f3f;
            width: 15px;
            border-radius: 7px;
        }

        QScrollBar::handle:vertical {
            background-color: #6b47a8;
            border-radius: 7px;
        }

        QScrollBar::handle:vertical:hover {
            background-color: #5d3990;
        }

        QScrollBar::sub-line:vertical,
        QScrollBar::add-line:vertical {
            background-color: #3f3f3f;
            height: 15px;
            border-radius: 7px;
        }

        QScrollBar::sub-line:vertical:hover,
        QScrollBar::add-line:vertical:hover {
            background-color: #5d3990;
        }
        """)
        self.playlist_widget.horizontalScrollBar().setStyleSheet("""
        QScrollBar:horizontal {
            background-color: #3f3f3f;
            border-radius: 7px;
        }

        QScrollBar::handle:horizontal {
            background-color: #6b47a8;
            border-radius: 7px;
        }

        QScrollBar::handle:horizontal:hover {
            background-color: #5d3990;
        }

        QScrollBar::sub-line:horizontal,
        QScrollBar::add-line:horizontal {
            background-color: #3f3f3f;
            border-radius: 7px;
        }

        QScrollBar::sub-line:horizontal:hover,
        QScrollBar::add-line:horizontal:hover {
            background-color: #5d3990;
        }
        """)
        # Стиль для полосы изменения громкости
        self.volume_slider.setStyleSheet("""
        QSlider::groove:horizontal {
            background-color: grey;
            height: 4px;
            border-radius: 2px;
        }

        QSlider::sub-page:horizontal {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                              stop:0 #8a2be2, stop:1 #800080);
            border-radius: 2px;
        }

        QSlider::handle:horizontal {
            background-color: #ffffff;
            border: none;
            width: 10px;
            height: 10px;
            margin: -3px 0;
            border-radius: 5px;
        }
        """)
        # Стиль для поля ввода поиска
        self.search_input.setStyleSheet("""
        QLineEdit {
            background-color: #6b47a8;
            border-radius: 5px;
            padding: 5px;
        }
        """)
         # Уменьшение высоты поля ввода поиска
        self.search_input.setFixedHeight(20)

        # Уменьшение высоты кнопки поиска
        self.search_button.setFixedHeight(20)

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next()

    def setup_player(self):
        self.media_player.setVolume(self.volume_slider.value())

    def setup_signals(self):
        self.volume_slider.valueChanged.connect(self.media_player.setVolume)
        self.play_button.clicked.connect(self.play)
        self.stop_button.clicked.connect(self.stop)
        self.previous_button.clicked.connect(self.previous)
        self.next_button.clicked.connect(self.next)
        self.open_button.clicked.connect(self.open_folder)
        self.media_player.stateChanged.connect(self.update_buttons)
        self.playlist_widget.currentItemChanged.connect(self.change_track)
        self.search_button.clicked.connect(self.filter_playlist)

    def play(self):
        if self.playing:
            self.media_player.pause()
        else:
            self.media_player.play()

    def stop(self):
        self.media_player.stop()

    def previous(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.filtered_playlist) - 1
        self.play_track()

    def next(self):
        self.current_index += 1
        if self.current_index >= len(self.filtered_playlist):
            self.current_index = 0
        self.play_track()
        self.update_playlist_selection()
    
    def update_playlist_selection(self):
        # Снять выделение с предыдущего трека
        previous_item = self.playlist_widget.item(self.current_index - 1)
        if previous_item:
            previous_item.setSelected(False)

        # Выделить текущий трек
        current_item = self.playlist_widget.item(self.current_index)
        if current_item:
            current_item.setSelected(True)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder")
        if folder_path:
            self.load_playlist(folder_path)

    def load_playlist(self, folder_path):
        self.media_playlist = []
        self.filtered_playlist = []
        self.playlist_widget.clear()

        for file_name in os.listdir(folder_path):
            if file_name.endswith(".mp3"):
                full_path = os.path.join(folder_path, file_name)
                item = QListWidgetItem(file_name)
                item.setData(Qt.UserRole, full_path)
                self.media_playlist.append(item)
                self.filtered_playlist.append(item.clone())

        playlist_names = [item.text() for item in self.media_playlist]  # Получение списка имён песен
        self.playlist_widget.addItems(playlist_names)  # Передача списка имён песен вместо self.media_playlist

        self.current_index = 0
        self.play_track()

    def change_track(self, current_item, previous_item):
        if current_item:
            self.current_index = self.playlist_widget.currentRow()
            self.play_track()

    def play_track(self):
        if self.current_index >= 0 and self.current_index < len(self.filtered_playlist):
            track_path = self.filtered_playlist[self.current_index].data(Qt.UserRole)
            media_content = QMediaContent(QUrl.fromLocalFile(track_path))
            self.media_player.setMedia(media_content)
            self.playing = True
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.media_player.play()
            self.duration_timer.start()

    def update_buttons(self, state):
        if state == QMediaPlayer.PlayingState:
            self.playing = True
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.duration_timer.start()
        else:
            self.playing = False
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.duration_timer.stop()

    def update_duration(self):
        if self.media_player.duration() > 0:
            duration = self.media_player.duration() / 1000
            position = self.media_player.position() / 1000
            self.duration_label.setText(
                f"{self.format_time(position)} / {self.format_time(duration)}"
            )

    def format_time(self, time_seconds):
        minutes = int(time_seconds / 60)
        seconds = int(time_seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def filter_playlist(self):
        keyword = self.search_input.text().lower()
        if keyword:
            self.filtered_playlist = [
                item for item in self.media_playlist if keyword in item.text().lower()
            ]
        else:
            self.filtered_playlist = self.media_playlist[:]
        self.playlist_widget.clear()
        self.playlist_widget.addItems(self.filtered_playlist)
        self.current_index = 0
        self.play_track()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Установка стиля "Fusion"

    dark_palette = QPalette()  # Создание палитры цветов для темной версии
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setPalette(dark_palette)  # Установка темной палитры цветов

    app.setStyleSheet("""
        /* Основной стиль для всего приложения */
        QWidget {
            background-color: #353535;
            color: #ffffff;
        }

        /* Стиль для кнопок */
        QPushButton {
            background-color: #6b47a8;
            color: #ffffff;
            border: none;
            padding: 5px 10px;
            border-radius: 15px;  /* Добавляем скругленные углы */
        }

        QPushButton:hover {
            background-color: #5d3990;
        }

        QPushButton:pressed {
            background-color: #4e3278;
        }

        /* Стиль для панели прокрутки */
        QScrollBar:vertical {
            background-color: #3f3f3f;
            width: 15px;
            border-radius: 15px;  /* Добавляем скругленные углы */
        }

        QScrollBar::handle:vertical {
            background-color: #6b47a8;
            border-radius: 15px;  /* Добавляем скругленные углы */
        }

        QScrollBar::handle:vertical:hover {
            background-color: #5d3990;
        }

        QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
            background-color: #3f3f3f;
            height: 15px;
            border-radius: 15px;  /* Добавляем скругленные углы */
        }

        QScrollBar::sub-line:vertical:hover, QScrollBar::add-line:vertical:hover {
            background-color: #5d3990;
        }

        /* Стиль для элементов списка плейлиста */
        QListWidget::item {
            background-color: #353535;
            padding: 5px;
            border: none;  /* Убираем границу элемента */
            border-radius: 15px;  /* Добавляем скругленные углы */
        }

        QListWidget::item:hover {
            background-color: #5d3990;
        }

        QListWidget::item:selected {
            background-color: #6b47a8;
        }

        /* Стиль для метки текущей играющей песни */
        QLabel#current_track_label {
            color: #ffffff;
            background-color: transparent;
            border: none;
        }
    """)

    window = AudioPlayer()
    window.show()

    sys.exit(app.exec_())
