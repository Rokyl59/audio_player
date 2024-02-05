# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(769, 556)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setToolTipDuration(1)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"            background-color: #353535;\n"
"            color: #ffffff;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #353535;\n"
"    color: white;\n"
"    margin: 2px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 30px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    border: 1px solid black;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: black;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"    border-radius: 8px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy1)
        self.side_menu.setMaximumSize(QSize(16777215, 16777215))
        self.side_menu.setStyleSheet(u"background: rgb(42, 42, 42)")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.side_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.side_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.open_folder_button = QPushButton(self.frame)
        self.open_folder_button.setObjectName(u"open_folder_button")
        self.open_folder_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"			color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_folder_button.setIcon(icon)

        self.verticalLayout_7.addWidget(self.open_folder_button)

        self.open_file_button = QPushButton(self.frame)
        self.open_file_button.setObjectName(u"open_file_button")
        self.open_file_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_file_button.setIcon(icon1)
        self.open_file_button.setIconSize(QSize(16, 16))

        self.verticalLayout_7.addWidget(self.open_file_button)

        self.save_playlist_button = QPushButton(self.frame)
        self.save_playlist_button.setObjectName(u"save_playlist_button")
        self.save_playlist_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_playlist_button.setIcon(icon2)

        self.verticalLayout_7.addWidget(self.save_playlist_button)

        self.open_playlist_button = QPushButton(self.frame)
        self.open_playlist_button.setObjectName(u"open_playlist_button")
        self.open_playlist_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_playlist_button.setIcon(icon3)

        self.verticalLayout_7.addWidget(self.open_playlist_button)

        self.delete_playlist = QPushButton(self.frame)
        self.delete_playlist.setObjectName(u"delete_playlist")
        self.delete_playlist.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/folder-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_playlist.setIcon(icon4)

        self.verticalLayout_7.addWidget(self.delete_playlist)


        self.verticalLayout_6.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.side_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.change_theme_button = QPushButton(self.frame_2)
        self.change_theme_button.setObjectName(u"change_theme_button")
        self.change_theme_button.setLayoutDirection(Qt.LeftToRight)
        self.change_theme_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/feather.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.change_theme_button.setIcon(icon5)

        self.verticalLayout_8.addWidget(self.change_theme_button)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.side_menu)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"QFrame {\n"
"	background: #353535; \n"
"}")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.main_body)
        self.header.setObjectName(u"header")
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setStyleSheet(u"background: #353535;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.header)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.header)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.header)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.search_line_edit = QLineEdit(self.frame_12)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(74, 74, 74);\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"	color: white;\n"
"	border-bottom:1px solid rgb(85, 255, 127);\n"
"}")
        self.search_line_edit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.search_line_edit.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.search_line_edit)


        self.verticalLayout_3.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.body_content = QFrame(self.main_body)
        self.body_content.setObjectName(u"body_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.body_content.sizePolicy().hasHeightForWidth())
        self.body_content.setSizePolicy(sizePolicy2)
        self.body_content.setStyleSheet(u"")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.body_content)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 2, 2)
        self.scrollArea = QScrollArea(self.body_content)
        self.scrollArea.setObjectName(u"scrollArea")
        font1 = QFont()
        font1.setFamilies([u"MS Outlook"])
        font1.setPointSize(8)
        self.scrollArea.setFont(font1)
        self.scrollArea.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:#393939;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(74, 74, 74);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(74, 74, 74);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLL"
                        "BAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(74, 74, 74);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #393939;\n"
"    height: 14px; /* Set the width instead of the height */\n"
"    margin: 0 15px 0 15px; /* Adjust the margins accordingly */\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* HANDLE BAR HORIZONTAL */\n"
""
                        "QScrollBar::handle:horizontal {\n"
"    background-color: rgb(74, 74, 74);\n"
"    min-width: 30px; /* Set the height instead of the width */\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(74, 74, 74);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"/* BTN LEFT - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"   	background-color: rgb(74, 74, 74);\n"
"    width: 15px; /* Set the height instead of the width */\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left; /* Change subcontrol position to left */\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: rgb(74, 74, 74);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"/* BTN RIGHT - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
""
                        "    border: none;\n"
