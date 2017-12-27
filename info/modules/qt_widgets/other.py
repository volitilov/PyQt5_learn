from PyQt5.QtWidgets import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# документация на английском: 
# http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html#PyQt5-QtWidgets

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

QAbstractButton()
#

QAbstractGraphicsShapeItem()
#

QAbstractItemDelegate()
#


QAbstractItemView()
#
	editTriggers()
	#


QAbstractScrollArea()
#

QAbstractSlider()
#


QAbstractSpinBox()
#
	stepEnabled()
	#


QAction()
#

QActionGroup()
#


qApp
# получение доступа к объекту приложения
	quit
	# задаёт выход из приложения


QApplication()
# создаёт объект приложения

QBoxLayout()
# 

QButtonGroup()
#

QCalendarWidget()
#

QCheckBox()
#


QColorDialog()
#
	colorDialogOptions()
	#


QColumnView()
#

QComboBox()
# 

QCommandLinkButton()
#

QCommonStyle()
#

QCompleter()
#

QDataWidgetMapper()
#

QDateEdit()
#


QDateTimeEdit()
#
	sections()
	#


QDesktopWidget()
#

QDial()
#

QDialog()
# задаёт диологовое окно. При наследовании класса QDialog, окно будет
# выравниваться по центру экрана (или по центру родительского окна) и
# иметь в зоголовке окна только две кнопки: Справка и Закрыть


QDialogButtonBox()
#
	standardButtons()
	#


QDirModel()
#


QDockWidget()
# 
	dockWidgetFeatures()
	#


QDoubleSpinBox()
#

QErrorMessage()
#


QFileDialog()
#
	options()
	#


QFileIconProvider()
#
	options()
	#


QFileSystemModel()
#

QFocusFrame()
#


QFontComboBox()
#
	fontFilters()
	#


QFontDialog()
#
	fontDialogOptions()
	#


QFormLayout()
#
	takeRowResult()
	#


QFrame()
# задаёт окно с рамкой


# Gesture ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

QGesture()
#

QGestureEvent()
#


QGestureRecognizer()
#
	result()
	#



QGridLayout()
# 

QGroupBox()
#

QHBoxLayout()
#

QHeaderView()
#


QInputDialog()
#
	inputDialogOptions()
	#

QItemDelegate()
#

QItemEditorCreatorBase()
#

QItemEditorFactory()
#

QKeyEventTransition()
#

QKeySequenceEdit()
#

QLCDNumber()
#

QLabel()
# задаёт текст надписи
	setAlignment(QtCore.Qt.AlignHCenter)
	# задаёт выравнивание текста в объекте надписи

	setText(str)
	# задаёт текст надписи, можно обернуть HTML тегами

QLayout()
#

QLayoutItem()
#

QLineEdit()
#

QListView()
#

QListWidget()
#

QListWidgetItem()
#

QMacCocoaViewContainer()
#


QMainWindow()
# предоставляет главное окно приложения с меню, панелями инструментов
# и строкой состояния
	dockOptions()
	#


QMdiArea()
# 
	areaOptions()
	#


QMdiSubWindow()
#
	subWindowOptions()
	#


QMenu()
#

QMenuBar()
#


QMessageBox()
#
	standardButtons()
	#


QMouseEventTransition()
#

QOpenGLWidget()
#

QPanGesture()
#


QPinchGesture()
#
	changeFlags()
	#


QPlainTextDocumentLayout()
#

QPlainTextEdit()
#

QProgressBar()
#

QProgressDialog()
#

QProxyStyle()
#

QPushButton(str)
# создаёт кнопку с надписью
	setDisabled(True)
	# дулает кнопку неактивной

QRadioButton()
#

QRubberBand()
#

QScrollArea()
#

QScrollBar()
#

QScroller()
#

QScrollerProperties()
#

QShortcut()
#

QSizeGrip()
#


QSizePolicy()
#
	controlTypes()
	#


QSlider()
#

QSpacerItem()
#

QSpinBox()
#

QSplashScreen()
#

QSplitter()
#

QSplitterHandle()
#

QStackedLayout()
#

QStackedWidget()
#

QStatusBar()
#

QSwipeGesture()
#

QSystemTrayIcon()
#

QTabBar()
#

QTabWidget()
#

QTableView()
#

QTableWidget()
#

QTableWidgetItem()
#

QTableWidgetSelectionRange()
#

QTapAndHoldGesture()
#

QTapGesture()
#

QTextBrowser()
#


QTextEdit()
#
	autoFormatting()
	#

	extraSelections()
	#	


QTimeEdit()
#

QToolBar()
#

QToolBox()
#

QToolButton()
#

QToolTip()
#

QTreeView()
#

QTreeWidget()
#

QTreeWidgetItem()
#


QTreeWidgetItemIterator()
#
	iteratorFlags()
	#


QUndoCommand()
#

QUndoGroup()
#

QUndoStack()
#

QUndoView()
#

QVBoxLayout()
# создаёт вертикальный контейнер, все компоненты добавляемые в этот
# контейнер, будут распологаться с верху в низ в порядке прибывания
# внутри контейнера автоматически происходит подгонка размеров 
# добавляемых компонентов под размеры контейнера. При изменении 
# размеров контейнера будет произведенно изменение размеров всех
# компонентов
	addWidget(component)
	# добавление компонента в контейнер

	setContentsMargins(0, 0, 0, 0)
	# устанавливает отступы между границами контейнера и 
	# границами соседних элементов


QWhatsThis()
#


QWidget()
# создаёт объект окна, этот класс наследует почти все классы
# графического интерфейса. И любой компонент, не имеющий родителя
# обладает своим собственным окном.
	renderFlags()
	#

	setWindowTitle(str)
	# задаёт текст который будет выводиться в заголовке окна

	setLayout(box)
	# вставляет контейнер в основное окно, таким образом контейнер
	# становится потомком основного окна

	resize(x, y)
	# задаёт размеры не самого окна, а его клиентской области,
	# размеры заголовка и ширина границ окна не учитывается.
	# если компонент не помещается в окне, оно будет увеличено


QWidgetAction()
#

QWidgetItem()
#


QWizard()
#
	wizardOptions()
	#


QWizardPage()
#