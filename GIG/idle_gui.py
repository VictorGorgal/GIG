# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idle_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(901, 525)
        MainWindow.setMinimumSize(QtCore.QSize(901, 525))
        MainWindow.setMaximumSize(QtCore.QSize(901, 525))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(10, 50, 61, 41))
        self.home_button.setObjectName("home_button")
        self.options_button = QtWidgets.QPushButton(self.centralwidget)
        self.options_button.setGeometry(QtCore.QRect(10, 250, 61, 41))
        self.options_button.setObjectName("options_button")
        self.diamonds_button = QtWidgets.QPushButton(self.centralwidget)
        self.diamonds_button.setGeometry(QtCore.QRect(10, 150, 61, 41))
        self.diamonds_button.setObjectName("diamonds_button")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(90, 0, 801, 521))
        self.pages.setObjectName("pages")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.yuri_profit_label = QtWidgets.QLabel(self.home)
        self.yuri_profit_label.setGeometry(QtCore.QRect(490, 210, 311, 31))
        self.yuri_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.yuri_profit_label.setObjectName("yuri_profit_label")
        self.mine_button = QtWidgets.QPushButton(self.home)
        self.mine_button.setGeometry(QtCore.QRect(300, 460, 201, 51))
        self.mine_button.setObjectName("mine_button")
        self.slaves_profit_label = QtWidgets.QLabel(self.home)
        self.slaves_profit_label.setGeometry(QtCore.QRect(80, 140, 311, 31))
        self.slaves_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slaves_profit_label.setObjectName("slaves_profit_label")
        self.rats_button = QtWidgets.QPushButton(self.home)
        self.rats_button.setGeometry(QtCore.QRect(0, 70, 75, 31))
        self.rats_button.setObjectName("rats_button")
        self.rats_progress = QtWidgets.QProgressBar(self.home)
        self.rats_progress.setGeometry(QtCore.QRect(80, 70, 311, 31))
        self.rats_progress.setMaximum(60)
        self.rats_progress.setProperty("value", 0)
        self.rats_progress.setTextVisible(False)
        self.rats_progress.setInvertedAppearance(False)
        self.rats_progress.setObjectName("rats_progress")
        self.machines_progress = QtWidgets.QProgressBar(self.home)
        self.machines_progress.setGeometry(QtCore.QRect(490, 140, 311, 31))
        self.machines_progress.setMaximum(60)
        self.machines_progress.setProperty("value", 0)
        self.machines_progress.setTextVisible(False)
        self.machines_progress.setObjectName("machines_progress")
        self.machines_label = QtWidgets.QLabel(self.home)
        self.machines_label.setGeometry(QtCore.QRect(410, 120, 151, 16))
        self.machines_label.setObjectName("machines_label")
        self.gold_label = QtWidgets.QLabel(self.home)
        self.gold_label.setGeometry(QtCore.QRect(540, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gold_label.setFont(font)
        self.gold_label.setScaledContents(False)
        self.gold_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gold_label.setWordWrap(False)
        self.gold_label.setObjectName("gold_label")
        self.chemical_profit_label = QtWidgets.QLabel(self.home)
        self.chemical_profit_label.setGeometry(QtCore.QRect(80, 210, 311, 31))
        self.chemical_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chemical_profit_label.setObjectName("chemical_profit_label")
        self.yuri_label = QtWidgets.QLabel(self.home)
        self.yuri_label.setGeometry(QtCore.QRect(410, 190, 151, 16))
        self.yuri_label.setObjectName("yuri_label")
        self.rats_profit_label = QtWidgets.QLabel(self.home)
        self.rats_profit_label.setGeometry(QtCore.QRect(80, 70, 311, 31))
        self.rats_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rats_profit_label.setObjectName("rats_profit_label")
        self.chemical_progress = QtWidgets.QProgressBar(self.home)
        self.chemical_progress.setGeometry(QtCore.QRect(80, 210, 311, 31))
        self.chemical_progress.setMaximum(60)
        self.chemical_progress.setProperty("value", 0)
        self.chemical_progress.setTextVisible(False)
        self.chemical_progress.setObjectName("chemical_progress")
        self.yuri_button = QtWidgets.QPushButton(self.home)
        self.yuri_button.setGeometry(QtCore.QRect(410, 210, 75, 31))
        self.yuri_button.setObjectName("yuri_button")
        self.flame_profit_label = QtWidgets.QLabel(self.home)
        self.flame_profit_label.setGeometry(QtCore.QRect(490, 70, 311, 31))
        self.flame_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flame_profit_label.setObjectName("flame_profit_label")
        self.slaves_progress = QtWidgets.QProgressBar(self.home)
        self.slaves_progress.setGeometry(QtCore.QRect(80, 140, 311, 31))
        self.slaves_progress.setMaximum(60)
        self.slaves_progress.setProperty("value", 0)
        self.slaves_progress.setTextVisible(False)
        self.slaves_progress.setObjectName("slaves_progress")
        self.slaves_button = QtWidgets.QPushButton(self.home)
        self.slaves_button.setGeometry(QtCore.QRect(0, 140, 75, 31))
        self.slaves_button.setObjectName("slaves_button")
        self.chemical_button = QtWidgets.QPushButton(self.home)
        self.chemical_button.setGeometry(QtCore.QRect(0, 210, 75, 31))
        self.chemical_button.setObjectName("chemical_button")
        self.flame_button = QtWidgets.QPushButton(self.home)
        self.flame_button.setGeometry(QtCore.QRect(410, 70, 75, 31))
        self.flame_button.setObjectName("flame_button")
        self.flame_progress = QtWidgets.QProgressBar(self.home)
        self.flame_progress.setGeometry(QtCore.QRect(490, 70, 311, 31))
        self.flame_progress.setMaximum(60)
        self.flame_progress.setProperty("value", 0)
        self.flame_progress.setTextVisible(False)
        self.flame_progress.setObjectName("flame_progress")
        self.flame_label = QtWidgets.QLabel(self.home)
        self.flame_label.setGeometry(QtCore.QRect(410, 50, 181, 16))
        self.flame_label.setObjectName("flame_label")
        self.machines_profit_label = QtWidgets.QLabel(self.home)
        self.machines_profit_label.setGeometry(QtCore.QRect(490, 140, 311, 31))
        self.machines_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.machines_profit_label.setObjectName("machines_profit_label")
        self.slaves_label = QtWidgets.QLabel(self.home)
        self.slaves_label.setGeometry(QtCore.QRect(0, 120, 171, 16))
        self.slaves_label.setObjectName("slaves_label")
        self.machines_button = QtWidgets.QPushButton(self.home)
        self.machines_button.setGeometry(QtCore.QRect(410, 140, 75, 31))
        self.machines_button.setObjectName("machines_button")
        self.chemical_label = QtWidgets.QLabel(self.home)
        self.chemical_label.setGeometry(QtCore.QRect(0, 190, 171, 16))
        self.chemical_label.setObjectName("chemical_label")
        self.yuri_progress = QtWidgets.QProgressBar(self.home)
        self.yuri_progress.setGeometry(QtCore.QRect(490, 210, 311, 31))
        self.yuri_progress.setMaximum(60)
        self.yuri_progress.setProperty("value", 0)
        self.yuri_progress.setTextVisible(False)
        self.yuri_progress.setObjectName("yuri_progress")
        self.rats_label = QtWidgets.QLabel(self.home)
        self.rats_label.setGeometry(QtCore.QRect(0, 50, 181, 16))
        self.rats_label.setObjectName("rats_label")
        self.multiplier_label = QtWidgets.QLabel(self.home)
        self.multiplier_label.setGeometry(QtCore.QRect(0, 10, 31, 31))
        self.multiplier_label.setObjectName("multiplier_label")
        self.multiplier_button = QtWidgets.QPushButton(self.home)
        self.multiplier_button.setGeometry(QtCore.QRect(30, 10, 41, 31))
        self.multiplier_button.setAutoDefault(False)
        self.multiplier_button.setDefault(False)
        self.multiplier_button.setFlat(False)
        self.multiplier_button.setObjectName("multiplier_button")
        self.aliens_label = QtWidgets.QLabel(self.home)
        self.aliens_label.setGeometry(QtCore.QRect(410, 260, 171, 16))
        self.aliens_label.setObjectName("aliens_label")
        self.soraka_label = QtWidgets.QLabel(self.home)
        self.soraka_label.setGeometry(QtCore.QRect(410, 330, 151, 16))
        self.soraka_label.setObjectName("soraka_label")
        self.soraka_progress = QtWidgets.QProgressBar(self.home)
        self.soraka_progress.setGeometry(QtCore.QRect(490, 350, 311, 31))
        self.soraka_progress.setMaximum(60)
        self.soraka_progress.setProperty("value", 0)
        self.soraka_progress.setTextVisible(False)
        self.soraka_progress.setObjectName("soraka_progress")
        self.aliens_progress = QtWidgets.QProgressBar(self.home)
        self.aliens_progress.setGeometry(QtCore.QRect(490, 280, 311, 31))
        self.aliens_progress.setMaximum(60)
        self.aliens_progress.setProperty("value", 0)
        self.aliens_progress.setTextVisible(False)
        self.aliens_progress.setObjectName("aliens_progress")
        self.soraka_profit_label = QtWidgets.QLabel(self.home)
        self.soraka_profit_label.setGeometry(QtCore.QRect(490, 350, 311, 31))
        self.soraka_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.soraka_profit_label.setObjectName("soraka_profit_label")
        self.aliens_profit_label = QtWidgets.QLabel(self.home)
        self.aliens_profit_label.setGeometry(QtCore.QRect(490, 280, 311, 31))
        self.aliens_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.aliens_profit_label.setObjectName("aliens_profit_label")
        self.soraka_button = QtWidgets.QPushButton(self.home)
        self.soraka_button.setGeometry(QtCore.QRect(410, 350, 75, 31))
        self.soraka_button.setObjectName("soraka_button")
        self.aliens_button = QtWidgets.QPushButton(self.home)
        self.aliens_button.setGeometry(QtCore.QRect(410, 280, 75, 31))
        self.aliens_button.setObjectName("aliens_button")
        self.babushka_label = QtWidgets.QLabel(self.home)
        self.babushka_label.setGeometry(QtCore.QRect(0, 330, 171, 16))
        self.babushka_label.setObjectName("babushka_label")
        self.babushka_progress = QtWidgets.QProgressBar(self.home)
        self.babushka_progress.setGeometry(QtCore.QRect(80, 350, 311, 31))
        self.babushka_progress.setMaximum(60)
        self.babushka_progress.setProperty("value", 0)
        self.babushka_progress.setTextVisible(False)
        self.babushka_progress.setObjectName("babushka_progress")
        self.hole_progress = QtWidgets.QProgressBar(self.home)
        self.hole_progress.setGeometry(QtCore.QRect(80, 280, 311, 31))
        self.hole_progress.setMaximum(60)
        self.hole_progress.setProperty("value", 0)
        self.hole_progress.setTextVisible(False)
        self.hole_progress.setObjectName("hole_progress")
        self.babushka_button = QtWidgets.QPushButton(self.home)
        self.babushka_button.setGeometry(QtCore.QRect(0, 350, 75, 31))
        self.babushka_button.setObjectName("babushka_button")
        self.hole_button = QtWidgets.QPushButton(self.home)
        self.hole_button.setGeometry(QtCore.QRect(0, 280, 75, 31))
        self.hole_button.setObjectName("hole_button")
        self.babushka_profit_label = QtWidgets.QLabel(self.home)
        self.babushka_profit_label.setGeometry(QtCore.QRect(80, 350, 311, 31))
        self.babushka_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.babushka_profit_label.setObjectName("babushka_profit_label")
        self.hole_label = QtWidgets.QLabel(self.home)
        self.hole_label.setGeometry(QtCore.QRect(0, 260, 151, 16))
        self.hole_label.setObjectName("hole_label")
        self.hole_profit_label = QtWidgets.QLabel(self.home)
        self.hole_profit_label.setGeometry(QtCore.QRect(80, 280, 311, 31))
        self.hole_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hole_profit_label.setObjectName("hole_profit_label")
        self.rats_progress.raise_()
        self.slaves_progress.raise_()
        self.chemical_progress.raise_()
        self.yuri_progress.raise_()
        self.flame_progress.raise_()
        self.yuri_profit_label.raise_()
        self.mine_button.raise_()
        self.slaves_profit_label.raise_()
        self.rats_button.raise_()
        self.machines_progress.raise_()
        self.machines_label.raise_()
        self.gold_label.raise_()
        self.chemical_profit_label.raise_()
        self.yuri_label.raise_()
        self.rats_profit_label.raise_()
        self.yuri_button.raise_()
        self.flame_profit_label.raise_()
        self.slaves_button.raise_()
        self.chemical_button.raise_()
        self.flame_button.raise_()
        self.flame_label.raise_()
        self.machines_profit_label.raise_()
        self.slaves_label.raise_()
        self.machines_button.raise_()
        self.chemical_label.raise_()
        self.rats_label.raise_()
        self.multiplier_label.raise_()
        self.multiplier_button.raise_()
        self.aliens_label.raise_()
        self.soraka_label.raise_()
        self.soraka_progress.raise_()
        self.aliens_progress.raise_()
        self.soraka_profit_label.raise_()
        self.aliens_profit_label.raise_()
        self.soraka_button.raise_()
        self.aliens_button.raise_()
        self.babushka_label.raise_()
        self.babushka_progress.raise_()
        self.hole_progress.raise_()
        self.babushka_button.raise_()
        self.hole_button.raise_()
        self.babushka_profit_label.raise_()
        self.hole_label.raise_()
        self.hole_profit_label.raise_()
        self.pages.addWidget(self.home)
        self.upgrades = QtWidgets.QWidget()
        self.upgrades.setObjectName("upgrades")
        self.hole5x_button = QtWidgets.QPushButton(self.upgrades)
        self.hole5x_button.setGeometry(QtCore.QRect(0, 180, 241, 41))
        self.hole5x_button.setObjectName("hole5x_button")
        self.rats5x_button = QtWidgets.QPushButton(self.upgrades)
        self.rats5x_button.setEnabled(True)
        self.rats5x_button.setGeometry(QtCore.QRect(0, 60, 241, 41))
        self.rats5x_button.setObjectName("rats5x_button")
        self.everything10x_button = QtWidgets.QPushButton(self.upgrades)
        self.everything10x_button.setGeometry(QtCore.QRect(560, 300, 241, 41))
        self.everything10x_button.setObjectName("everything10x_button")
        self.soraka5x_button = QtWidgets.QPushButton(self.upgrades)
        self.soraka5x_button.setGeometry(QtCore.QRect(0, 240, 241, 41))
        self.soraka5x_button.setObjectName("soraka5x_button")
        self.yuri5x_button = QtWidgets.QPushButton(self.upgrades)
        self.yuri5x_button.setGeometry(QtCore.QRect(560, 120, 241, 41))
        self.yuri5x_button.setObjectName("yuri5x_button")
        self.everything5x1_button = QtWidgets.QPushButton(self.upgrades)
        self.everything5x1_button.setGeometry(QtCore.QRect(0, 300, 241, 41))
        self.everything5x1_button.setObjectName("everything5x1_button")
        self.aliens5x_button = QtWidgets.QPushButton(self.upgrades)
        self.aliens5x_button.setGeometry(QtCore.QRect(280, 180, 241, 41))
        self.aliens5x_button.setObjectName("aliens5x_button")
        self.flame5x_button = QtWidgets.QPushButton(self.upgrades)
        self.flame5x_button.setGeometry(QtCore.QRect(280, 60, 241, 41))
        self.flame5x_button.setObjectName("flame5x_button")
        self.chemical5x_button = QtWidgets.QPushButton(self.upgrades)
        self.chemical5x_button.setGeometry(QtCore.QRect(280, 120, 241, 41))
        self.chemical5x_button.setObjectName("chemical5x_button")
        self.slaves5x_button = QtWidgets.QPushButton(self.upgrades)
        self.slaves5x_button.setGeometry(QtCore.QRect(560, 60, 241, 41))
        self.slaves5x_button.setObjectName("slaves5x_button")
        self.babushka5x_button = QtWidgets.QPushButton(self.upgrades)
        self.babushka5x_button.setGeometry(QtCore.QRect(560, 180, 241, 41))
        self.babushka5x_button.setObjectName("babushka5x_button")
        self.machines5x_button = QtWidgets.QPushButton(self.upgrades)
        self.machines5x_button.setGeometry(QtCore.QRect(0, 120, 241, 41))
        self.machines5x_button.setObjectName("machines5x_button")
        self.everything5x2_button = QtWidgets.QPushButton(self.upgrades)
        self.everything5x2_button.setGeometry(QtCore.QRect(280, 300, 241, 41))
        self.everything5x2_button.setObjectName("everything5x2_button")
        self.diamond1p1_button = QtWidgets.QPushButton(self.upgrades)
        self.diamond1p1_button.setGeometry(QtCore.QRect(280, 240, 241, 41))
        self.diamond1p1_button.setObjectName("diamond1p1_button")
        self.diamond1p2_button = QtWidgets.QPushButton(self.upgrades)
        self.diamond1p2_button.setGeometry(QtCore.QRect(560, 240, 241, 41))
        self.diamond1p2_button.setObjectName("diamond1p2_button")
        self.label2 = QtWidgets.QLabel(self.upgrades)
        self.label2.setEnabled(True)
        self.label2.setGeometry(QtCore.QRect(580, 490, 221, 31))
        self.label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label2.setObjectName("label2")
        self.pages.addWidget(self.upgrades)
        self.diamonds = QtWidgets.QWidget()
        self.diamonds.setObjectName("diamonds")
        self.diamonds_label = QtWidgets.QLabel(self.diamonds)
        self.diamonds_label.setGeometry(QtCore.QRect(0, 10, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.diamonds_label.setFont(font)
        self.diamonds_label.setScaledContents(False)
        self.diamonds_label.setAlignment(QtCore.Qt.AlignCenter)
        self.diamonds_label.setWordWrap(False)
        self.diamonds_label.setObjectName("diamonds_label")
        self.everything2x1_button = QtWidgets.QPushButton(self.diamonds)
        self.everything2x1_button.setGeometry(QtCore.QRect(560, 240, 241, 41))
        self.everything2x1_button.setObjectName("everything2x1_button")
        self.everything2x2_button = QtWidgets.QPushButton(self.diamonds)
        self.everything2x2_button.setGeometry(QtCore.QRect(0, 300, 241, 41))
        self.everything2x2_button.setObjectName("everything2x2_button")
        self.everything5x_button = QtWidgets.QPushButton(self.diamonds)
        self.everything5x_button.setGeometry(QtCore.QRect(280, 300, 241, 41))
        self.everything5x_button.setObjectName("everything5x_button")
        self.label = QtWidgets.QLabel(self.diamonds)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(580, 490, 221, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.prestige_button = QtWidgets.QPushButton(self.diamonds)
        self.prestige_button.setGeometry(QtCore.QRect(250, 450, 301, 61))
        self.prestige_button.setObjectName("prestige_button")
        self.rats2x_button = QtWidgets.QPushButton(self.diamonds)
        self.rats2x_button.setEnabled(True)
        self.rats2x_button.setGeometry(QtCore.QRect(0, 60, 241, 41))
        self.rats2x_button.setObjectName("rats2x_button")
        self.slaves2x_button = QtWidgets.QPushButton(self.diamonds)
        self.slaves2x_button.setGeometry(QtCore.QRect(560, 60, 241, 41))
        self.slaves2x_button.setObjectName("slaves2x_button")
        self.flame2x_button = QtWidgets.QPushButton(self.diamonds)
        self.flame2x_button.setGeometry(QtCore.QRect(280, 60, 241, 41))
        self.flame2x_button.setObjectName("flame2x_button")
        self.machines2x_button = QtWidgets.QPushButton(self.diamonds)
        self.machines2x_button.setGeometry(QtCore.QRect(0, 120, 241, 41))
        self.machines2x_button.setObjectName("machines2x_button")
        self.chemical2x_button = QtWidgets.QPushButton(self.diamonds)
        self.chemical2x_button.setGeometry(QtCore.QRect(280, 120, 241, 41))
        self.chemical2x_button.setObjectName("chemical2x_button")
        self.yuri2x_button = QtWidgets.QPushButton(self.diamonds)
        self.yuri2x_button.setGeometry(QtCore.QRect(560, 120, 241, 41))
        self.yuri2x_button.setObjectName("yuri2x_button")
        self.aliens2x_button = QtWidgets.QPushButton(self.diamonds)
        self.aliens2x_button.setGeometry(QtCore.QRect(280, 180, 241, 41))
        self.aliens2x_button.setObjectName("aliens2x_button")
        self.babushka2x_button = QtWidgets.QPushButton(self.diamonds)
        self.babushka2x_button.setGeometry(QtCore.QRect(560, 180, 241, 41))
        self.babushka2x_button.setObjectName("babushka2x_button")
        self.hole2x_button = QtWidgets.QPushButton(self.diamonds)
        self.hole2x_button.setGeometry(QtCore.QRect(0, 180, 241, 41))
        self.hole2x_button.setObjectName("hole2x_button")
        self.soraka2x_button = QtWidgets.QPushButton(self.diamonds)
        self.soraka2x_button.setGeometry(QtCore.QRect(0, 240, 241, 41))
        self.soraka2x_button.setObjectName("soraka2x_button")
        self.starting_gold_100_button = QtWidgets.QPushButton(self.diamonds)
        self.starting_gold_100_button.setGeometry(QtCore.QRect(280, 240, 241, 41))
        self.starting_gold_100_button.setObjectName("starting_gold_100_button")
        self.pages.addWidget(self.diamonds)
        self.stats = QtWidgets.QWidget()
        self.stats.setObjectName("stats")
        self.stats_label1 = QtWidgets.QLabel(self.stats)
        self.stats_label1.setGeometry(QtCore.QRect(0, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stats_label1.setFont(font)
        self.stats_label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stats_label1.setObjectName("stats_label1")
        self.total_session_gold_label = QtWidgets.QLabel(self.stats)
        self.total_session_gold_label.setGeometry(QtCore.QRect(400, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_session_gold_label.setFont(font)
        self.total_session_gold_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_session_gold_label.setObjectName("total_session_gold_label")
        self.stats_label3 = QtWidgets.QLabel(self.stats)
        self.stats_label3.setGeometry(QtCore.QRect(0, 110, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stats_label3.setFont(font)
        self.stats_label3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stats_label3.setObjectName("stats_label3")
        self.total_diamonds_label = QtWidgets.QLabel(self.stats)
        self.total_diamonds_label.setGeometry(QtCore.QRect(400, 110, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_diamonds_label.setFont(font)
        self.total_diamonds_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_diamonds_label.setObjectName("total_diamonds_label")
        self.stats_label5 = QtWidgets.QLabel(self.stats)
        self.stats_label5.setGeometry(QtCore.QRect(0, 210, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stats_label5.setFont(font)
        self.stats_label5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stats_label5.setObjectName("stats_label5")
        self.total_prestiges_label = QtWidgets.QLabel(self.stats)
        self.total_prestiges_label.setGeometry(QtCore.QRect(400, 210, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_prestiges_label.setFont(font)
        self.total_prestiges_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_prestiges_label.setObjectName("total_prestiges_label")
        self.stats_label2 = QtWidgets.QLabel(self.stats)
        self.stats_label2.setGeometry(QtCore.QRect(0, 60, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stats_label2.setFont(font)
        self.stats_label2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stats_label2.setObjectName("stats_label2")
        self.total_life_gold_label = QtWidgets.QLabel(self.stats)
        self.total_life_gold_label.setGeometry(QtCore.QRect(400, 60, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_life_gold_label.setFont(font)
        self.total_life_gold_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_life_gold_label.setObjectName("total_life_gold_label")
        self.stats_label4 = QtWidgets.QLabel(self.stats)
        self.stats_label4.setGeometry(QtCore.QRect(0, 160, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stats_label4.setFont(font)
        self.stats_label4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stats_label4.setObjectName("stats_label4")
        self.diamond_boost_label = QtWidgets.QLabel(self.stats)
        self.diamond_boost_label.setGeometry(QtCore.QRect(400, 160, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.diamond_boost_label.setFont(font)
        self.diamond_boost_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diamond_boost_label.setObjectName("diamond_boost_label")
        self.pages.addWidget(self.stats)
        self.options = QtWidgets.QWidget()
        self.options.setObjectName("options")
        self.per_bar_fill_button = QtWidgets.QPushButton(self.options)
        self.per_bar_fill_button.setGeometry(QtCore.QRect(0, 10, 241, 41))
        self.per_bar_fill_button.setFlat(False)
        self.per_bar_fill_button.setObjectName("per_bar_fill_button")
        self.save_button = QtWidgets.QPushButton(self.options)
        self.save_button.setGeometry(QtCore.QRect(280, 10, 241, 41))
        self.save_button.setFlat(False)
        self.save_button.setObjectName("save_button")
        self.delete_button = QtWidgets.QPushButton(self.options)
        self.delete_button.setGeometry(QtCore.QRect(560, 10, 241, 41))
        self.delete_button.setFlat(False)
        self.delete_button.setObjectName("delete_button")
        self.delete_confirmation_button = QtWidgets.QPushButton(self.options)
        self.delete_confirmation_button.setEnabled(False)
        self.delete_confirmation_button.setGeometry(QtCore.QRect(260, 220, 281, 81))
        self.delete_confirmation_button.setAutoFillBackground(False)
        self.delete_confirmation_button.setText("")
        self.delete_confirmation_button.setCheckable(False)
        self.delete_confirmation_button.setAutoDefault(False)
        self.delete_confirmation_button.setDefault(False)
        self.delete_confirmation_button.setFlat(True)
        self.delete_confirmation_button.setObjectName("delete_confirmation_button")
        self.close_confirmation_button = QtWidgets.QPushButton(self.options)
        self.close_confirmation_button.setEnabled(False)
        self.close_confirmation_button.setGeometry(QtCore.QRect(520, 220, 20, 20))
        self.close_confirmation_button.setText("")
        self.close_confirmation_button.setFlat(True)
        self.close_confirmation_button.setObjectName("close_confirmation_button")
        self.pages.addWidget(self.options)
        self.stats_button = QtWidgets.QPushButton(self.centralwidget)
        self.stats_button.setGeometry(QtCore.QRect(10, 200, 61, 41))
        self.stats_button.setObjectName("stats_button")
        self.upgrades_button = QtWidgets.QPushButton(self.centralwidget)
        self.upgrades_button.setGeometry(QtCore.QRect(10, 100, 61, 41))
        self.upgrades_button.setObjectName("upgrades_button")
        self.pages.raise_()
        self.home_button.raise_()
        self.options_button.raise_()
        self.diamonds_button.raise_()
        self.stats_button.raise_()
        self.upgrades_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Idle Game"))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.options_button.setText(_translate("MainWindow", "Options"))
        self.diamonds_button.setText(_translate("MainWindow", "Diamonds"))
        self.yuri_profit_label.setText(_translate("MainWindow", "+3.00e3 Gold"))
        self.mine_button.setText(_translate("MainWindow", "Mine (+1 Gold)"))
        self.slaves_profit_label.setText(_translate("MainWindow", "+52 Gold"))
        self.rats_button.setText(_translate("MainWindow", "10 Gold"))
        self.machines_label.setText(_translate("MainWindow", "Machines: 0"))
        self.gold_label.setText(_translate("MainWindow", "Gold: 0.0"))
        self.chemical_profit_label.setText(_translate("MainWindow", "+1.00e3 Gold"))
        self.yuri_label.setText(_translate("MainWindow", "Yuri: 0"))
        self.rats_profit_label.setText(_translate("MainWindow", "+1 Gold"))
        self.yuri_button.setText(_translate("MainWindow", "1.25e4 Gold"))
        self.flame_profit_label.setText(_translate("MainWindow", "+12 Gold"))
        self.slaves_button.setText(_translate("MainWindow", "350 Gold"))
        self.chemical_button.setText(_translate("MainWindow", "5.00e3 Gold"))
        self.flame_button.setText(_translate("MainWindow", "100 Gold"))
        self.flame_label.setText(_translate("MainWindow", "Flame Throwers: 0"))
        self.machines_profit_label.setText(_translate("MainWindow", "+170 Gold"))
        self.slaves_label.setText(_translate("MainWindow", "Slaves: 0"))
        self.machines_button.setText(_translate("MainWindow", "1.00e3 Gold"))
        self.chemical_label.setText(_translate("MainWindow", "Chemical Bombs: 0"))
        self.rats_label.setText(_translate("MainWindow", "Rats: 0"))
        self.multiplier_label.setText(_translate("MainWindow", "Buy:"))
        self.multiplier_button.setText(_translate("MainWindow", "1X"))
        self.aliens_label.setText(_translate("MainWindow", "Aliens: 0"))
        self.soraka_label.setText(_translate("MainWindow", "Sorakas: 0"))
        self.soraka_profit_label.setText(_translate("MainWindow", "+1.90e11 Gold"))
        self.aliens_profit_label.setText(_translate("MainWindow", "+1.30e5 Gold"))
        self.soraka_button.setText(_translate("MainWindow", "6.66e11 Gold"))
        self.aliens_button.setText(_translate("MainWindow", "7.78e5 Gold"))
        self.babushka_label.setText(_translate("MainWindow", "Babushkas: 0"))
        self.babushka_button.setText(_translate("MainWindow", "1.30e8 Gold"))
        self.hole_button.setText(_translate("MainWindow", "2.13e5 Gold"))
        self.babushka_profit_label.setText(_translate("MainWindow", "+1.75e7 Gold"))
        self.hole_label.setText(_translate("MainWindow", "Black Holes: 0"))
        self.hole_profit_label.setText(_translate("MainWindow", "+2.67e4 Gold"))
        self.hole5x_button.setText(_translate("MainWindow", "Black Holes 5X (15 Black Holes)"))
        self.rats5x_button.setText(_translate("MainWindow", "Rats 5X (30 Rats)"))
        self.everything10x_button.setText(_translate("MainWindow", "Everything 10X (40 Everything)"))
        self.soraka5x_button.setText(_translate("MainWindow", "Sorakas 5X (10 Sorakas)"))
        self.yuri5x_button.setText(_translate("MainWindow", "Yuri 5X (20 Yuris)"))
        self.everything5x1_button.setText(_translate("MainWindow", "Everything 5X (20 Everything)"))
        self.aliens5x_button.setText(_translate("MainWindow", "Aliens 5X (15 Aliens)"))
        self.flame5x_button.setText(_translate("MainWindow", "Flame Throwers 5X (30 Flame Throwers)"))
        self.chemical5x_button.setText(_translate("MainWindow", "Chemical Bombs 5X (20 Chemical Bombs)"))
        self.slaves5x_button.setText(_translate("MainWindow", "Slaves 5X (25 Slaves)"))
        self.babushka5x_button.setText(_translate("MainWindow", "Babushkas 5X (10 Babushkas)"))
        self.machines5x_button.setText(_translate("MainWindow", "Machines 5X (25 Machines)"))
        self.everything5x2_button.setText(_translate("MainWindow", "5X again (20 Everything)"))
        self.diamond1p1_button.setText(_translate("MainWindow", "Diamond boost + 1% (10 Everything)"))
        self.diamond1p2_button.setText(_translate("MainWindow", "Diamond boost + 1% (10 Everything)"))
        self.label2.setText(_translate("MainWindow", "Price of resource(s) stay the same*"))
        self.diamonds_label.setText(_translate("MainWindow", "Diamonds: 0"))
        self.everything2x1_button.setText(_translate("MainWindow", "Everything 2X (3.00e3 diamonds)"))
        self.everything2x2_button.setText(_translate("MainWindow", "2X again (2.50e5 diamonds)"))
        self.everything5x_button.setText(_translate("MainWindow", "5X for everybody (1.00e10 diamonds)"))
        self.label.setText(_translate("MainWindow", "These upgrades does not aply to diamonds*"))
        self.prestige_button.setText(_translate("MainWindow", "Prestige to gain 0.0 Diamonds (+0.0 per second)"))
        self.rats2x_button.setText(_translate("MainWindow", "Rats 2X (10 diamonds)"))
        self.slaves2x_button.setText(_translate("MainWindow", "Slaves 2X (20 diamonds)"))
        self.flame2x_button.setText(_translate("MainWindow", "Flame Thrower 2X (10 diamonds)"))
        self.machines2x_button.setText(_translate("MainWindow", "Machines 2X (20 diamonds)"))
        self.chemical2x_button.setText(_translate("MainWindow", "Chemical Bombs 2X (30 diamonds)"))
        self.yuri2x_button.setText(_translate("MainWindow", "Yuri 2X (30 diamonds)"))
        self.aliens2x_button.setText(_translate("MainWindow", "Aliens 2X (40 diamonds)"))
        self.babushka2x_button.setText(_translate("MainWindow", "Babushkas 2X (50 diamonds)"))
        self.hole2x_button.setText(_translate("MainWindow", "Black Holes 2X (40 diamonds)"))
        self.soraka2x_button.setText(_translate("MainWindow", "Sorakas 2X (60 diamonds)"))
        self.starting_gold_100_button.setText(_translate("MainWindow", "start session with 100 gold (100 diamonds)"))
        self.stats_label1.setText(_translate("MainWindow", "Total Gold earned in this session:"))
        self.total_session_gold_label.setText(_translate("MainWindow", "0 Gold"))
        self.stats_label3.setText(_translate("MainWindow", "Total Diamonds earned:"))
        self.total_diamonds_label.setText(_translate("MainWindow", "0 Diamonds"))
        self.stats_label5.setText(_translate("MainWindow", "Total times prestiged:"))
        self.total_prestiges_label.setText(_translate("MainWindow", "0 Prestiges"))
        self.stats_label2.setText(_translate("MainWindow", "Total Gold earned:"))
        self.total_life_gold_label.setText(_translate("MainWindow", "0 Gold"))
        self.stats_label4.setText(_translate("MainWindow", "Diamond boost:"))
        self.diamond_boost_label.setText(_translate("MainWindow", "2%"))
        self.per_bar_fill_button.setText(_translate("MainWindow", "Show gold per bar fill"))
        self.save_button.setText(_translate("MainWindow", "Manually save"))
        self.delete_button.setText(_translate("MainWindow", "Delete save"))
        self.stats_button.setText(_translate("MainWindow", "Stats"))
        self.upgrades_button.setText(_translate("MainWindow", "Upgrades"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
