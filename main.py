import sys
import os
import subprocess
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMenu
from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QCursor


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.search_field.setText(QDir.rootPath())
        # Список использованных путей
        self.paths = [QDir.rootPath()]
        # path_ind для left, right клавиш
        self.path_ind = 0
        self.ind_hist = [0]

        self.folder_tree()
        self.folder_content()

        self.btn_left.clicked.connect(self.btn_left_act)
        self.btn_right.clicked.connect(self.btn_right_act)

    def folder_tree(self):
        """Отобразить структуру папок системы."""
        self.dir_model = QFileSystemModel()
        self.dir_model.setRootPath(QDir.rootPath())
        self.dir_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)

        self.dir_view.setModel(self.dir_model)
        self.dir_view.hideColumn(1)
        self.dir_view.hideColumn(2)
        self.dir_view.hideColumn(3)
        self.dir_view.setRootIndex(self.dir_model.index(QDir.rootPath()))

        self.dir_view.clicked.connect(self.switch_folder)

    def folder_content(self):
        """Вывести содержимое папки."""
        self.table_model = QFileSystemModel()
        self.table_model.setRootPath(QDir.rootPath())

        self.table_view.setModel(self.table_model)
        self.table_view.setRootIndex(self.table_model.index(QDir.rootPath()))
        self.table_view.setSortingEnabled(True)
        self.table_view.setRootIsDecorated(False)

        self.table_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_view.customContextMenuRequested.connect(self.context_menu)

    def switch_folder(self, index):
        """Сменить отображаемую папку с содержимым."""
        path = self.dir_model.fileInfo(index).absoluteFilePath()
        self.table_view.setRootIndex(self.table_model.setRootPath(path))

        self.change_field_text(path)

    def context_menu(self):
        """Открыть меню правой кнопкой мыши."""
        menu = QMenu()
        btn_open = menu.addAction('Оpen')

        cursor = QCursor()
        btn_open.triggered.connect(self.open_file)
        menu.exec_(cursor.pos())

    def open_file(self):
        """Открыть файл."""
        path = self.table_model.fileInfo(self.table_view.currentIndex())\
            .absoluteFilePath()

        if os.path.isfile(path):
            if os.name == 'nt':  # Для Windows
                os.startfile(path)
            elif os.name == 'posix':  # Для Linux, Mac
                subprocess.call(('xdg-open', path))
        elif os.path.isdir(path):
            # Открыть папку
            self.table_view.setRootIndex(self.table_model.setRootPath(path))

            self.change_field_text(path)

    def btn_left_act(self):
        """Сменить путь в случае нажатия на левую кнопку"""
        if self.path_ind > 0:
            self.path_ind -= 1
            new_path = self.paths[self.path_ind]
            self.search_field.setText(new_path)

            self.table_view.setRootIndex(
                self.table_model.setRootPath(new_path))

    def btn_right_act(self):
        """Сменить путь в случае нажатия на правую кнопку"""
        if self.path_ind < len(self.paths) - 1:
            self.path_ind += 1
            new_path = self.paths[self.path_ind]
            self.search_field.setText(new_path)

            self.table_view.setRootIndex(
                self.table_model.setRootPath(new_path))

    def change_field_text(self, path):
        """Сменить путь в поисковой строке и перейти туда."""
        self.paths.append(path)
        self.path_ind = len(self.paths) - 1
        self.ind_hist.append(self.path_ind)

        self.search_field.setText(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec())
