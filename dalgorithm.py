width = 25
explored = []

def tocoords(position):
    # Convert to coords
    return position // width, position % width

def backtoposition(coords:tuple):
    # Convert to position index
    r, c = coords
    return r*width + c

def djkstras(node):
    #Search surrounding nodes
    nodecoords = tocoords(node)
    y, x = nodecoords

    # # up
    # if y!=0:
    #     y1=y-1
    #     explored.append([y1, x])
    #     djkstras(backtoposition([y1, x]))
    # else:
    #     return 0

    # # down
    if y!=width-1:
        y2=y+1
        newcoords = [y2, x]
        explored.append(newcoords)
        print(newcoords)
        djkstras(backtoposition(newcoords))
        # time.sleep(0.5)
    # else:
    #     return 0
        
    # # left
    # if x!=0:
    #     x1=x-1
    #     explored.append([y, x1])
    #     djkstras(backtoposition([y, x1]))
    # else:
    #     return 0

    # right
    # if x!=width-1:
    #     x2=x+1
    #     explored.append([y, x2])
    #     djkstras(backtoposition([y, x2]))
    # else:
    #     return 0
    
djkstras(0)