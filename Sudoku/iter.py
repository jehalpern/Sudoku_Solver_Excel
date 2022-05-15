import openpyxl as xl
wb = xl.load_workbook('sudoku.xlsx')

ws = wb['Sheet1 (3)']




full_ws = []
for row in ws.values:
    for value in row:
        full_ws.append(value)
while None in full_ws:
    print('x')
