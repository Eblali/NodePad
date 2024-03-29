# Form implementation generated from reading ui file '.\NotepadDemo.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")

        # This code add a sub menu
        self.openRecent_menu = QtWidgets.QMenu(parent=self.menu_File)
        self.openRecent_menu.setObjectName("openRecent_menu")


        self.menu_Edit = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Format = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Format.setObjectName("menu_Format")
        self.menu_View = QtWidgets.QMenu(parent=self.menubar)
        self.menu_View.setObjectName("menu_View")
        self.menuZoom = QtWidgets.QMenu(parent=self.menu_View)
        self.menuZoom.setObjectName("menuZoom")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea, self.toolBar_2)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_3 = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar_3)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPrint = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/print.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/printprev.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint_Preview.setIcon(icon4)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionExport_PDF = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/pdf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExport_PDF.setIcon(icon5)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCopy.setIcon(icon7)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/paste.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPaste.setIcon(icon8)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtGui.QAction(parent=MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/cut.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCut.setIcon(icon9)
        self.actionCut.setObjectName("actionCut")
        self.actionUndo = QtGui.QAction(parent=MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/undo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUndo.setIcon(icon10)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(parent=MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/redo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRedo.setIcon(icon11)
        self.actionRedo.setObjectName("actionRedo")
        self.actionBold = QtGui.QAction(parent=MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/bold.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBold.setIcon(icon12)
        font = QtGui.QFont()
        font.setBold(True)
        self.actionBold.setFont(font)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(parent=MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/italic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionItalic.setIcon(icon13)
        font = QtGui.QFont()
        font.setItalic(True)
        self.actionItalic.setFont(font)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtGui.QAction(parent=MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/underline.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUnderline.setIcon(icon14)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.actionUnderline.setFont(font)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionLeft = QtGui.QAction(parent=MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLeft.setIcon(icon15)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtGui.QAction(parent=MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRight.setIcon(icon16)
        self.actionRight.setObjectName("actionRight")
        self.actionCenter = QtGui.QAction(parent=MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCenter.setIcon(icon17)
        self.actionCenter.setObjectName("actionCenter")
        self.actionJustify = QtGui.QAction(parent=MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/justify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionJustify.setIcon(icon18)
        self.actionJustify.setObjectName("actionJustify")
        self.actionColor = QtGui.QAction(parent=MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionColor.setIcon(icon19)
        self.actionColor.setObjectName("actionColor")
        self.actionFont = QtGui.QAction(parent=MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionFont.setIcon(icon20)
        self.actionFont.setObjectName("actionFont")
        self.actionView_Help = QtGui.QAction(parent=MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/aboutqt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionView_Help.setIcon(icon21)
        self.actionView_Help.setObjectName("actionView_Help")
        self.actionSend_Feedback = QtGui.QAction(parent=MainWindow)
        self.actionSend_Feedback.setObjectName("actionSend_Feedback")
        self.actionAbout_NotePad = QtGui.QAction(parent=MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout_NotePad.setIcon(icon22)
        self.actionAbout_NotePad.setObjectName("actionAbout_NotePad")
        self.actionStatus_Bar = QtGui.QAction(parent=MainWindow)
        self.actionStatus_Bar.setCheckable(True)
        self.actionStatus_Bar.setChecked(True)
        self.actionStatus_Bar.setObjectName("actionStatus_Bar")
        self.actionZoom_In = QtGui.QAction(parent=MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icons/magnifier-zoom-in.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionZoom_In.setIcon(icon23)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtGui.QAction(parent=MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icons/magnifier-zoom-out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionZoom_Out.setIcon(icon24)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionRestore_Default_Zoom = QtGui.QAction(parent=MainWindow)
        self.actionRestore_Default_Zoom.setObjectName("actionRestore_Default_Zoom")
        self.menu_File.addAction(self.actionNew)
        self.menu_File.addAction(self.actionOpen)
        # this code add action to open files menu
        self.menu_File.addAction(self.openRecent_menu.menuAction())

        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionSave_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionPrint)
        self.menu_File.addAction(self.actionPrint_Preview)
        self.menu_File.addAction(self.actionExport_PDF)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menu_Edit.addAction(self.actionCopy)
        self.menu_Edit.addAction(self.actionPaste)
        self.menu_Edit.addAction(self.actionCut)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionUndo)
        self.menu_Edit.addAction(self.actionRedo)
        self.menu_Format.addAction(self.actionBold)
        self.menu_Format.addAction(self.actionItalic)
        self.menu_Format.addAction(self.actionUnderline)
        self.menu_Format.addSeparator()
        self.menu_Format.addAction(self.actionLeft)
        self.menu_Format.addAction(self.actionRight)
        self.menu_Format.addAction(self.actionCenter)
        self.menu_Format.addAction(self.actionJustify)
        self.menu_Format.addSeparator()
        self.menu_Format.addAction(self.actionColor)
        self.menu_Format.addAction(self.actionFont)
        self.menuZoom.addAction(self.actionZoom_In)
        self.menuZoom.addAction(self.actionZoom_Out)
        self.menuZoom.addAction(self.actionRestore_Default_Zoom)
        self.menu_View.addAction(self.menuZoom.menuAction())
        self.menu_View.addAction(self.actionStatus_Bar)
        self.menu_Help.addAction(self.actionView_Help)
        self.menu_Help.addAction(self.actionSend_Feedback)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionAbout_NotePad)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Format.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar_2.addAction(self.actionCopy)
        self.toolBar_2.addAction(self.actionPaste)
        self.toolBar_2.addAction(self.actionCut)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionUndo)
        self.toolBar_2.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionPrint_Preview)
        self.toolBar.addAction(self.actionExport_PDF)
        self.toolBar_3.addAction(self.actionBold)
        self.toolBar_3.addAction(self.actionItalic)
        self.toolBar_3.addAction(self.actionUnderline)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.actionLeft)
        self.toolBar_3.addAction(self.actionRight)
        self.toolBar_3.addAction(self.actionCenter)
        self.toolBar_3.addAction(self.actionJustify)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.actionColor)
        self.toolBar_3.addAction(self.actionFont)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.actionZoom_In)
        self.toolBar_3.addAction(self.actionZoom_Out)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NotePad+"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))

        # We create thes menu later
        self.openRecent_menu.setTitle(_translate("MainWindow", "Open &Recent"))

        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_Format.setTitle(_translate("MainWindow", "&Format"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "Create new file"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open a file"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save &As..."))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))
        self.actionPrint_Preview.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export PDF"))
        self.actionExport_PDF.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionUnderline.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionLeft.setShortcut(_translate("MainWindow", "Ctrl+Alt+L"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionRight.setShortcut(_translate("MainWindow", "Ctrl+Alt+R"))
        self.actionCenter.setText(_translate("MainWindow", "Center"))
        self.actionCenter.setShortcut(_translate("MainWindow", "Ctrl+Alt+C"))
        self.actionJustify.setText(_translate("MainWindow", "Justify"))
        self.actionJustify.setShortcut(_translate("MainWindow", "Ctrl+Alt+J"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionView_Help.setText(_translate("MainWindow", "View Help"))
        self.actionSend_Feedback.setText(_translate("MainWindow", "Send Feedback"))
        self.actionAbout_NotePad.setText(_translate("MainWindow", "About NotePad"))
        self.actionStatus_Bar.setText(_translate("MainWindow", "Status Bar"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionRestore_Default_Zoom.setText(_translate("MainWindow", "Restore Default Zoom"))