"    background-color: rgb(74, 74, 74);\n"
"    width: 15px; /* Set the height instead of the width */\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right; /* Change subcontrol position to right */\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color: rgb(74, 74, 74);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::left-arrow:horizontal,\n"
"QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.playlist_widget = QListWidget()
        self.playlist_widget.setObjectName(u"playlist_widget")
        self.playlist_widget.setGeometry(QRect(0, 0, 712, 414))
        font2 = QFont()
        font2.setFamilies([u"Victoria"])
        font2.setPointSize(10)
        self.playlist_widget.setFont(font2)
        self.playlist_widget.setFocusPolicy(Qt.NoFocus)
        self.playlist_widget.setAutoFillBackground(True)
        self.playlist_widget.setStyleSheet(u"QListWidget {\n"
"    background-color: #353535;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #353535;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"	color: white;\n"
"	letter-spacing: 3px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    color: rgb(85, 255, 127);\n"
"}")
        self.playlist_widget.setDragEnabled(False)
        self.playlist_widget.setDragDropOverwriteMode(False)
        self.playlist_widget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.playlist_widget.setDefaultDropAction(Qt.MoveAction)
        self.playlist_widget.setAlternatingRowColors(False)
        self.playlist_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.playlist_widget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.playlist_widget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.playlist_widget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.playlist_widget.setSpacing(3)
        self.scrollArea.setWidget(self.playlist_widget)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.body_content)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background: #353535;\n"
"")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.footer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background: rgb(53,53,53)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 2, 5, 2)
        self.song_label = QLabel(self.frame_7)
        self.song_label.setObjectName(u"song_label")
        self.song_label.setStyleSheet(u"color: white;\n"
"font-weight:bold;")

        self.horizontalLayout_6.addWidget(self.song_label)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignVCenter)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background: #353535;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.duration_label = QLabel(self.frame_5)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setStyleSheet(u"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_5.addWidget(self.duration_label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.duration_slider = QSlider(self.frame_5)
        self.duration_slider.setObjectName(u"duration_slider")
        self.duration_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	background-color: grey;\n"
"	height: 4px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background-color:rgb(85, 255, 127);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(85, 255, 0);\n"
"	border: none;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	margin: -3px 0;\n"
"	border-radius: 5px;\n"
"}")
        self.duration_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.duration_slider, 0, Qt.AlignVCenter)

        self.duration_label_2 = QLabel(self.frame_5)
        self.duration_label_2.setObjectName(u"duration_label_2")
        self.duration_label_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_5.addWidget(self.duration_label_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignVCenter)

        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background: #353535;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.language_button = QPushButton(self.frame_10)
        self.language_button.setObjectName(u"language_button")
        self.language_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.language_button.setIcon(icon6)
        self.language_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.language_button)

        self.sound_button = QPushButton(self.frame_10)
        self.sound_button.setObjectName(u"sound_button")
        self.sound_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/volume-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sound_button.setIcon(icon7)
        self.sound_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.sound_button)

        self.volume_slider = QSlider(self.frame_10)
        self.volume_slider.setObjectName(u"volume_slider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy3)
        self.volume_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: grey;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color:rgb(85, 255, 127);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 255, 0);\n"
