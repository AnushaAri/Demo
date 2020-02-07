import xlrd
import datetime
from re import compile


def read_sheet(model_name, tmp_dpe_txt, tmp_bootfile_txt):
    date_format = datetime.date.today()
    bootf_path = date_format.strftime(
        "%Y_Maintenance/%b_%Y/%m_%d_%Y/Boofiles_info_%m%d%Y.xlsx")
    file_path = "/home/anusha/Desktop/" + bootf_path
    work_book = xlrd.open_workbook(file_path)
    sheet = work_book.sheet_by_name(model_name)
    dpe_pattern = compile("Soak deployment")

    for row in range(sheet.nrows):
        dpe_value = sheet.cell_value(row, 0)
        if dpe_pattern.match(dpe_value):
            dpe = dpe_value.split(":")[1]
            write_to_text(tmp_dpe_txt, dpe)

    bootf_pattern = compile(r"d11")
    for row in range(sheet.nrows):
        value_bootf = sheet.cell_value(row, 0)
        if bootf_pattern.match(value_bootf):
            bootfile = value_bootf + "\n"
            write_to_text(tmp_bootfile_txt, bootfile)

    instruction = compile("Instructions")
    for row in range(sheet.nrows):
        inst = sheet.cell_value(row, 1)
        if instruction.match(inst):
            print(inst)
            print(sheet.cell_value(row + 1, 1))


def write_to_text(file_name, data):
    with open(file_name, "a") as fp:
        fp.write(data)


# main
Model_Name = "SBG10"
DPE_FILE = "DPE.txt"
BOOTFILE = "bootfile.txt"
read_sheet(Model_Name, DPE_FILE, BOOTFILE)
