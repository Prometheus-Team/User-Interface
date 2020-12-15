
if __name__ == '__main__':

	import os
	import sys

	mainDirectory = os.getcwd()

	sys.path.append(mainDirectory + '\\..')

	os.chdir(mainDirectory + '\\..')

import time
import pygame
from pygame.locals import *
import threading
import os
from ctypes import windll

from client_data import *

class Loader(threading.Thread):

	def __init__(self, blitimage):
		super().__init__()
		self.blitimage = blitimage
		self.start()

	def launchSplash(self):
		pygame.init()
		self.image = pygame.image.load(self.blitimage)
		w,h = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)
		w1, h1 = self.image.get_width(), self.image.get_height()
		os.environ['SDL_VIDEO_WINDOW_POS'] = str(w//2 - w1//2) + ',' + str(h//2 - h1//2)
		self.win = pygame.display.set_mode((w1, h1), NOFRAME)
		self.image = self.image.convert()
		self.text = 'Initializing'
		self.barheight = 5
		self.w1, self.h1 = w1, h1
		pygame.font.init()
		os.environ['SDL_VIDEO_WINDOW_POS'] = '300,200'
		self.font = pygame.font.Font('resources/AdventPro-Regular.ttf',23)
		self.tick()

	def updatePercent(self):
		self.win.blit(self.image, (0,0))
		self.text = ClientData.uiInformation.loadingText
		txt = self.font.render(str(self.text) + '...', True, pygame.Color('#ffffff'))
		self.win.blit(txt, (self.w1 - 750,self.h1 - 50))
		#pygame.draw.rect(self.win, pygame.Color('#aaaaaa'), pygame.Rect((0, self.h1 - self.barheight, self.percent/100 * self.w1, self.barheight)))

	def run(self):
		self.launchSplash()
		while True:
			self.tick()

	def tick(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		if ClientData.uiInformation.depthLoaded:
			self.kill()
		self.updatePercent()
		pygame.display.update()
		pygame.time.wait(20)


	def kill(self):
		pygame.quit()
		quit()

if __name__=="__main__":

	l = Loader(r"resources/splash.png")