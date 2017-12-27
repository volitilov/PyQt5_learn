#!PyQt/bin/env python3

from PyQt5 import QtCore, QtWidgets
import sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# print(QtCore.PYQT_VERSION_STR)
# print(QtCore.QT_VERSION_STR)

# создаю объект приложения
app = QtWidgets.QApplication(sys.argv)

# создаю объект окна
window = QtWidgets.QWidget()

# задаю текст который будет выводиться в заголовке окна
window.setWindowTitle('Первая программа на PyQt5')

# задаю размеры окна
window.resize(300, 70)

# задаю текст надписи
label = QtWidgets.QLabel('<center>Привет мир!</center>')

# создаю кнопку с надписью, & задаёт гарячие клавиши '<alt> + <З>'
# которые вызовут команду нажатие кнопки
btnQuit = QtWidgets.QPushButton('&Закрыть окно')

# создаёт вертикальный контейнер
vbox = QtWidgets.QVBoxLayout()

# добавление компонентов в вертикальный контейнер
vbox.addWidget(label)
vbox.addWidget(btnQuit)

# добавление контейнера в основное окно
window.setLayout(vbox)

# назначает обработчик сигнала clicked() кнопки, который
# генерится при её нажатии
btnQuit.clicked.connect(app.quit)

# выводит на экран окно и все компаненты
window.show()

# запускает бесконечный цикл обработки событий в приложении
sys.exit(app.exec_())