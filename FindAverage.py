import openpyxl
import openpyxl.utils
from Count import get_excel_data

def FindAverage():
    game_data = get_excel_data("games-features.xlsx")
    count = -1
    total = 0
    for game_row in game_data:
        count +=1
        column_number = openpyxl.utils.column_index_from_string("P")-1
        owners_count = game_row[column_number].value
        if type(owners_count) is str:
            continue
        total = total + owners_count
    average_owners_count = total / count
    print(f"Each game is owned by an average of {average_owners_count:.2f} owners per game")


FindAverage()