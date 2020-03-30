#PDF转PNG主程序
# -*- coding: utf-8 -*-
import os , sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from ico import * # 调用ico图片
from conver import * # 调用转换程序
#UI窗口
class Ui_MainWindow(object):
    # 创建GUI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(550, 270)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':g.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off) #注意此处g.ico 前的:号
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 531, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.PDFPathEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PDFPathEdit.setGeometry(QtCore.QRect(100, 40, 341, 30))
        self.PDFPathEdit.setEnabled(False)
        self.PDFPathEdit.setObjectName("PDFPathEdit")
        self.PDFPathButton = QtWidgets.QPushButton(self.groupBox)
        self.PDFPathButton.setGeometry(QtCore.QRect(450, 40, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.PDFPathButton.setFont(font)
        self.PDFPathButton.setObjectName("PDFPathButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 531, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.PNGPathButton = QtWidgets.QPushButton(self.groupBox_2)
        self.PNGPathButton.setGeometry(QtCore.QRect(450, 40, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.PNGPathButton.setFont(font)
        self.PNGPathButton.setObjectName("PNGPathButton")
        self.PNGPathEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.PNGPathEdit.setEnabled(False)
        self.PNGPathEdit.setGeometry(QtCore.QRect(100, 40, 341, 30))
        self.PNGPathEdit.setObjectName("PNGPathEdit")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setEnabled(False)
        self.OKButton.setGeometry(QtCore.QRect(240, 220, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.OKButton.setFont(font)
        self.OKButton.setObjectName("OKButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF to PNG"))
        self.groupBox.setTitle(_translate("MainWindow", "PDF选取"))
        self.PDFPathButton.setText(_translate("MainWindow", "浏 览"))
        self.label_2.setText(_translate("MainWindow", "选择文件："))
        self.groupBox_2.setTitle(_translate("MainWindow", "PNG保存"))
        self.PNGPathButton.setText(_translate("MainWindow", "浏 览"))
        self.label.setText(_translate("MainWindow", "保存位置："))
        self.OKButton.setText(_translate("MainWindow", "转  换"))
#继承窗口UI类
class MyWindowsMain(QMainWindow, Ui_MainWindow):
    # 初始化主窗口
    def __init__(self):
        super(MyWindowsMain, self).__init__()
        self.setupUi(self)
        self.PDFPathButton.clicked.connect(self.PDFPathButtonClick)
        self.PNGPathButton.clicked.connect(self.PNGPathButtonClick)
        self.OKButton.clicked.connect(self.OKButtonClick)
        self.setFixedSize(self.width(), self.height())  # 禁止窗口最大化
    def PDFPathButtonClick(self):
        # 选择PDF文件
        openfile_name = QFileDialog.getOpenFileName(self, "选择PDF文件", '*.pdf')
        if openfile_name[0] != '':
            self.PDFPathEdit.setText(openfile_name[0].replace('/', '\\'))
            PNG_Path, tempfilename = os.path.split(self.PDFPathEdit.text())
            self.PNGPathEdit.setText(PNG_Path)
            self.OKButton.setEnabled(1)  # 开启按键
    def PNGPathButtonClick(self):
        # 选PNG文件保存位置
        dir_path = QFileDialog.getExistingDirectory(self, "选择PNG文件保存位置").replace('/', '\\')
        if dir_path != '':
            self.PNGPathEdit.setText(dir_path)
    def OKButtonClick(self):
        self.OKButton.setEnabled(0)
        # 创建PDF转PNG类实例
        conver1=conver(self.PDFPathEdit.text(),self.PNGPathEdit.text(),0)
        conver1.conver()
        # 转换完成提示
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("已全部转换完成,共转换  " + str(conver1.count) + "  页！")
        infoBox.setWindowTitle("提示")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.button(QMessageBox.Ok).animateClick(5 * 1000)  # 5秒自动关闭
        infoBox.exec_()
        # 打开转换后文件所在目录
        os.system('""{}" "{}"'.format('explorer.exe', self.PNGPathEdit.text()))
        self.PDFPathEdit.setText('')
        self.PNGPathEdit.setText('')
if __name__ == '__main__':
    # 主程序入口
    app = QApplication(sys.argv)
    main = MyWindowsMain()
    main.show()
    sys.exit(app.exec_())
