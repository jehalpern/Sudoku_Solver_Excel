import openpyxl as xl
from data_pull import block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9
from col import col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9
from row import row_1,row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9
from classes import coordinate
wb = xl.load_workbook('sudoku.xlsx')
ws = wb['Sheet1 (3)']

print("Processing...")
for i in range(1,101):
    coordinate('a1')
    coordinate('a2')
    coordinate('a3')
    coordinate('b1')
    coordinate('b2')
    coordinate('b3')
    coordinate('c1')
    coordinate('c2')
    coordinate('c3')
    coordinate('d1')
    coordinate('d2')
    coordinate('d3')
    coordinate('e1')
    coordinate('e2')
    coordinate('e3')
    coordinate('f1')
    coordinate('f2')
    coordinate('f3')
    coordinate('g1')
    coordinate('g2')
    coordinate('g3')
    coordinate('h1')
    coordinate('h2')
    coordinate('h3')
    coordinate('i1')
    coordinate('i2')
    coordinate('i3')
    coordinate('a4')
    coordinate('a5')
    coordinate('a6')
    coordinate('b4')
    coordinate('b5')
    coordinate('b6')
    coordinate('c4')
    coordinate('c5')
    coordinate('c6')
    coordinate('d4')
    coordinate('d5')
    coordinate('d6')
    coordinate('e4')
    coordinate('e5')
    coordinate('e6')
    coordinate('f4')
    coordinate('f5')
    coordinate('f6')
    coordinate('g4')
    coordinate('g5')
    coordinate('g6')
    coordinate('h4')
    coordinate('h5')
    coordinate('h6')
    coordinate('i4')
    coordinate('i5')
    coordinate('i6')
    coordinate('a7')
    coordinate('a8')
    coordinate('a9')
    coordinate('b7')
    coordinate('b8')
    coordinate('b9')
    coordinate('c7')
    coordinate('c8')
    coordinate('c9')
    coordinate('d7')
    coordinate('d8')
    coordinate('d9')
    coordinate('e7')
    coordinate('e8')
    coordinate('e9')
    coordinate('f7')
    coordinate('f8')
    coordinate('f9')
    coordinate('g7')
    coordinate('g8')
    coordinate('g9')
    coordinate('h7')
    coordinate('h8')
    coordinate('h9')
    coordinate('i7')
    coordinate('i8')
    coordinate('i9')
    print("pass", i, "complete")

print("complete")
