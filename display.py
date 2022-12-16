import tkinter as tk


class ButtonBetter(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loc = (0,0)

    def printmyid(self):
        butpressed = self.loc
        print(self.loc, butpressed)

    def getloc(self):
        return self.loc

def change_butpressed(newvalue):
    butpressed = newvalue
    print(butpressed)


def buildwindow(size=(15, 15)) -> tuple:

    buts = []

    root = tk.Tk()
    root.title("A* Pathfinding Algorithm")
    root.geometry("400x480")

    topbar = tk.Canvas(root)
    topbar.grid(row=0, columnspan=size[1], pady=5)
    titlelabel = tk.Label(topbar, text=f"{size} table")
    titlelabel.pack()
    frame1 = tk.Frame(topbar, bg="grey79")
    frame1.pack()

    buttonbar = tk.Canvas(root)
    buttonbar.grid(row=1, columnspan=size[1], padx=5)
    for r in range(size[0]):
        dummylist = []
        for c in range(size[1]):
            newbut = ButtonBetter(buttonbar, text="     ", relief=tk.FLAT, bg="white")
            newbut.grid(row=r, column=c)
            # newbut.config(command=newbut.printmyid)
            newbut.loc = (r, c)
            dummylist.append(newbut)
        buts.append(dummylist)

    glabel = tk.Label(text=f"place a start node:")
    glabel.grid(row=size[0]+2,columnspan=size[1], pady=10)

    botbutton = tk.Button(text=f"next:", command=lambda: change_butpressed('next'))
    botbutton.grid(row=size[0]+3,columnspan=size[1], pady=0)


    return (root, buts, glabel, botbutton)

def update_buttons(buts, data): #you get list of buttons from above func # you get data from grid.getgrid (2d array of types)
    colordic = {0:'white', 1:'black', 2:'red', 3:'blue', 4:'grey', 5:'green'}
    for r, re in enumerate(data):
        for c, ce in enumerate(re):
            buts[r][c].config(bg=colordic[ce])





