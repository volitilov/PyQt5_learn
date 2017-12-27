PyQt5 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# PyQt5 представляет собой набор привязок Python для 5 версии 
# платформы приложений Qt. Qt представляет собой набор 
# библиотек C++ и средств разработки, которые включают в себя 
# независимые от платформы абстракции для графических 
# пользовательских интерфейсов, сетей, потоков, регулярных 
# выражений, баз данных SQL, SVG, OpenGL, XML, пользовательских 
# и прикладных настроек, служб позиционирования и определения 
# местоположения, NFC и Bluetooth) и доступ к облаку. PyQt5 
# реализует более 1000 таких классов как набор модулей Python.
# PyQt5 поддерживает платформы Windows, Linux, UNIX, Android, 
# OSX и iOS.

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# документация на английском:
# http://pyqt.sourceforge.net/Docs/PyQt5/

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from PyQt5 import *

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Enginio # (deprecated)
# Классы для доступа к облачным службам Qt.

QAxContainer
# Классы для доступа к элементам управления ActiveX и 
# COM-объектам

Qt3DCore
# Основные классы для поддержки симуляционных систем в режиме 
# реального времени.

Qt3DExtras
# Предварительно созданные элементы для использования с Qt3D.

Qt3DInput
# Классы для обработки пользовательского ввода при 
# использовании Qt3D.

Qt3DLogic
# Классы, которые обеспечивают синхронизацию кадров.

Qt3DRender
# Классы, которые позволяют 2D и 3D-рендеринг.

QtAndroidExtras
# Дополнительные классы, специфичные для Android.

QtBluetooth
# Классы для поддержки соединений между устройствами с поддержкой 
# Bluetooth.

QtChart
# Классы для поддержки создания 2D-диаграмм.

QtCore
# содержит классы не связанные с реализацией графического 
# интерфейса. От этого модуля зависят все остальные модули

QtDBus
# Классы для поддержки IPC с использованием протокола D-Bus.

QtDataVisualization
# Классы для поддержки визуализации данных в 3D.

QtDesigner
# Классы, позволяющие расширять Qt Designer с помощью Python.

QtGui
# содержит классы реализующие низкоуровневую работу с оконными
# элементами, обработку сигналов, вывод двухмерной графики и 
# теста, пр.

QtHelp
# содержит инструменты для создания интарактивных справочных
# сестем

QtLocation
# Классы для создания приложений сопоставления.

QtMacExtras
# Дополнительные классы, специфичные для macOS и iOS.

QtWidjets
# QtWidjets содержит классы реализующие компоненты графического
# интнрфейса: окна, надписи, кнопки, текстовые поля и др.

QtWebKit # (deprecated)
# включает низкоуровневые классы для отображения веб-страниц

QtWebKitWidgets # (deprecated)
# реализует высокоуровневые компоненты графического интерфейса
# предназначенные для вывода web-страниц и использующие модуль
# QtWebkit

QtMultimedia
# включает низкоуровневые классы для работы с мультимедиа

QtMultimediaWidgets
# реализует высокоуровневые компаненты графического интерфейса
# с мультимедиа и использующие модуль QtMultimedia

QtPrintSupport
# содержит классы, обеспечивающие поддержку печати и 
# предварительного просмотра документов

QtSql
# включает поддержку работы с базами данных, а также реализацию
# SQLite

QtSvg
# позволяет работать с векторной графикой SVG

QtOpenGL
# обеспечивает поддержку OpenGL

QtNetwork
# содержит классы предназначенные для работы с сетью

QtXml и QtXmlPatterns
# предназначенны для обработки Xml

QtWinExtras
# включает поддержку специфических возможностей Microsoft Windows

Qt
# включает классы из всех модулей сразу

QtNfc
# Классы для поддержки соединений между устройствами с поддержкой 
# NFC.

QtPositioning
# Классы для получения информации о местоположении со спутника, 
# Wi-Fi и т. Д.

QtPurchasing
# Классы для поддержки покупки приложений в магазинах приложений.

QtQml
# Классы для интеграции с языком QML.

QtQuick
# Классы для расширения приложений QML с кодом Python.

QtQuickWidgets
# Классы для рендеринга сцены QML в традиционных виджетах.

QtSensors
# Классы для доступа к аппаратным датчикам системы.

QtSerialPort
# Классы для доступа к последовательным портам системы.

QtTest
# Поддержка модульного тестирования графических приложений.

QtWebChannel
# Классы для одноранговой связи между Python и HTML / JavaScript.

QtWebEngine
# Классы для интеграции объектов QML Web Engine с Python.

QtWebEngineCore
# Основные классы Web Engine

QtWebEngineWidgets
# Веб-браузер на основе chromium.

QtWebSockets
# Классы, реализующие протокол WebSocket.

QtX11Extras
# Дополнительные классы, относящиеся к X11.

uic
# При работе с QtDesigner файлы с компанентами получают 
# расширение .ui и содержимое в xml, следовательно подключить
# файл с помощью инструкции import не получится. Для подключения
# предназначен модуль uic.



# ::::::::::::::::::::::::::::::::::::::::::::
# Преобразование .ui файла в .py
# для преобразования служит утелита pyuic5
	
pyuic5 MyForm.ui -o ui_MyForm.py
# 