from PyQt5 import QtCore, QtWidgets
from my_window import MyWindow

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

class MyDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self, parent)
		self.my_widget = MyWindow()

		# производится изменение отступа между границами
		# контейнера и границами соседних элементов
		self.my_widget.vbox.setContentsMargins(0, 0, 0, 0)
		self.button = QtWidgets.QPushButton('&Изменить надпись')
		self.button2 = QtWidgets.QPushButton('&Учз надпись')
		mainBox = QtWidgets.QVBoxLayout()
		mainBox.addWidget(self.my_widget)
		mainBox.addWidget(self.button)
		mainBox.addWidget(self.button2)
		self.setLayout(mainBox)

		# назначает обработчик нажатие кнопки. В качестве параметра
		# указывается ссылка на метод on_clicked() 
		self.button.clicked.connect(self.on_clicked)
		self.button2.clicked.connect(self.on_clicked2)

	def on_clicked(self):
		self.my_widget.label.setText('<h3>Новая надпись</h3>')
		self.button.setDisabled(True)
		

	def on_clicked2(self):
		self.setContentsMargins(50, 50, 50, 50)
		self.button2.setDisabled(True)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MyDialog()
	window.setWindowTitle('Преимущества ООП стиля')
	window.resize(300, 100)
	window.show()
	sys.exit(app.exec_())