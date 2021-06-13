from tkinter import*

def generate_board():
    base = 3
    side = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s))
    rBase = range(base)
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # 隨機產生的數獨數字盤
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

    # 移除部分數字，產生數獨題目
    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    return board


board = generate_board()
print(board)


def showNum(a):
    var[0][1].set(a)
                

w = Tk()
w.title("數獨遊戲")
w.geometry("500x600")
w.maxsize(500, 600)
x = [115, 145, 175, 210, 240, 270, 305, 335, 365]
y = [30, 53, 76, 104, 127, 150, 178, 201, 224]
var=[[" "for i in range (9)]for j in range (9)]

content = [["C1", "C2", "C3","C4", "C5", "C6", "C7", "C8", "C9"],
           ["C10", "C11", "C12","C13", "C14", "C15", "C16", "C17", "C18"],
           ["C19", "C20", "C21","C22", "C23", "C24", "C25", "C26", "C27"],
           ["C28", "C29", "C30","C31", "C32", "C33", "C34", "C35", "C36"],
           ["C37", "C38", "C39","C40", "C41", "C42", "C43", "C44", "C45"],
           ["C46", "C47", "C48","C49", "C50", "C51", "C52", "C53", "C54"],
           ["C55", "C56", "C57","C58", "C59", "C60", "C61", "C62", "C63"],
           ["C64", "C65", "C66","C67", "C68", "C69", "C70", "C71", "C72"],
           ["C73", "C74", "C75","C76", "C77", "C78", "C79", "C80", "C81"],]

for row in range (0, 9):
    for column in range (0, 9):
        if board[row][column] == 0:
            var[row][column] = StringVar()
            content[row][column] = Entry(w, width = 3, textvariable = var[row][column], highlightcolor = "black", highlightthickness = 1).place(x=x[column], y=y[row])
                                            
        else:
            content[row][column] = Label(w, text = board[row][column], width = 3, bg = "white").place(x=x[column], y=y[row])
            
btn1 = Button(w, text = "1", width = 3, command = showNum(1)).place(x = 80, y = 260)
btn2 = Button(w, text = "2", width = 3, command = showNum(2)).place(x = 120, y = 260)
btn3 = Button(w, text = "3", width = 3, command = showNum(3)).place(x = 160, y = 260)
btn4 = Button(w, text = "4", width = 3, command = showNum(4)).place(x = 200, y = 260)
btn5 = Button(w, text = "5", width = 3, command = showNum(5)).place(x = 240, y = 260)
btn6 = Button(w, text = "6", width = 3, command = showNum(6)).place(x = 280, y = 260)
btn7 = Button(w, text = "7", width = 3, command = showNum(7)).place(x = 320, y = 260)
btn8 = Button(w, text = "8", width = 3, command = showNum(8)).place(x = 360, y = 260)
btn9 = Button(w, text = "9", width = 3, command = showNum(9)).place(x = 400, y = 260)


        
w.mainloop()

