from PyQt5.uic import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

loadUi('MyForm.ui', exempl_class)
# предназначена для загрузки ui файлов. Если второй аргумент
# не указан, функция возвращает ссылку на объект формы. С 
# помощью этой ссылки можно получить доступ к компонентам 
# формы и например можно назначить обработчики сигналов.


loadUiType('MyForm.ui')
# возвращает кортеж из двух элементов: ссылки на класс формы
# и ссылки на базовый класс. Так как функция возвращает ссылку
# на класс, а не экземпляр класса, можно создавать множество
# экземпляров класса
	setupUi(self)
	# после создания экземпляра класса формы необходимо 
	# вызвать данный метод и передать ему указатель self