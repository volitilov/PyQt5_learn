from PyQt5 import QtWidgets, uic
import sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# app = QtWidgets.QApplication(sys.argv)
# window = uic.loadUi('MyForm.ui')
# window.button.clicked.connect(app.quit)
# window.show()
# sys.exit(app.exec_())


class MyWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		uic.loadUi('MyForm.ui', self)
		self.button.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MyWidget()
	window.show()
	sys.exit(app.exec_())