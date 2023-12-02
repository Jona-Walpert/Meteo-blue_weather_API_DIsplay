import tkinter as tk
import requests
import csv
from requests.api import head
import pygame




pygame.init()
SCREEN_WIDTH = 1920 
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


time = ["22","23","0","1","2","3"]

api_key = "YOUR_API_KEY"

text_font = pygame.font.SysFont("Arial", 35, bold=True)


def drawscreen(word):
            screen.fill((0,0,0))

            draw_text(word, text_font, (255,255,255), 800, 500)

            pygame.display.flip()

def draw_text(text, font, text_col, x, y):
          img = font.render(text, True, text_col)
          screen.blit(img, (x, y))


run = True
while run:





    data = requests.get(f'https://my.meteoblue.com/packages/basic-1h_clouds-1h?apikey={api_key}&lat=47.615&lon=7.66457&asl=308&format=csv').text


           
    tcc_arr = []

    for tcc_data in range(22,28):
          data_text = str(data).splitlines()[tcc_data].split(',')
          tcc = int(data_text[6])
          tcc_arr.append(tcc)



    for x in range(0,6):
        print("Uhrzeit: ", time[x]," Uhr" " : ", "Gesamt Wolkenbedeckung= ", tcc_arr[x], "%")



    
    drawscreen("")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    time.sleep(1000000000)
        
    