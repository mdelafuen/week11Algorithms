import openpyxl

def get_excel_data(filename):
    excel_file = openpyxl.load_workbook(filename)
    worksheet_rows = excel_file.active
    return worksheet_rows

def count_data():
    row_count = 0
    rows_to_count = get_excel_data("games-features.xlsx")
    for row_being_counted in rows_to_count:
        row_count += 1
    print(f"There are {row_count} rows in the file")

if __name__ == '__main__':
    count_data()
