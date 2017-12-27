from PyQt5 import QtWidgets, uic
import sys

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# class MyWidget(QtWidgets.QWidget):
# 	def __init__(self, parent=None):
# 		QtWidgets.QWidget.__init__(self, parent)
# 		Form, _ = uic.loadUiType('MyForm.ui')
# 		self.ui = Form()
# 		self.ui.setupUi(self)
# 		self.ui.button.clicked.connect(QtWidgets.qApp.quit)


Form, _ = uic.loadUiType('MyForm.ui')
class MyWidget(QtWidgets.QWidget, Form):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.button.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MyWidget()
	window.show()
	sys.exit(app.exec_())