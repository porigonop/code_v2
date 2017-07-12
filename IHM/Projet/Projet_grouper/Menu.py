import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Menu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        #self.x = 100
        #self.y = 10
        self.pixmap = QPixmap("pie.gif")
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.liste_pixmap = [QPixmap("pie.gif"),QPixmap("pie1.gif"),QPixmap("pie2.gif"),QPixmap("pie3.gif")]
        self.pos = 0
        self.l = QLineF()
        self.show()
        self.oy = 0
        self.ox = 0
        self.showmenu = 0
        self.w = 200
        self.h = 200
        self.setMouseTracking(True);
        self.px = 0
        self.py = 0
       
       

        
    def mousePressEvent(self,event):
    	self.showmenu = 1
    	x = event.x()
    	y = event.y()
    	print(str(x)+"-"+str(y))
    	self.px = x
    	self.py = y 
    	
    	
    	self.oy = y-self.h/2
    	self.ox = x-self.w/2
    	self.update()
        
    
    def mouseMoveEvent(self,event):
    	x = event.x()
    	y = event.y()
    	self.l = QLineF(self.px,self.py,x,y)
    	#print(str(self.l.angle()))
    	pos = event.pos()
    	
    	if self.l.angle() >90 and self.l.angle() <210 and self.l.length() <self.h/2:
    		self.pos=1
    	elif self.l.angle() >210 and self.l.angle()<330 and self.l.length() <self.h/2:
    		self.pos=3
    	elif self.l.angle()>330 or self.l.angle() <90 and self.l.length() <self.h/2:
    		self.pos=2
    	else: 
    		self.pos = 0
    	self.update()
  

    def paintEvent(self, event):
        qp = QPainter(self)
        #qp.begin(self)
        #qp.setPen(Qt.red)

        if self.showmenu == 1:
        	qp.drawPixmap(self.ox,self.oy,self.w,self.h,self.liste_pixmap[self.pos])
        	#qp.drawLine(self.l)
        #qp.drawRect(self.x,self.y,100,30)
        #qp.end()
    
    def setpos(self, point):
    	self.showmenu = 1
    	x = point.x()
    	y = point.y()
    	print(str(x)+"-"+str(y))
    	self.px = x
    	self.py = y 
    	
    	
    	self.oy = y-self.h/2
    	self.ox = x-self.w/2
    	self.update()
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
