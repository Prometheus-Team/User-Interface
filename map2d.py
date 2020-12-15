if __name__ == '__main__':

	import os
	import sys

	mainDirectory = os.getcwd()

	sys.path.append(mainDirectory + '\\..')

	os.chdir(mainDirectory + '\\..')


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import time

from client_data import *

import pynput
import keyboard

obstacleColor = np.array([255,255,255])
emptyColor = np.array([0,0,0])
droneColor = np.array([255,0,0])

class OwnImageWidget(QtWidgets.QWidget):
		def __init__(self, parent=None):
			super(OwnImageWidget, self).__init__(parent)
			self.image = None

		def setImage(self, image):
			self.image = image
			sz = image.size()
			self.setMinimumSize(sz)
			self.update()

		def paintEvent(self, event):
			qp = QtGui.QPainter()
			qp.begin(self)
			if self.image:
				qp.drawImage(QtCore.QPoint(0, 0), self.image)
			qp.end()


class UpdateView(QtCore.QThread):

	updated = QtCore.pyqtSignal(object)

	def __init__(self, parent=None):
		super(UpdateView, self).__init__(parent)
		self.img = ClientData.vehicleInformation.locationBitmap
		

	def run(self):
		
		imageColored=np.zeros((500, 500,3), dtype=np.uint8)
		self.img = ClientData.vehicleInformation.locationBitmap

		while True:
			#print(imageColored[255][10])
			imageColored[self.img==1] = obstacleColor
			imageColored[self.img==2] = droneColor
			
			#imageColored[250:429, 10:80]=[255,0,0]
			self.updated.emit(imageColored)
			time.sleep(1)


class MapView(QWidget):

	def __init__(self):
		super(MapView, self).__init__()
		self.label = QLabel()
		
		self.updateView = UpdateView()
		img = np.zeros((500, 500,3), dtype=np.uint8)
		img[100:200,100:200]=[255,0,0]

		pin = QPixmap(QImage(img.data, img.shape[0], img.shape[1], QImage.Format_RGB888))
		self.label.setPixmap(pin)
		layout = QVBoxLayout()
		layout.addWidget(self.label)
		self.setLayout(layout)
		self.loadStuff()

	def loadStuff(self):
		self.updateView.updated.connect(self.on_data_ready)
		self.updateView.start()
	
	def on_data_ready(self, data):
		qImg = QPixmap(QImage(data.data, data.shape[0], data.shape[1], QImage.Format_RGB888))
		self.label.setPixmap(qImg)
		self.label.update()