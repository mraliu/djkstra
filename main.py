import tkinter as tk, random
from tkinter import messagebox

root = tk.Tk()
root.geometry("960x720")
root.title("Djkstra Algorithm")
root.resizable(False, False)

v = tk.IntVar()
defaultwidth = 25

menu = tk.Frame(root)
screen = tk.Frame(root)

menu.place(x=0,y=0,width=150,height=600)
screen.place(x=150,y=0,width=810,height=700)
grid = []

def clearmap():
    global screen
    screen.destroy()
    screen = tk.Frame(root)
    screen.place(x=150,y=0,width=810,height=700)

# When click creates boundary
def addnode(item):
    r, c = item
    grid[r][c].config(bg="Grey") if grid[r][c].cget("background") == "SystemButtonFace" else grid[r][c].config(bg="SystemButtonFace")
        
def makemap():
    global width, grid, screen
    grid.clear()
    clearmap()
    if ent_size.get() == "":
        width = defaultwidth
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

def genobstacles():
    obstacles = []
    totalmapsize = (width * width)-1
    if not ent_size.get().isnumeric():
        messagebox.showinfo("Error", "Must be number.")
    if int(ent_size.get()) < 1 or int(ent_size.get()) > 99:
        messagebox.showinfo("Error", "Must be 1 - 99 inclusive.")
    elif ent_size.get().isnumeric():
        obstaclepercent = int(ent_size.get()) / 100
        obstacleamount = int(obstaclepercent * totalmapsize)
        lbl_obstaclesize.config(text = obstacleamount)

        # Loop through create different obstacles randomly into array
        for i in range(0, obstacleamount):
            tempobstacle = random.randint(0, totalmapsize)

            while tempobstacle in obstacles:
                tempobstacle = random.randint(0, totalmapsize)
            else:
                obstacles.append(tempobstacle)

        # Set obstacles onto grid
        for row in grid:
            for cell in row:
                cell.config(bg="SystemButtonFace")

        for obstacle in obstacles:
            try:
                grid[obstacle % width][obstacle // width].config(bg="Grey")
            except:
                print(obstacle, obstacle % width, obstacle // width)
        




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

btn_generate = tk.Button(menu, text="Generate Map", command=genobstacles)
btn_generate.pack()

# btn_clear = tk.Button(menu, text="Clear Map", command=clearmap)
# btn_clear.pack()

lbl_toolbox = tk.Label(menu, text="Obstacles: ")
lbl_toolbox.pack()

lbl_obstaclesize = tk.Label(menu, text="")
lbl_obstaclesize.pack()

lbl_info = tk.Label(menu, text="Width: " + str(defaultwidth) + " Area: " + str(defaultwidth**2))
lbl_info.pack()

##################################################################################################
# Obstacle Frame

makemap()


root.mainloop()