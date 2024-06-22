import tkinter as tk
from tkinter import messagebox
from playsound import playsound

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 800
root = tk.Tk()
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title(f"Djkstra Algorithm v2 {SCREEN_WIDTH}x{SCREEN_HEIGHT} ")
root.resizable(False, False)
# root.config(bg="White")

# Frames
gui = tk.Frame(root)
display = tk.Frame(root)
dataview = tk.Frame(root)

# Frame positioning
gui.place(x=0,y=0,width=150,height=650)
display.place(x=150,y=0,width=810,height=650)
dataview.place(x=0,y=650,width=960,height=150)

# Data
def playfx():
    playsound('pop.mp3')

def addnode(event):
    global can, graph
    python_green = "#476042"
    size = 6
    x1, y1 = (event.x - size), (event.y - size)
    x2, y2 = (event.x + size), (event.y + size)
    can.create_oval(x1, y1, x2, y2, fill = python_green)
    nodecoords = [event.x, event.y, x1, y1, x2, y2]
    graph.append(nodecoords)
    lbl_data.delete("1.0", tk.END) # clear text
    lbl_data.insert(tk.END, graph) # add text
    x, y = nodecoords[:2]
    can.create_text(event.x, y1+30, text=f"x: {x} y: {y}")

def checknode(event):
    global lbl_xy
    # lbl_xy.config(text={event.x, event.y})
    for x, node in enumerate(graph):
        if event.x >= node[2] and event.x <=node[4] and event.y >= node[3] and event.y <= node[5]:
            return (node)
        
def addedge(event):
    global clicks, can
    # lbl_xy.config(text={event.x, event.y})
    node = checknode(event)
    if node != None:
        if clicks < 1:
            rcoords.append(node[0])
            rcoords.append(node[1])
            clicks+=1
        else:
            rcoords.append(node[0])
            rcoords.append(node[1])
            can.create_line(rcoords[0], rcoords[1], rcoords[2], rcoords[3], fill="red", width=2)
            rcoords.clear()
            clicks = 0

# Menu Frame (Needs to be global)
lbl_GUI = tk.Label(gui, text="GUI", bg="Grey")
lbl_DV = tk.Label(dataview, text="DATAVIEW", bg="Light Grey")
can = tk.Canvas(display, width=810, height=650)
graph = []
clicks = 0
rcoords = []
lbl_data = tk.Text(dataview, height=5)
# Radio buttons
# btn_AddNode = tk.Button(gui, text="Add node", command=lambda x=1:guiEditing(x))
# btn_AddEdge = tk.Button(gui, text="Add edge", command=lambda x=2:guiEditing(x))
lbl_xy = tk.Label(gui, text="xx")

# Menu Frame
def placeGUI():
    lbl_GUI.place(x=0,y=0,width=150,height=650)
    # btn_AddNode.place(x=5,y=5)
    # btn_AddEdge.place(x=5,y=50)
    lbl_xy.place(x=5,y=100)
    lbl_DV.place(x=0,y=0,width=960,height=150)
    can.place(x=0,y=0,width=810,height=650)
    can.bind("<Button-1>", addnode)
    can.bind("<Button-3>", addedge)
    lbl_data.place(x=0,y=0,width=960,height=150)
    # can.bind("<Motion>", checknode)

placeGUI()
root.mainloop()