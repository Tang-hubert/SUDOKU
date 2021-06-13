def CheckMap(index_x, index_y, value):
   anwser = generateBoard()
   for i in range(9):
      for j in range(9):
         if anwser[index_x][index_y] is value:
            return True
         else:
            return False
