
from functools import partial
from .ui.gui import Ui_MainWindow

from PyQt6.QtGui import QFont, QAction, QIcon
from PyQt6.QtCore import QFileInfo, Qt
from PyQt6.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt6.QtWidgets import (
    QMainWindow, QFileDialog, QLabel,
    QMessageBox, QFontDialog, QColorDialog,
)

FILTERS = ";;".join(
    ("All Files()",
     "PDF Files (*.pdf)",
     "Doc Files (*.docx)",
     "Text Files (*.txt)",
     "Python Files (*.py)",
     )
)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icons/Notepad.png"))
        self.current_open_file = None
        self.recent_files = []
        self.is_bold = False
        self.is_italic = False
        self.is_underline = False

        # Menu Signals and Slots
        self._create_menu_signals()
        # Menu Signals and Slots

        # Edit Signals and Slots
        self._create_edit_signals()
        # Edit Signals and Slots

        # Format Signals and Slots
        self._create_format_signals()
        # Format Signals and Slots

        self.show_status_bar()

        # This method create signals for status bar
        self._create_status_bar_signals()

        # This method create signals or handle event the niew menu
        self._create_view_signals()

        #This is help signals and slots
        self.help_signals()

    def help_signals(self):
        self.actionAbout_NotePad.triggered.connect(self.about)
        self.actionSend_Feedback.triggered.connect(self.send_feedback)

    def _create_status_bar_signals(self):
        """
        Creating status event handling fot status bar
        """
        self.textEdit.document().blockCountChanged.connect(self.show_block_count)
        self.textEdit.document().contentsChanged.connect(self.show_line_count)
        self.textEdit.document().contentsChanged.connect(self.show_char_count)
        self.textEdit.document().contentsChanged.connect(self.show_word_count)

    def _create_view_signals(self):
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionZoom_Out.triggered.connect(self.zoom_out)

    def _create_menu_signals(self):  # This method create signals for menu actions 
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.openRecent_menu.aboutToShow.connect(self.populate_open_recent)
        self.actionNew.triggered.connect(self.new_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.prev_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionExit.triggered.connect(self.close)

    def _create_edit_signals(self):  # This method create signals for edit actions
        """ All of this signals is build in signals """
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionCut.triggered.connect(self.textEdit.cut)

        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)

    def _create_format_signals(self):
        self.actionBold.triggered.connect(self.text_bold)
        self.actionItalic.triggered.connect(self.text_italic)
        self.actionUnderline.triggered.connect(self.text_underline)

        self.actionLeft.triggered.connect(self.align_left)
        self.actionRight.triggered.connect(self.align_right)
        self.actionCenter.triggered.connect(self.align_center)
        self.actionJustify.triggered.connect(self.justify)

        self.actionColor.triggered.connect(self.color_dialog)
        self.actionFont.triggered.connect(self.font_dialog)
    
    def closeEvent(self, event):
        if self.textEdit.document().isModified():
            rep = QMessageBox.question(
                self,
                "Exit Question",
                "Do you want save changes ?",
                QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
            )

            if rep == QMessageBox.StandardButton.Save:
                self.save_file()
                event.accept()
            elif rep == QMessageBox.StandardButton.Discard:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def zoom_in(self):
        self.textEdit.zoomIn()

    def zoom_out(self):
        self.textEdit.zoomOut()

    def get_block_count(self):
        return self.textEdit.document().lineCount()

    def get_line_count(self):
        text = self.textEdit.toPlainText()
        line = text.splitlines()
        return len(line)

    def get_word_count(self):
        text = self.textEdit.toPlainText()
        word = text.split()
        return len(word)
    
    def show_word_count(self):
        self.status_word_label.setText(f"{self.get_word_count()} words")
        self.statusbar.addPermanentWidget(self.status_word_label)

    def get_char_count(self):
        return self.textEdit.document().characterCount()

    def show_line_count(self):
        self.status_line_label.setText(f"{self.get_line_count()} lines")
        self.statusbar.addPermanentWidget(self.status_line_label)

    def show_char_count(self):
        self.status_char_label.setText(f"{self.get_char_count()} charaters")
        self.statusbar.addPermanentWidget(self.status_char_label)

    def show_status_bar(self):
        self.statusbar.showMessage("Welcome Dear User!", 3000)

        self.actionStatus_Bar.triggered.connect(self.status_hide)

        self.status_char_label = QLabel()
        self.status_char_label.setText(f"{self.get_char_count() - 1} character")
        self.statusbar.addPermanentWidget(self.status_char_label)

        self.status_word_label = QLabel()
        self.status_word_label.setText(f"{self.get_word_count()} words")
        self.statusbar.addPermanentWidget(self.status_word_label)

        self.status_block_label = QLabel()
        self.status_block_label.setText(f"{self.get_block_count()} blocks")
        self.statusbar.addPermanentWidget(self.status_block_label)

        self.status_line_label = QLabel()
        self.status_line_label.setText(f"{self.get_line_count()} lines")
        self.statusbar.addPermanentWidget(self.status_line_label)

    def status_hide(self):
        if not self.statusbar.isHidden():
            self.statusbar.hide()
        else:
            self.statusbar.show()

    def show_block_count(self):
        self.status_block_label.setText(f"{self.get_block_count()} blocks")
        self.statusbar.addPermanentWidget(self.status_block_label)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)

    def text_bold(self):
        font = QFont()
        if not self.is_bold:
            font.setBold(True)
            self.textEdit.setFont(font)
            self.is_bold = True
        else:
            font.setBold(False)
            self.textEdit.setFont(font)
            self.is_bold = False

    def text_italic(self):
        font = QFont()
        if not self.is_italic:
            font.setItalic(True)
            self.textEdit.setFont(font)
            self.is_italic = True
        else:
            font.setItalic(False)
            self.textEdit.setFont(font)
            self.is_italic = False

    def text_underline(self):
        font = QFont()
        if not self.is_underline:
            font.setUnderline(True)
            self.textEdit.setFont(font)
            self.is_underline = True
        else:
            font.setUnderline(False)
            self.textEdit.setFont(font)
            self.is_underline = False

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def new_file(self):
        if self.is_save():
            self.textEdit.clear()
            self.current_open_file = None

    def is_save(self):
        rep = None
        if self.textEdit.document().isModified():
            rep = QMessageBox.warning(
                self,
                "Application",
                "The document has been modified! \n Do you want save changes?",
                QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
            )

        if rep == QMessageBox.StandardButton.Save:
            self.save_file()
            return True
        elif rep == QMessageBox.StandardButton.Discard:
            return True
        elif rep == QMessageBox.StandardButton.Cancel:
            return False
        else:
            return True

    def save_as_file(self):
        filename, ok = QFileDialog.getSaveFileName(self, "Save File", "new", "*.txt ;; All Files()")
        if ok and filename:
            if filename != "":
                if not self.is_have_suffix(filename): filename += ".txt"
            self.save(filename)
            self.current_open_file = filename

    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            text = self.textEdit.toPlainText()
            file.write(text)
            QMessageBox.about(
                self,
                "Save File",
                "File has been saved"
            )
        
    def save_file(self):
        try:
            if self.current_open_file is not None:
                if self.textEdit.document().isModified():
                    filename = self.current_open_file
                    self.save(filename)
            else:
                self.save_as_file()
        except Exception:
            QMessageBox.warning(
                self,
                "Save Error",
                f"Sorry you can't save"
            )   

    def is_have_suffix(self, file):
        return QFileInfo(file).suffix() != ""

    def open_file(self):
        try:
            filename, ok = QFileDialog.getOpenFileName(self, "Open File", "\home", filter=FILTERS)
            self.current_open_file = filename
            if filename not in self.recent_files:
                self.recent_files.append(filename)
            if ok and filename:
                with open(filename, 'r', encoding='utf-8') as file:
                    text = file.read()
                    self.textEdit.setText(text)
        except Exception:
            QMessageBox.information(
                self,
                "Open Error",
                "Can't open this file"
            )

    def populate_open_recent(self):
        self.openRecent_menu.clear()
        actions = []
        filenames = self.recent_files
        for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.open_recent_file, filename))
            actions.append(action)
        self.openRecent_menu.addActions(actions)

    def open_recent_file(self, filename):
        with open(filename, 'r') as file:
            text = file.read()
            self.textEdit.setText(text)

    def print_file(self):
        try:
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            dialog = QPrintDialog(printer, self)

            if dialog.exec() == QPrintDialog.DialogCode.Accepted:
                self.textEdit.print(printer)
        except Exception as ex:
            QMessageBox.information(
                self,
                "Error",
                f"{ex}"
            )

    def prev_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        prev_dialog = QPrintPreviewDialog(printer, self)

        prev_dialog.paintRequested.connect(partial(self.print_preview, printer))
        prev_dialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    # This method export text to pdf file
    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", "\home directory PDF files (.pdf)")

        if fn != "":
            if not self.is_have_suffix(): fn += ".pdf"
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

    def about(self):
        QMessageBox.about(
            self,
            "About",
            "Dear users"
            "\nThis is simple notepad program"
            "\ndeveloped by Ibrahim Sadiqi"
        )

    def send_feedback(self):
        QMessageBox.information(
            self,
            "Feedback",
            "Dear users"
            "\nSend your feedback in this email:"
            "\nebrahimsadiqi769@gmail.com"
        )
    

