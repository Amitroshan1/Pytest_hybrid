import openpyexcel


def Row_count(file,sheetname):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook[sheetname]
    return sheet.max_row

def col_count(file,sheetname):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook[sheetname]
    return sheet.max_column

def read_data(file,sheetname,rownum,colnum):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook[sheetname]
    return sheet.cell(rownum,colnum).value


def write_data(file,sheetname,row_num,col_num,data):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook[sheetname]
    sheet.cell(row_num,col_num).value=data
    workbook.save(file)


