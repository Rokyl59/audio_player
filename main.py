import sys
import os
import pickle 
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSlider, QPushButton, QLabel, QWidget, QFileDialog, QStyle, QSizePolicy, QHBoxLayout, QListWidget, QAbstractItemView, QLineEdit, QListWidgetItem, QProgressBar, QMenu, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer, pyqtSignal, QRect, QPropertyAnimation, QPoint, QEasingCurve, QObject, QLocale
from PyQt5.QtGui import QIcon, QPalette, QColor, QPainter, QLinearGradient, QCursor
from PyQt5.QtCore import QPropertyAnimation, QPoint
import random
from translations import *

class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_language = "ENGLISH"
        self.current_folder = ""
        self.current_index = 0

        if not os.path.exists("settings.pickle"):
            self.save_settings()

        try:
            self.load_settings()
        except FileNotFoundError:
            pass

        self.setWindowTitle(TRANSLATIONS[self.current_language]["window_title"])
        self.setWindowIcon(QIcon("ico.ico"))
        self.setGeometry(100, 100, 600, 400)

        self.media_player = QMediaPlayer()
        self.media_playlist = []
        self.filtered_playlist = []
        self.current_index = 0
        self.setup_ui()
        self.setup_menu()
        self.setup_player()
        self.setup_signals()

        self.duration_timer = QTimer()
        self.duration_timer.setInterval(1000)  
        self.duration_timer.timeout.connect(self.update_duration)

        self.playing = False  # Флаг состояния воспроизведения
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)

        self.update_translations()

        if self.current_folder:
            self.load_playlist(self.current_folder)
            self.playlist_widget.setCurrentRow(self.current_index)
            self.play_track()

        # Загрузка сохраненных настроек при запуске программы
        self.load_settings()

        self.media_player.setMedia(QMediaContent())  
        self.playing = False  # Сброс флага состояния воспроизведения
        self.update_buttons(self.media_player.state())  

    def setup_ui(self):
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.play_button = QPushButton()
        self.stop_button = QPushButton()
        self.previous_button = QPushButton()
        self.next_button = QPushButton()
        self.open_button = QPushButton(TRANSLATIONS[self.current_language]["open_folder_button"])
        self.playlist_widget = QListWidget()
        self.playlist_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.playlist_widget.setSpacing(5)
        self.search_input = QLineEdit()
        self.clear_button = QPushButton()
        self.clear_button.setIcon(QIcon("search.png"))  
        self.duration_label = QLabel("00:00")
        self.duration_label_two = QLabel("00:00")
        self.seek_forward_button = QPushButton()
        self.seek_backward_button = QPushButton()
        # Добавление ползунка положения позиции воспроизведения
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)
        self.song_label = QLabel()

        self.seek_forward_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.seek_backward_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.previous_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.next_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))

        main_layout = QVBoxLayout()
        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.previous_button)
        control_layout.addWidget(self.seek_backward_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.seek_forward_button)
        control_layout.addWidget(self.next_button)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.clear_button)

        position_duration = QHBoxLayout()
        position_duration.addWidget(self.duration_label)
        position_duration.addWidget(self.position_slider) # Можете использовать addWidget(self.progress_bar)
        position_duration.addWidget(self.duration_label_two)

        main_layout.addWidget(self.open_button)
        main_layout.addWidget(self.volume_slider)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.playlist_widget)
        main_layout.addWidget(self.song_label)
        main_layout.addLayout(position_duration)
        main_layout.addLayout(control_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

         # Добавьте следующий код для создания скругленных краев
        self.setStyleSheet("border-radius: 10px;")

        # Установка главного макета
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar.setStyleSheet(open("styles.qss").read())
        self.song_label.setObjectName("song_label")
        self.song_label.setStyleSheet(open("styles.qss").read())
        self.duration_label.setObjectName("duration_label")
        self.duration_label_two.setObjectName("duration_label")
        self.duration_label.setStyleSheet(open("styles.qss").read())
        self.open_button.setObjectName("open_button")
        self.open_button.setStyleSheet(open("styles.qss").read())
        # Стиль для элементов списка плейлиста
        self.playlist_widget.setObjectName("playlist_widget")
        self.playlist_widget.setStyleSheet(open("styles.qss").read())
        # Стиль для полосы прокрутки
        self.playlist_widget.verticalScrollBar().setObjectName("playlist_widget")
        self.playlist_widget.verticalScrollBar().setStyleSheet(open("styles.qss").read())
        self.playlist_widget.horizontalScrollBar().setObjectName("playlist_widget")
        self.playlist_widget.horizontalScrollBar().setStyleSheet(open("styles.qss").read())

        # Стиль для полосы изменения громкости
        self.volume_slider.setObjectName("volume_slider")
        self.volume_slider.setStyleSheet(open("styles.qss").read())

        # Стиль для полосы изменения воспроизведения
        self.position_slider.setObjectName("position_slider")
        self.position_slider.setStyleSheet(open("styles.qss").read())
        # Стиль для поля ввода поиска
        self.search_input.setObjectName("search_input")
        self.search_input.setStyleSheet(open("styles.qss").read())
         # Уменьшение высоты поля ввода поиска
        self.search_input.setFixedHeight(20)

        # Уменьшение высоты кнопки поиска
        self.clear_button.setFixedHeight(20)
        self.song_label.setFixedHeight(15)

        self.progress_bar.setFixedHeight(3)

        self.seek_forward_button.clicked.connect(self.seek_forward)
        self.seek_backward_button.clicked.connect(self.seek_backward)

    def set_position(self, position):
        self.media_player.setPosition(position * 1000)  # Установка новой позиции в миллисекундах

    def setup_menu(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setObjectName("menu_bar")
        self.menu_bar.setStyleSheet(open("styles.qss").read())

        # Создание меню
        menu = self.menuBar().addMenu(TRANSLATIONS[self.current_language]["menu_tr"])
        file_menu = self.menu_bar.addMenu((TRANSLATIONS[self.current_language]["file_tr"]))
        edit_menu = self.menu_bar.addMenu((TRANSLATIONS[self.current_language]["edit_tr"]))
        view_menu = self.menu_bar.addMenu((TRANSLATIONS[self.current_language]["view_tr"]))
        help_menu = self.menu_bar.addMenu((TRANSLATIONS[self.current_language]["help_tr"]))

        shuffle_action = menu.addAction((TRANSLATIONS[self.current_language]["shuffle_tracks_tr"]))
        shuffle_action.triggered.connect(self.shuffle_tracks)

        open_folder_action = file_menu.addAction((TRANSLATIONS[self.current_language]["open_folder_folders_button"]))
        open_folder_action.triggered.connect(self.open_folder)

        switch_language_action = view_menu.addAction((TRANSLATIONS[self.current_language]["switch_language"]))
        switch_language_action.triggered.connect(self.switch_language)

        # Добавьте другие действия меню и подключите их к соответствующим функциям

    def update_translations(self):
        self.setWindowTitle(TRANSLATIONS[self.current_language]["window_title"])
        self.open_button.setText(TRANSLATIONS[self.current_language]["open_folder_button"])
        self.menu_bar.actions()[0].setText(TRANSLATIONS[self.current_language]["menu_tr"])
        self.menu_bar.actions()[1].setText(TRANSLATIONS[self.current_language]["file_tr"])
        self.menu_bar.actions()[2].setText(TRANSLATIONS[self.current_language]["edit_tr"])
        self.menu_bar.actions()[3].setText(TRANSLATIONS[self.current_language]["view_tr"])
        self.menu_bar.actions()[4].setText(TRANSLATIONS[self.current_language]["help_tr"])
        self.menu_bar.actions()[3].menu().actions()[0].setText(TRANSLATIONS[self.current_language]["switch_language"])
        self.menu_bar.actions()[0].menu().actions()[0].setText(TRANSLATIONS[self.current_language]["shuffle_tracks_tr"])
        self.menu_bar.actions()[1].menu().actions()[0].setText(TRANSLATIONS[self.current_language]["open_folder_folders_button"])

    def shuffle_tracks(self):
        import random
        if self.filtered_playlist and self.current_index >= 0 and self.current_index < len(self.filtered_playlist):
            random.shuffle(self.filtered_playlist)
            self.playlist_widget.clear()
            self.playlist_widget.addItems([item.text() for item in self.filtered_playlist])
            self.current_index = 0
            self.play_track()
            self.update_playlist_selection()
            self.song_label.setText(self.filtered_playlist[self.current_index].text())
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowIcon(QIcon("ico.ico"))
            self.msg.setText(TRANSLATIONS[self.current_language]["msg_information"])
            self.msg.setInformativeText(TRANSLATIONS[self.current_language]["msg_no_tracks_message"])
            self.msg.setWindowTitle(TRANSLATIONS[self.current_language]["window_title"])
            self.msg.setStandardButtons(QMessageBox.Ok)  # Изменить кнопку на "OK"
            self.update_translations()
            self.msg.exec_()

    def switch_language(self):
        if self.current_language == "RUSSIAN":
            self.current_language = "ENGLISH"
        else:
            self.current_language = "RUSSIAN"

        self.update_translations()

    def clear_search_input(self):
        self.search_input.clear()

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
        self.search_input.textChanged.connect(self.filter_playlist)
        self.clear_button.clicked.connect(self.clear_search_input)
        self.position_slider.sliderMoved.connect(self.set_position)

    def seek_forward(self):
        position = self.media_player.position()
        self.media_player.setPosition(position + 15000)  # Перемотка на 15 секунд вперед

    def seek_backward(self):
        position = self.media_player.position()
        self.media_player.setPosition(position - 15000)  # Перемотка на 15 секунд назад
        
    def play(self):
        if self.playing:
            self.media_player.pause()
            self.song_label.setText(self.filtered_playlist[self.current_index].text())  
        else:
            self.media_player.play()
            self.song_label.setText(self.filtered_playlist[self.current_index].text())  

    def stop(self):
        self.media_player.stop()
        self.song_label.setText(self.filtered_playlist[self.current_index].text())  # Обновление названия трека

    def previous(self):
        if self.filtered_playlist:
            self.current_index -= 1
            if self.current_index < 0:
                self.current_index = len(self.filtered_playlist) - 1
            self.play_track()
            self.update_playlist_selection()
            self.song_label.setText(self.filtered_playlist[self.current_index].text())  

    def next(self):
        if self.filtered_playlist:
            self.current_index += 1
            if self.current_index >= len(self.filtered_playlist):
                self.current_index = 0
            self.play_track()
            self.update_playlist_selection()
            self.song_label.setText(self.filtered_playlist[self.current_index].text()) 

    def update_playlist_selection(self):
        # Снять выделение с предыдущего трека
        previous_item = self.playlist_widget.item(self.current_index - 1)
        if previous_item:
            previous_item.setSelected(False)

        # Выделить текущий трек
        current_item = self.playlist_widget.item(self.current_index)
        if current_item:
            current_item.setSelected(True)

    def load_playlist(self, folder_path):
        self.media_playlist = []
        self.filtered_playlist = []
        self.playlist_widget.clear()
        self.update_playlist_selection()

        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith(".mp3"):
                    full_path = os.path.join(root, file_name)
                    item = QListWidgetItem(file_name)
                    item.setData(Qt.UserRole, full_path)
                    self.media_playlist.append(item)
                    self.filtered_playlist.append(item.clone())
                    
        playlist_names = [item.text() for item in self.media_playlist]
        self.playlist_widget.addItems(playlist_names)

        self.current_index = 0
        if self.playing:
            self.play_track()

    def change_track(self, current_item, previous_item):
        if current_item:
            self.current_index = self.playlist_widget.currentRow()
            self.song_label.setText(current_item.text())
            self.play_track()

    def play_track(self):
        if self.filtered_playlist and self.current_index >= 0 and self.current_index < len(self.filtered_playlist):
            track_path = self.filtered_playlist[self.current_index].data(Qt.UserRole)
            media_content = QMediaContent(QUrl.fromLocalFile(track_path))
            self.media_player.setMedia(media_content)
            self.playing = True
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.song_label.setText(self.filtered_playlist[self.current_index].text())  # Обновление названия трека
            self.media_player.play()
            self.duration_timer.start()
            self.update_playlist_selection()

    def update_buttons(self, state):
        if state == QMediaPlayer.PlayingState:
            self.playing = True
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.duration_timer.start()
        else:
            self.playing = False
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.duration_timer.stop()
        current_item = self.playlist_widget.currentItem()
        if current_item:
            self.song_label.setText(current_item.text())
        else:
            self.song_label.setText("")

    def update_duration(self):
        if self.media_player.duration() > 0:
            duration = self.media_player.duration() / 1000
            position = self.media_player.position() / 1000
            self.duration_label.setText(
                f"{self.format_time(position)}"
            )
            self.duration_label_two.setText(
                f"{self.format_time(duration)}"
            )
            progress = int((position / duration) * 100)
            self.progress_bar.setValue(progress)
            self.position_slider.setRange(0, int(duration))
            self.position_slider.setValue(int(position))
            QTimer.singleShot(10, self.update_duration)

    def format_time(self, time_seconds):
        minutes = int(time_seconds / 60)
        seconds = int(time_seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def filter_playlist(self, keyword):
        keyword = keyword.lower()
        if keyword:
            self.filtered_playlist = [
                item for item in self.media_playlist if keyword.lower() in item.text().lower()
            ]
        else:
            self.filtered_playlist = self.media_playlist[:]

        current_item = self.playlist_widget.currentItem()
        current_track = current_item.data(Qt.UserRole) if current_item else None
        self.playlist_widget.clear()
        self.playlist_widget.addItems([item.text() for item in self.filtered_playlist])
        if current_track:
            for index, item in enumerate(self.filtered_playlist):
                if item.data(Qt.UserRole) == current_track:
                    self.current_index = index
                    break
        else:
            self.current_index = 0

        self.update_playlist_selection()

    def load_settings(self):
        with open("settings.pickle", "rb") as f:
            settings = pickle.load(f)
            self.current_language = settings["current_language"]
            self.current_folder = settings["current_folder"]
            self.current_index = settings["current_index"]
            
    def save_settings(self):
        settings = {
            "current_language": self.current_language,
            "current_folder": self.current_folder,
            "current_index": self.current_index,
        }
        with open("settings.pickle", "wb") as f:
            pickle.dump(settings, f)

    def open_folder(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly)

        if folder_dialog.exec_():
            folder_paths = folder_dialog.selectedFiles()
            for folder_path in folder_paths:
                self.current_folder = folder_path
                self.save_settings()

            if self.current_folder:
                self.load_playlist(folder_path)
                self.current_index = 0
                self.playlist_widget.setCurrentRow(self.current_index)

                self.media_player.setMedia(QMediaContent()) 
                self.playing = False  # Сброс флага состояния воспроизведения
                self.update_buttons(self.media_player.state()) 
            else:
                self.playlist_widget.clear()

    def closeEvent(self, event):
        self.save_settings()
        event.accept()

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
    app.setStyleSheet(open("styles.qss").read())

    window = AudioPlayer()
    window.show()

    sys.exit(app.exec_())
