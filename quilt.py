from graphics import Canvas
    

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches 
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE*2, 0)
    draw_circle_patch(canvas, PATCH_SIZE*3, 0)
    # draw the second row of patches.
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE*2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE*3, PATCH_SIZE)

def draw_circle_patch(canvas, start_x, start_y):
    # TODO: your code here
    end_x=start_x+PATCH_SIZE
    end_y=start_y+PATCH_SIZE
    inset = 3
    #keep layering smaller circles with alternating colors
    for i in range (17):
        if i %2 ==0:
            color = "purple"
        else:
            color="white"
        canvas.create_oval(start_x+inset*i,start_y+inset*i,end_x-inset*i,end_y-inset*i,color)


def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 3
    for i in range (17):
    # keep layering smaller boxes with alternate colors between purple and white
        if i %2 ==0:
            color = "purple"
        else:
            color="white"
        canvas.create_rectangle(start_x+inset*i, start_y+inset*i, end_x-inset*i, end_y-inset*i, color)
        
if __name__ == '__main__':
    main()