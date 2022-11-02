from tkinter import *

def create_map (rowsEntryVar, columnsEntryVar): #creates rows x columns 2D list - a map
    mapList = []
    for row in range(rowsEntryVar):
        tempList = []
        for column in range(columnsEntryVar):
            tempList.append(Button(root,
                            bd=0, bg="lightgray", activebackground=r"magenta3", height=3, width=3))
        mapList.append(tempList)
    return mapList

def draw_map(mapList):
    for row in range((len(mapList))):
        for column in range(len(mapList[row])-1):
            mapList[row][column].grid(row=row, column=column)
    


root = Tk()

map_list=create_map(10, 11)
btn = Button(root, text = 'Click me !', command = root.destroy)
btn2 = Button(root, text = 'Click me !', command = root.destroy)
btn3 = Button(root, text = 'Click me !', command = root.destroy)

draw_map(map_list)
btn.grid(row=0, column= 11)
btn2.grid(row=1, column= 11)
btn3.grid(row=2, column= 11)
root.title("Trabalho SO")
root.mainloop()