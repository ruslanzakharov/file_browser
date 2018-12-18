import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMenu
from PyQt5.QtCore import QDir


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.folder_tree()
        self.folder_content()

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

    def switch_folder(self, index):
        """Сменить отображаемую папку с содержимым."""
        path = self.dir_model.fileInfo(index).absoluteFilePath()
        self.table_view.setRootIndex(self.table_model.setRootPath(path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec())