"    border: none;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin: -3px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider {\n"
"	border-radius: 2px;\n"
"}")
        self.volume_slider.setValue(99)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.volume_slider)


        self.horizontalLayout_2.addWidget(self.frame_10, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.frame_9)
        self.previous_button.setObjectName(u"previous_button")
        sizePolicy3.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy3)
        self.previous_button.setMinimumSize(QSize(0, 0))
        self.previous_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/skip-back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_button.setIcon(icon8)
        self.previous_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.previous_button)

        self.pre_button = QPushButton(self.frame_9)
        self.pre_button.setObjectName(u"pre_button")
        sizePolicy3.setHeightForWidth(self.pre_button.sizePolicy().hasHeightForWidth())
        self.pre_button.setSizePolicy(sizePolicy3)
        self.pre_button.setMinimumSize(QSize(0, 0))
        self.pre_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/rewind.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pre_button.setIcon(icon9)
        self.pre_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pre_button)

        self.play_button = QPushButton(self.frame_9)
        self.play_button.setObjectName(u"play_button")
        sizePolicy3.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy3)
        self.play_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon10)
        self.play_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.play_button)

        self.forw_button = QPushButton(self.frame_9)
        self.forw_button.setObjectName(u"forw_button")
        sizePolicy3.setHeightForWidth(self.forw_button.sizePolicy().hasHeightForWidth())
        self.forw_button.setSizePolicy(sizePolicy3)
        self.forw_button.setMinimumSize(QSize(0, 0))
        self.forw_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/fast-forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.forw_button.setIcon(icon11)
        self.forw_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.forw_button)

        self.following_button = QPushButton(self.frame_9)
        self.following_button.setObjectName(u"following_button")
        sizePolicy3.setHeightForWidth(self.following_button.sizePolicy().hasHeightForWidth())
        self.following_button.setSizePolicy(sizePolicy3)
        self.following_button.setMinimumSize(QSize(0, 0))
        self.following_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/skip-forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.following_button.setIcon(icon12)
        self.following_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.following_button)


        self.horizontalLayout_2.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.shuffle_button = QPushButton(self.frame_8)
        self.shuffle_button.setObjectName(u"shuffle_button")
        self.shuffle_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.shuffle_button.setIcon(icon13)

        self.gridLayout.addWidget(self.shuffle_button, 0, 4, 1, 1)

        self.sound_menu_button = QPushButton(self.frame_8)
        self.sound_menu_button.setObjectName(u"sound_menu_button")
        self.sound_menu_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 53, 53);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sound_menu_button.setIcon(icon14)

        self.gridLayout.addWidget(self.sound_menu_button, 0, 5, 1, 1)

        self.replay_button = QPushButton(self.frame_8)
        self.replay_button.setObjectName(u"replay_button")
        self.replay_button.setStyleSheet(u"QToolTip {\n"
"	padding: 3px; \n"
" 	background-color: #353535;\n"
"	color: white;\n"
"    font-weight:bold;\n"
"	border:1px solid black;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            color: #ffffff;\n"
"            border: none;\n"
"            padding: 2px 6px;\n"
"            border-radius: 5px;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(74, 74, 74);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.replay_button.setIcon(icon15)
        self.replay_button.setCheckable(True)

        self.gridLayout.addWidget(self.replay_button, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_8, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.open_folder_button.setToolTip(QCoreApplication.translate("MainWindow", u"Open folder", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.open_folder_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.open_folder_button.setText("")
#if QT_CONFIG(tooltip)
        self.open_file_button.setToolTip(QCoreApplication.translate("MainWindow", u"Open file", None))
#endif // QT_CONFIG(tooltip)
        self.open_file_button.setText("")
#if QT_CONFIG(tooltip)
        self.save_playlist_button.setToolTip(QCoreApplication.translate("MainWindow", u"Save playlist", None))
#endif // QT_CONFIG(tooltip)
        self.save_playlist_button.setText("")
#if QT_CONFIG(tooltip)
        self.open_playlist_button.setToolTip(QCoreApplication.translate("MainWindow", u"Open playlist", None))
#endif // QT_CONFIG(tooltip)
        self.open_playlist_button.setText("")
#if QT_CONFIG(tooltip)
        self.delete_playlist.setToolTip(QCoreApplication.translate("MainWindow", u"Delete playlist", None))
#endif // QT_CONFIG(tooltip)
        self.delete_playlist.setText("")
#if QT_CONFIG(tooltip)
        self.change_theme_button.setToolTip(QCoreApplication.translate("MainWindow", u"Change Theme", None))
#endif // QT_CONFIG(tooltip)
        self.change_theme_button.setText("")
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.song_label.setText("")
        self.duration_label.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.duration_label_2.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
#if QT_CONFIG(tooltip)
        self.language_button.setToolTip(QCoreApplication.translate("MainWindow", u"Switch language", None))
#endif // QT_CONFIG(tooltip)
        self.language_button.setText("")
#if QT_CONFIG(tooltip)
        self.sound_button.setToolTip(QCoreApplication.translate("MainWindow", u"Mute", None))
#endif // QT_CONFIG(tooltip)
        self.sound_button.setText("")
#if QT_CONFIG(tooltip)
        self.previous_button.setToolTip(QCoreApplication.translate("MainWindow", u"Previous", None))
#endif // QT_CONFIG(tooltip)
        self.previous_button.setText("")
#if QT_CONFIG(tooltip)
        self.pre_button.setToolTip(QCoreApplication.translate("MainWindow", u"- 15", None))
#endif // QT_CONFIG(tooltip)
        self.pre_button.setText("")
#if QT_CONFIG(tooltip)
        self.play_button.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.play_button.setText("")
#if QT_CONFIG(tooltip)
        self.forw_button.setToolTip(QCoreApplication.translate("MainWindow", u"+ 15 ", None))
#endif // QT_CONFIG(tooltip)
        self.forw_button.setText("")
#if QT_CONFIG(tooltip)
        self.following_button.setToolTip(QCoreApplication.translate("MainWindow", u"Following", None))
#endif // QT_CONFIG(tooltip)
        self.following_button.setText("")
#if QT_CONFIG(tooltip)
        self.shuffle_button.setToolTip(QCoreApplication.translate("MainWindow", u"Shuffle", None))
#endif // QT_CONFIG(tooltip)
        self.shuffle_button.setText("")
#if QT_CONFIG(tooltip)
        self.sound_menu_button.setToolTip(QCoreApplication.translate("MainWindow", u"Additional parameters", None))
#endif // QT_CONFIG(tooltip)
        self.sound_menu_button.setText("")
#if QT_CONFIG(tooltip)
        self.replay_button.setToolTip(QCoreApplication.translate("MainWindow", u"Replay", None))
#endif // QT_CONFIG(tooltip)
        self.replay_button.setText("")
    # retranslateUi

