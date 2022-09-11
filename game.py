# Frist Game Ping-Pong

# baixando Interface tkinter
from __future__ import barry_as_FLUFL
from asyncio import start_server
from itertools import count
from logging import root
from multiprocessing.util import log_to_stderr
from operator import length_hint, truediv
from textwrap import fill
from tkinter import *
import random
# function
import time
from tracemalloc import start
from turtle import pos
from typing_extensions import Self
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH

level = int(input("Qual o nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 502/level

# Janela raiz na qual todos os outros widgets vão. É uma instância da classe Tk.
root = Tk()
# funções Built-in de Strings
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

#programa de edição vetorial auto-contido, em que elementos como linhas, retângulos, imagens mesmo outros widgets de Tkinter podem ser dispostos, eventos de entrada tratados,
canvas = Canvas(root, width=801, height=601, bd=0,highlightthickness=0)
canvas.pack()

root.update()

#variável
count = 0
lost = False

#características tradicionais da programação orientada a objetos
class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        Self.id = canvas.create_oval(0, 0, 15, 14, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()

        if pos[1] <= 0:
            self.y = 3
        
        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        
        else:
            game_over()
            global lost
            lost = True

class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<Keypress-Left>", self.move_left)
        self.canvas.bind_all("<Keypress-Left>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        global lost

        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "black")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()        
    













        















