#pylint: disable=E0611
#pylint: disable=I0011
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Equation import Equation
from Douglas_Peucker import DouglasPeucker
# pylint: disable=W0201
# pylint: disable=W0312
class Feuille(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.initmenu()

	def initUI(self):
		self.setFocusPolicy(Qt.StrongFocus)
		self.paths = []
		self.texts = []
		self.liste_equation = []
		self.current = QPolygon()
		self.select = QPolygon()
		self.ctrl = False
		self.color = QColor("black")
		self.width = 1
		self.buttonpressed = -1
		self.selected_poly = []
		self.control = False

	def initmenu(self):
		path = "photo/"
		self.liste_pixmap = [QPixmap(path+"pie.gif"),\
							QPixmap(path+"pie1.gif"),\
							QPixmap(path+"pie2.gif"),\
							QPixmap(path+"pie3.gif")]
		self.pos = 0
		self.linemenu = QLineF()
		self.show()
		self.oy = 0
		self.ox = 0
		self.showmenu = 0
		self.w = 150
		self.h = 150
		self.setMouseTracking(True);
		self.px = 0
		self.py = 0

	def paintEvent(self, event):
		qp = QPainter()
		pen = QPen()
		qp.begin(self)
		qp.setRenderHint(QPainter.Antialiasing)
		for equation in self.liste_equation:
			qp.drawPixmap(equation[1].x(), equation[1].y(),\
						equation[0].width(), equation[0].height(),\
						equation[0])
		for path in self.paths:
			pen.setColor(path[1])
			pen.setWidth(path[2])
			qp.setPen(pen)
			qp.drawPolyline(path[0])
		for text in self.texts:
			pen.setColor(text[1])
			pen.setWidth(text[2])
			qp.setPen(pen)
			qp.drawPolyline(text[0])

		pen.setColor(self.color)
		pen.setWidth(self.width)
		qp.setPen(pen)
		qp.drawPolyline(self.current)

		pen.setColor(QColor("orange"))
		qp.setPen(pen)
		for path in self.selected_poly:
			qp.drawPolyline(path[0])
		pen.setStyle(Qt.DashDotLine)
		pen.setColor(QColor("black"))
		pen.setWidth(2)
		qp.setPen(pen)
		qp.drawPolygon(self.select)


		if self.showmenu == 1:
			qp.drawPixmap(self.ox, self.oy, self.w, self.h, self.liste_pixmap[self.pos])

		qp.end()
	def keyPressEvent(self, event):
		print("key pressed : ", event.key())
		if event.key() == Qt.Key_Control:
			self.control = True
	def keyReleaseEvent(self, event):
		if event.key() == Qt.Key_Control:
			self.control = False
	def mousePressEvent(self, event):

		self.select = QPolygon()
		self.buttonpressed = event.button()
		if self.buttonpressed == Qt.RightButton:
			self.selected = QPolygon()
			self.select.append(event.pos())
		elif self.showmenu != 1:
			self.current = QPolygon()
			self.current.append(event.pos())
		self.update()

	def mouseReleaseEvent(self, event):
		if self.showmenu == 1:
			self.showmenu = 0
			if self.linemenu.length() < self.h / 2:
				if self.pos == 1:#equation de merde ! 
					self.eq = Equation(None, self, event.pos())
					self.eq.show()
				if self.pos == 3:#beautify
					new_path = []# Louliloooll Ca va faire bugger ton code 
					for index in range(len(self.selected_poly)):
						#print(str(self.selected_poly)) print ta mere 
						path = self.selected_poly[index]
						self.paths[path[1]] = (DouglasPeucker(path[0], 10),\
											 self.paths[path[1]][1],\
											self.paths[path[1]][2])
					self.selected_poly = []
				#rajouter FUQ et Poulygorn
				#
				#
				#
				#
				#print("on fait : " + str(self.pos))
			#activer commande
		elif self.showmenu != 1 and self.current != QPolygon():
			if self.control:
				self.texts.append((self.current, self.color, self.width))
			else:
				self.paths.append((self.current, self.color, self.width))
		if self.buttonpressed == Qt.RightButton:
			self.px = event.x()
			self.py = event.y()
			self.oy = event.y()-self.h/2
			self.ox = event.x()-self.w/2
			self.showmenu = 1

		self.current = QPolygon()
		self.buttonpressed = -1
		self.update()

	def mouseMoveEvent(self, event):

		if self.buttonpressed == Qt.RightButton:
			self.select.append(event.pos())
			self.selected_poly = []
			for index, path in enumerate(self.paths):
				if containspoly(self.select, path[0]):
					self.selected_poly.append((path[0], index))

		if self.showmenu == 1:
			x = event.x()
			y = event.y()
			self.linemenu = QLineF(self.px, self.py, x, y)
			pos = event.pos()
			if self.linemenu.angle() > 90 and self.linemenu.angle() < 210 and self.linemenu.length() < self.h / 2:
				self.pos = 1
			elif self.linemenu.angle() > 210 and self.linemenu.angle() < 330 and self.linemenu.length() < self.h / 2:
				self.pos = 3
			elif self.linemenu.angle() > 330 or self.linemenu.angle() < 90 and self.linemenu.length() < self.h / 2:
				self.pos = 2
			else:
				self.pos = 0
		elif self.buttonpressed == Qt.LeftButton:
			self.current.append(event.pos())
		self.update()

def containspoly(poly1: QPolygon, poly2: QPolygon):
	for point_index in range(poly2.size()-1):
		if not poly1.containsPoint(poly2.point(point_index), Qt.OddEvenFill):
			return False
	return True

