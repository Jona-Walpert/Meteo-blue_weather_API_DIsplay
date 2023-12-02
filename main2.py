import tkinter as tk
import requests
from pip._vendor import requests
import csv
import time
import pygame
import sys
import threading

api_key = ""

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


text_font = pygame.font.SysFont("Arial", 12, bold=False)


def drawscreen(word,x,offset):

    draw_text(word, text_font, (255,255,255), x, (offset+1)*20)

    pygame.display.flip()
    
def clearscreen():
    screen.fill((0,0,0))
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


sideoffset = SCREEN_WIDTH / 40

def main():
    clearscreen()
    for x in range(1,24):
        result_text = "Uhrzeit: " + getdate(x) + " Uhr" + " : " + "Gesamt Wolkenbedeckung= " + gettcc(x) + " %"
        drawscreen(result_text, SCREEN_WIDTH / 40, x)
    for x in range(25,48):
        result_text = "Uhrzeit: " + getdate(x) + " Uhr" + " : " + "Gesamt Wolkenbedeckung= " + gettcc(x) + " %"
        drawscreen(result_text, sideoffset + 350, x-24)


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



       