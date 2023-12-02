import tkinter as tk
import requests
from pip._vendor import requests
import csv
import time
import pygame
import sys
import threading
import ctypes
user32 = ctypes.windll.user32

api_key = "YOURAPIKEY"
logoname ="logoname.png (PICTURE IN SAME DIRECTORY AS main.py)" #255 x 255 pixels

pygame.init()
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)-70
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('API weather display')

sideoffset = (SCREEN_WIDTH - 1160) / 3

textsize = 20
text_font = pygame.font.SysFont("Arial", textsize, bold=True)


def drawscreen(word,x,offset):

    draw_text(word, text_font, (255,255,255), x, (offset+1)*20)

    pygame.display.flip()
    
def clearscreen():
    screen.fill((23, 98, 151))
    pygame.display.flip()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def getdate(x):
    date_text = str(data).splitlines()[x].split(',')
    date = date_text[0] if date_text[0] else '00:00'
    return date

def gettcc(x):
    tcc_text = str(data).splitlines()[x].split(',')
    tcc = tcc_text[6] if tcc_text[6] else '0'
    return tcc


data = requests.get(f'https://my.meteoblue.com/packages/basic-1h_clouds-1h?apikey={api_key}&lat=47.615&lon=7.66457&asl=308&format=csv').text

imp = pygame.image.load(logoname).convert()
 



def main():
    clearscreen()
    for x in range(1,24):
        result_text = getdate(x) + " Uhr" + " : " + "Gesamt Wolkenbedeckung= " + gettcc(x) + " %"
        drawscreen(result_text, sideoffset-50, x*1.6)
    for x in range(25,48):
        result_text = getdate(x) + " Uhr" + " : " + "Gesamt Wolkenbedeckung= " + gettcc(x) + " %"
        drawscreen(result_text,2* sideoffset + 580+50, (x-24)*1.6)
    screen.blit(imp, ((sideoffset+100-255)/2 + sideoffset-50 + 580, SCREEN_HEIGHT/2 - 255/2))
    pygame.display.flip()


def start_fetch_data():
    while True:
        data = requests.get(f'https://my.meteoblue.com/packages/basic-1h_clouds-1h?apikey={api_key}&lat=47.615&lon=7.66457&asl=308&format=csv').text
        main()
        time.sleep(12 * 60 * 60) # Wait for 12 hours

fetch_data_thread = threading.Thread(target=start_fetch_data)
fetch_data_thread.start()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
pygame.event.clear()



       