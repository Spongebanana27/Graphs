
from tkinter import *
from graph import graph

bColor = "#192934"
vColor = "#838586"
eColor = "#838586"

def drawVertex(x, y, name1):
    drawnVertices[name1] = (x, y)
    g.createVertex(name1)
    canv.create_oval(x-20, y-20, x+20, y+20, fill =vColor, outline=vColor, tags=(name1))

def clicked(event):

    global click1

    items = canv.find_overlapping(event.x - 20, event.y- 20, event.x + 20, event.y + 20)

    if(len(items) > 0):
        
        print(items)

        if(click1 == ""):
            click1 = canv.itemcget(items[0], "tags")[0]
        else:
            drawEdge(str(click1), str(canv.itemcget(items[0], "tags")[0]))
            click1 = ""
            
    else:
        click1 = ""
        drawVertex(event.x, event.y, str(len(drawnVertices)))

def drawEdge(name1, name2):
    g.addEdge(name1, name2)
    canv.create_line(drawnVertices[name1][0], drawnVertices[name1][1], drawnVertices[name2][0], drawnVertices[name2][1], width = 5, fill=eColor)

drawnVertices = {}
click1 = ""

g = graph(False)

root = Tk()

frame = Frame(root, width = 900, height = 900)
frame.pack(expand = True, fill = BOTH)

canv = Canvas(frame, bg = bColor, width = 500, height = 500)
canv.bind("<Button-1>", clicked)
canv.pack(expand = True, fill = BOTH)

root.mainloop()