import tkinter as tk
from tkinter import messagebox

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 800
root = tk.Tk()
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title(f"Djkstra Algorithm v2 {SCREEN_WIDTH}x{SCREEN_HEIGHT} ")
root.resizable(False, False)

# Frames
gui = tk.Frame(root)
display = tk.Frame(root)
dataview = tk.Frame(root)

# Frame positioning
gui.place(x=0,y=0,width=150,height=650)
display.place(x=150,y=0,width=810,height=650)
dataview.place(x=0,y=650,width=960,height=150)

def addnode(event): # Adds the nodes
    global can, graph
    python_green = "#476042"
    size = 6
    x1, y1 = (event.x - size), (event.y - size)
    x2, y2 = (event.x + size), (event.y + size)
    can.create_oval(x1, y1, x2, y2, fill = python_green)

    node = chr(len(graph) + 65)
    nodecoords = [event.x, event.y, x1, y1, x2, y2]
    graph[node] = nodecoords

    lbl_data.delete("1.0", tk.END) # clear text
    lbl_data.insert(tk.END, graph) # add text
    x, y = nodecoords[:2]
    can.create_text(event.x, y1+25, text=f"{node}")
    can.create_text(event.x, y1+45, text=f"x: {x} y: {y}")

def checknode(event): # Returns gets node from graph dictionary
    global lbl_xy
    for node in graph:
        if event.x >= graph[node][2] and event.x <=graph[node][4] and event.y >= graph[node][3] and event.y <= graph[node][5]:
            return (node)
        
def addedge(event): # Adds an edge between nodes
    global clicks, can
    node = checknode(event)
    if node != None:
        if clicks < 1:
            rcoords.append(graph[node][0])
            rcoords.append(graph[node][1])
            clicks+=1
        else:
            rcoords.append(graph[node][0])
            rcoords.append(graph[node][1])
            can.create_line(rcoords[0], rcoords[1], rcoords[2], rcoords[3], fill="red", width=2)
            rcoords.clear()
            clicks = 0

# Menu Frame (Needs to be global)
lbl_GUI = tk.Label(gui, text="GUI", bg="Grey")
lbl_DV = tk.Label(dataview, text="DATAVIEW", bg="Light Grey")
can = tk.Canvas(display, width=810, height=650)
graph = {}
clicks = 0
rcoords = []
lbl_data = tk.Text(dataview, height=5)
lbl_xy = tk.Label(gui, text="xx")

# Menu Frame
def placeGUI():
    lbl_GUI.place(x=0,y=0,width=150,height=650)
    lbl_xy.place(x=5,y=100)
    lbl_DV.place(x=0,y=0,width=960,height=150)
    can.place(x=0,y=0,width=810,height=650)
    can.bind("<Button-1>", addnode)
    can.bind("<Button-3>", addedge)
    lbl_data.place(x=0,y=0,width=960,height=150)

placeGUI()
root.mainloop()