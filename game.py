# Frist Game Ping-Pong

# baixando Interface tkinter
from asyncio import start_server
from itertools import count
from logging import root
from multiprocessing.util import log_to_stderr
from operator import length_hint
from textwrap import fill
from tkinter import *
import random
# function
import time
from tracemalloc import start
from turtle import pos
from typing_extensions import Self

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
        self.canvas.move(self.id, 245, 201)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()

        if pos[1] <= 0:
            self.y = 3
        
        if pos[3] >= self.canvas_height
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        















