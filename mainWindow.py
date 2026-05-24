# -*- coding: utf-8 -*-

# Enhanced UI for Shazam-clone
# Dark futuristic aesthetic with waveform-inspired styling
# All functionality (signals/slots) preserved exactly.

from PyQt5 import QtCore, QtGui, QtWidgets


STYLESHEET = """
/* ── Global ── */
QMainWindow, QWidget#centralwidget {
    background-color: #0d0f14;
}

/* ── Table ── */
QTableWidget {
    background-color: #13161f;
    border: 1px solid #1e2435;
    border-radius: 10px;
    color: #c8d0e8;
    gridline-color: #1e2435;
    font-family: "Courier New", monospace;
    font-size: 12px;
    selection-background-color: #1f3a6e;
    selection-color: #e0e8ff;
    outline: none;
}
QTableWidget::item {
    padding: 6px 10px;
    border-bottom: 1px solid #1a1e2a;
}
QTableWidget::item:hover {
    background-color: #1a2340;
}
QHeaderView::section {
    background-color: #0d1120;
    color: #5b8cff;
    font-family: "Courier New", monospace;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 10px;
    border: none;
    border-bottom: 1px solid #1e2d55;
}
QScrollBar:vertical {
    background: #0d0f14;
    width: 6px;
    border-radius: 3px;
}
QScrollBar::handle:vertical {
    background: #2a3a6e;
    border-radius: 3px;
    min-height: 20px;
}
QScrollBar:horizontal {
    background: #0d0f14;
    height: 6px;
    border-radius: 3px;
}
QScrollBar::handle:horizontal {
    background: #2a3a6e;
    border-radius: 3px;
}

/* ── Primary Scan button ── */
QPushButton#pushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #1749c9, stop:1 #3b7bff);
    color: #ffffff;
    border: none;
    border-radius: 8px;
    font-family: "Courier New", monospace;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 3px;
    padding: 0 16px;
}
QPushButton#pushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #2059e0, stop:1 #5090ff);
}
QPushButton#pushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #0f35a0, stop:1 #2a60e0);
}

/* ── Secondary buttons ── */
QPushButton#pushButton_2,
QPushButton#pushButton_3 {
    background-color: transparent;
    color: #5b8cff;
    border: 1px solid #2a4a9e;
    border-radius: 8px;
    font-family: "Courier New", monospace;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    padding: 0 12px;
}
QPushButton#pushButton_2:hover,
QPushButton#pushButton_3:hover {
    background-color: #0f1a3a;
    border-color: #5b8cff;
    color: #a0c0ff;
}
QPushButton#pushButton_2:pressed,
QPushButton#pushButton_3:pressed {
    background-color: #0a1230;
}

/* ── Slider ── */
QSlider::groove:horizontal {
    height: 4px;
    background: #1e2435;
    border-radius: 2px;
}
QSlider::sub-page:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1749c9, stop:1 #5b8cff);
    border-radius: 2px;
}
QSlider::handle:horizontal {
    background: #ffffff;
    border: 2px solid #5b8cff;
    width: 14px;
    height: 14px;
    margin: -5px 0;
    border-radius: 7px;
}
QSlider::handle:horizontal:hover {
    background: #5b8cff;
    border-color: #a0c0ff;
}

/* ── Labels ── */
QLabel {
    color: #6a7a9e;
    font-family: "Courier New", monospace;
    font-size: 11px;
    letter-spacing: 1px;
}
QLabel#label_4 {
    color: #ffffff;
    font-size: 26px;
    font-weight: bold;
    letter-spacing: 4px;
}
QLabel#label_3 {
    color: #8aa0cc;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}
QLabel#label_5 {
    color: #8aa0cc;
    font-size: 10px;
    letter-spacing: 1px;
}
QLabel#label_6,
QLabel#label_7 {
    color: #5b8cff;
    font-size: 10px;
    letter-spacing: 1px;
}

/* ── Status bar ── */
QStatusBar {
    background-color: #0a0c10;
    color: #3a4a6e;
    font-family: "Courier New", monospace;
    font-size: 10px;
    border-top: 1px solid #141825;
}

/* ── Menu bar ── */
QMenuBar {
    background-color: #0a0c10;
    color: #6a7a9e;
    font-family: "Courier New", monospace;
    font-size: 11px;
    border-bottom: 1px solid #141825;
}
QMenuBar::item:selected {
    background-color: #141825;
    color: #a0c0ff;
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 620)
        MainWindow.setMinimumSize(QtCore.QSize(820, 620))
        MainWindow.setStyleSheet(STYLESHEET)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ── Left panel background card ──────────────────────────────────────
        self.leftCard = QtWidgets.QFrame(self.centralwidget)
        self.leftCard.setGeometry(QtCore.QRect(24, 80, 490, 460))
        self.leftCard.setStyleSheet(
            "QFrame { background-color: #13161f; border: 1px solid #1e2435;"
            " border-radius: 14px; }"
        )
        self.leftCard.setObjectName("leftCard")
        self.leftCard.lower()

        # ── Right panel background card ─────────────────────────────────────
        self.rightCard = QtWidgets.QFrame(self.centralwidget)
        self.rightCard.setGeometry(QtCore.QRect(534, 80, 262, 460))
        self.rightCard.setStyleSheet(
            "QFrame { background-color: #13161f; border: 1px solid #1e2435;"
            " border-radius: 14px; }"
        )
        self.rightCard.setObjectName("rightCard")
        self.rightCard.lower()

        # ── App title ────────────────────────────────────────────────────────
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(24, 14, 340, 52))
        font_title = QtGui.QFont("Courier New", 26)
        font_title.setBold(True)
        font_title.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 4)
        self.label_4.setFont(font_title)
        self.label_4.setObjectName("label_4")

        # Accent bar under title
        self.accentBar = QtWidgets.QFrame(self.centralwidget)
        self.accentBar.setGeometry(QtCore.QRect(24, 66, 180, 3))
        self.accentBar.setStyleSheet(
            "background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            "stop:0 #1749c9, stop:1 transparent); border-radius:2px;"
        )
        self.accentBar.setObjectName("accentBar")

        # ── Table + its column label ─────────────────────────────────────────
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(42, 94, 160, 18))
        self.label_3.setObjectName("label_3")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 116, 466, 406))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)

        # ── Divider in right panel ───────────────────────────────────────────
        def make_divider(parent, x, y, w):
            d = QtWidgets.QFrame(parent)
            d.setGeometry(QtCore.QRect(x, y, w, 1))
            d.setStyleSheet("background-color: #1e2435;")
            return d

        # ── Single-song section ──────────────────────────────────────────────
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(554, 100, 220, 16))
        self.label.setObjectName("label")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(554, 122, 222, 34))
        self.pushButton_3.setObjectName("pushButton_3")

        make_divider(self.centralwidget, 548, 172, 234)

        # ── Two-song section ─────────────────────────────────────────────────
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(554, 184, 220, 16))
        self.label_2.setObjectName("label_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(554, 206, 222, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        make_divider(self.centralwidget, 548, 256, 234)

        # ── Weight slider section ────────────────────────────────────────────
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(554, 268, 222, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(554, 292, 40, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(736, 292, 48, 16))
        self.label_7.setObjectName("label_7")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(554, 316, 226, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        make_divider(self.centralwidget, 548, 354, 234)

        # ── Scan button ──────────────────────────────────────────────────────
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(554, 388, 222, 42))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Hidden grid widget (keep for compatibility)
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # ── Signals (unchanged) ──────────────────────────────────────────────
        self.pushButton.clicked.connect(MainWindow.scan)
        self.pushButton_3.clicked.connect(MainWindow.browseOneFile)
        self.pushButton_2.clicked.connect(MainWindow.browseFiles)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shazam-clone"))
        self.label_4.setText(_translate("MainWindow", "SHAZAM-CLONE"))
        self.label_3.setText(_translate("MainWindow", "SIMILARITY INDEX"))
        self.label.setText(_translate("MainWindow", "SINGLE SONG"))
        self.label_2.setText(_translate("MainWindow", "COMPARE TWO SONGS"))
        self.label_5.setText(_translate("MainWindow", "SONG WEIGHT BALANCE"))
        self.label_6.setText(_translate("MainWindow", "SONG 1"))
        self.label_7.setText(_translate("MainWindow", "SONG 2"))
        self.pushButton_3.setText(_translate("MainWindow", "BROWSE A FILE"))
        self.pushButton_2.setText(_translate("MainWindow", "BROWSE FILES"))
        self.pushButton.setText(_translate("MainWindow", "⬡  SCAN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
