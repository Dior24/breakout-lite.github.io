from tkinter import *
import time
from PIL import Image, ImageTk

from settings import *
from objects import *

tk = Tk()

tk.title(GAME_NAME)
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=WIDHT, height=HEIGHT, highlightthickness=0)
canvas.pack()
tk.update()

background = PhotoImage(file='background.gif')
width = background.width()
height = background.height()
for x in range(2):
    for y in range(2):
        canvas.create_image(x * width, y * height,
                            image=background, anchor='nw')

paddle = Paddle(canvas, COLOR_PADDLE, SIZE_PADDLE)
score = Score(canvas, COLOR_SCORE, SIZE_SCORE, INDENTS_IN_PIXELS)
ball = Ball(canvas, paddle, score, COLOR_BALL, SIZE_BALL)



while not ball.hit_bottom:

    if paddle.game_started:
        ball.draw(COLOR_END_TEXT, SIZE_TEXT)
        paddle.draw()

    tk.update_idletasks()
    tk.update()

    time.sleep(0.007)

time.sleep(3)
