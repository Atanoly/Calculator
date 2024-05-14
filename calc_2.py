from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QLineEdit, QLabel, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

app = QApplication([])

window = QWidget()
window.show()
window.setWindowTitle('Лютый калькултор')
window.setGeometry(533, 184, 300, 400)

#Все направляющие
main_line = QVBoxLayout()
line_1_H = QHBoxLayout()
line_2_H = QHBoxLayout()
line_3_H = QHBoxLayout()
line_4_H = QHBoxLayout()
line_5_H = QHBoxLayout()
line_6_H = QHBoxLayout()

#Группа с кнопками
buttons = QButtonGroup()

#Объекты на первой направляющей
label = QLineEdit('0')
line_1_H.addWidget(label, alignment = Qt.AlignRight)

#Объекты на второй направляющей
butn_AC = QPushButton('AC')
butn_pm = QPushButton('+/-')
butn_proc = QPushButton('%')
butn_split = QPushButton('/')

#Объекты нв третьей направляющей
butn_7 = QPushButton('7')
butn_8 = QPushButton('8')
butn_9 = QPushButton('9')
butn_X = QPushButton('X')

#Объекты нв четвертой направляющей
butn_4 = QPushButton('4')
butn_5 = QPushButton('5')
butn_6 = QPushButton('6')
butn_minus = QPushButton('-')

#Объекты на пятой направляющей
butn_1 = QPushButton('1')
butn_2 = QPushButton('2')
butn_3 = QPushButton('3')
butn_plus = QPushButton('+')

#Объекты на шестой направляющей
butn_0 = QPushButton('0')
butn_dot = QPushButton(',')
butn_ravno = QPushButton('=')

#Встывляем на направляющие
line_2_H.addWidget(butn_AC)#, alignment = Qt.AlignCenter)
line_2_H.addWidget(butn_pm)#, alignment = Qt.AlignCenter)
line_2_H.addWidget(butn_proc)#, alignment = Qt.AlignCenter)
line_2_H.addWidget(butn_split)#, alignment = Qt.AlignCenter)
line_3_H.addWidget(butn_7)#, alignment = Qt.AlignCenter)
line_3_H.addWidget(butn_8)#, alignment = Qt.AlignCenter)
line_3_H.addWidget(butn_9)#, alignment = Qt.AlignCenter)
line_3_H.addWidget(butn_X)#, alignment = Qt.AlignCenter)
line_4_H.addWidget(butn_4)#, alignment = Qt.AlignCenter)
line_4_H.addWidget(butn_5)#, alignment = Qt.AlignCenter)
line_4_H.addWidget(butn_6)#, alignment = Qt.AlignCenter)
line_4_H.addWidget(butn_minus)#, alignment = Qt.AlignCenter)
line_5_H.addWidget(butn_1)#, alignment = Qt.AlignCenter)
line_5_H.addWidget(butn_2)#, alignment = Qt.AlignCenter)
line_5_H.addWidget(butn_3)#, alignment = Qt.AlignCenter)
line_5_H.addWidget(butn_plus)#, alignment = Qt.AlignCenter)
line_6_H.addWidget(butn_0)#, alignment = Qt.AlignCenter)
line_6_H.addWidget(butn_dot)#, alignment = Qt.AlignCenter)
line_6_H.addWidget(butn_ravno)#, alignment = Qt.AlignCenter)

#
main_line.addLayout(line_1_H)
main_line.addLayout(line_2_H)
main_line.addLayout(line_3_H)
main_line.addLayout(line_4_H)
main_line.addLayout(line_5_H)
main_line.addLayout(line_6_H)
window.setLayout(main_line)
app.exec_()