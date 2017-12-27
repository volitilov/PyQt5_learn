from PyQt5 import QtCore, QtWidgets

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

class MyWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.label = QtWidgets.QLabel('<h3>Привет мир!</h3>')
		self.label.setAlignment(QtCore.Qt.AlignHCenter)
		self.btnQuit = QtWidgets.QPushButton('&Закрыть окно')
		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.btnQuit)
		self.setLayout(self.vbox)
		self.btnQuit.clicked.connect(QtWidgets.qApp.quit)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
	window.setWindowTitle('Первая программа на PyQt5')
	window.resize(300, 70)
	window.show()
	sys.exit(app.exec_())