# 3/12/2024
# Amanda M
# Trying out the 2d Array because its just like doing Excel by hand


#Rows and Colomns
scores = [ [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0] ]

NUM_ROWS = 1
NUM_COLS = 20

row = 0 
while row < NUM_ROWS:
    col = 0
    while col < NUM_COLS:
#        print("You will be prompted to enter 20 elements.")
#        scores[row][col] = input('Enter a score: ')
        col = col + 1
    row = row + 1

print(scores)
