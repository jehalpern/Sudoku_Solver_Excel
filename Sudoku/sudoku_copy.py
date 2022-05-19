import openpyxl as xl
from data_pull import block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9
from col import col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9
from row import row_1,row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9
from classes import coordinate
wb = xl.load_workbook('sudoku.xlsx')
ws = wb['Sheet1 (3)']

print("Processing...")
alpha = ['a','b','c','d','e','f','g','h','i']
all_cells = []
for i in range(1,10):
    for j in alpha:
        all_cells.append(j + str(i))

for i in all_cells:
    coordinate(i)

    print("pass", i, "complete")

print("complete")
