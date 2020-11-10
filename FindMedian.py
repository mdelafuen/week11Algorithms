import openpyxl
from us_state_abbrev import us_state_abbrev
from Count import get_excel_data
import openpyxl.utils


def get_key(housing_tuple):
    return housing_tuple[1]


def main():
    housing_cost_Excel_file = get_excel_data("State_Housing.xlsx")
    State_housing_cost_list = []
    total = 0
    count = 0
    for row in housing_cost_Excel_file:
        state_name = row[1].value
        if state_name in us_state_abbrev:
            # 'in' means is it anywhere inside this list? == only returns one match
            count +=1
            col_num = openpyxl.utils.column_index_from_string("JR")-1
            home_cost = row[col_num].value
            total = total + home_cost
            data_tuple = (state_name, home_cost)
            State_housing_cost_list.append(data_tuple)
    State_housing_cost_list.sort(key=get_key) # NO PARENTHESIS AFTER get_key OR THIS WONT WORK. IT IS A POINTER!
    average_cost = total/count
    middle = len(State_housing_cost_list)//2 # divide divide drops the remainder in the division
    median_tuple = State_housing_cost_list[middle]
    print(f"{median_tuple[0]} has the median cost house price of ${median_tuple[1]}")
    print(f"While the average is {average_cost:.2f}")

main()