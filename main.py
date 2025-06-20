from graphics import Canvas
import random
import time
from ai import call_gpt
import textwrap
from datetime import date

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
pix_height=35
pix_width=35
delay= 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    create_pix(canvas) #paint the canvas with random blue tiles
    show_title(canvas) #show 'Today's fortune'
    show_fortune(canvas) # print today's fortune
    show_bye(canvas) #greetings and today's date
    
def create_pix(canvas):
    color_list=[
        '#0000ff',
        '#89CFF0',
        '#0096FF',
        '#0047AB',
        '#6495ED',
        '#00008B',
        '#6F8FAF',
        '#1434A4',
        '#1F51FF',
        '#4169E1',
        '#0F52BA'
    ]
    left_x=0
    top_y=0
    run_times=int(CANVAS_HEIGHT/pix_height) #get the number of times to repeat tile rows
    for i in range(run_times+1):
        left_x=0
        while left_x<CANVAS_WIDTH:
            color=random.choice(color_list)
            right_x=left_x + pix_width
            bottom_y=top_y+pix_height
            pix=canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            color
            )
            left_x+=pix_width
            #time.sleep(delay)
        top_y=top_y+pix_height
            
def show_fortune(canvas):
    fortune=call_gpt("what is today's fortune cookie in 5 words?")
    canvas.create_text(
         CANVAS_WIDTH/10,
         CANVAS_HEIGHT/2,
         text= fortune,
         font='calibri',
         font_size=20,
         color='white',
         )
def show_title(canvas):
    canvas.create_text(
        CANVAS_WIDTH/10,
        (CANVAS_HEIGHT/2)-50,
        text="Today's fortune :) ",
        font='calibri',
        font_size=20,
        color='white')

def show_bye(canvas):
    today=str(date.today())
    canvas.create_text(
        CANVAS_WIDTH/10,
        CANVAS_HEIGHT/2+50,
        text="Enjoy the day! "+today,
        font='calibri',
        font_size=20,
        color='white'
        )
if __name__ == '__main__':
    main()