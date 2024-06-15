import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x600")
root.title("Djkstra Algorithm")

v = tk.IntVar()

menu = tk.Frame(root)
screen = tk.Frame(root)

menu.place(x=0,y=0,width=150,height=600)
screen.place(x=150,y=0,width=650,height=600)
grid = []

def clearmap():
    global screen
    screen.destroy()
    screen = tk.Frame(root)
    screen.place(x=150,y=0,width=650,height=600)

# When click creates boundary
def addnode(item):
    r, c = item
    if grid[r][c].cget("background") == "SystemButtonFace":
        grid[r][c].config(bg="Grey")
    else:
        grid[r][c].config(bg="SystemButtonFace")

def makemap():
    global width, grid, screen
    grid.clear()
    clearmap()
    if ent_size.get() == "":
        width = 10
    elif ent_size.get().isnumeric() and int(ent_size.get()) < 23:
        width = int(ent_size.get())
    else:
        messagebox.showerror("Error", "Error.")
    
    for row in range(0, width):
        temprow = []
        for col in range(0, width):
            tempbutton = tk.Button(screen, width=2, height=1, command=lambda x=(row, col):addnode(x))
            temprow.append(tempbutton)
            tempbutton.grid(row=row, column=col)
        grid.append(temprow)


##################################################################################################
# Menu Frame
lbl_mode = tk.Label(menu, text="Mode")
lbl_mode.pack()

rad = tk.Radiobutton(menu, text="Map Editing", padx = 20, variable=v, value=1)
rad.pack()

rad = tk.Radiobutton(menu, text="Path Search", padx = 20, variable=v, value=2)
rad.pack()

rad = tk.Radiobutton(menu, text="Map Setting", padx = 20, variable=v, value=3)
rad.pack()

lbl_obstacle = tk.Label(menu, text="Obstacle [%]")
lbl_obstacle.pack()

ent_size = tk.Entry(menu)
ent_size.pack()

btn_generate = tk.Button(menu, text="Generate Map", command=makemap)
btn_generate.pack()

btn_clear = tk.Button(menu, text="Clear Map", command=clearmap)
btn_clear.pack()

lbl_toolbox = tk.Label(menu, text="Toolbox: ")
lbl_toolbox.pack()

##################################################################################################
# Obstacle Frame

makemap()


root.mainloop()