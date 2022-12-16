import astarimproved as asi
import display


# empty by default, detect change
global butpressed
butpressed = ()

# step 0 : choose start node
# step 1 : choose end node
# step 2 : choose barriers
global step
step = 0

startxy = ()
endxy = ()
barriers = []
def setstartxy(loc):
    startxy = loc
    print('startxy is now', loc)
def setendxy(loc):
    endxy = loc
    print('endxy is now', loc)
def addbarrier(loc):
    print('barriers added', loc)
    barriers.append(loc)
def stepforward(step):
    print('step forward')
    step += 1
    # if step == 1
# first script creates an empty window
root, buts, glabel, botbutton = display.buildwindow()
# assign bot button has stepforward
botbutton.config(command=stepforward(step))
for r in buts:
    for c in r:
        print(c.getloc())
        c.config(command=lambda: setstartxy(c.getloc()))




# second script creates a grid object
grid = asi.creategrid(id=0)



display.update_buttons(buts, grid.get_grid())  # update the display to reflect the actual grid


root.mainloop()



asi.quicksolve(grid, display=True, skip=False)

asi.backtrack(grid)

grid.draw_simple()







