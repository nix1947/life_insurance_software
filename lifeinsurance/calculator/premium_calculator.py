"""
Premium calculator script
""" 

import math
import json
import xlrd   


def endowment():
   
    # Basic rate settings
    with open('rate_table.json', 'r') as file_obj:
        rate = json.load(file_obj)

    adb_rate = 1.25 
    bonus_rate = 65

    # Basic min settings
    min_age = 17 

    # Basic Max settings
    max_adb = 5000000 
    max_age = 65
    max_term = max_age - min_age 

    # Payment mode settings
    monthly = 12.0 
    quarterly = 4.0
    half_yearly = 2.0
    yearly = 1.0 


    # User input fields 
    term = input("Enter term \n") 
    dob = input("Enter dob \n")
    age = input("Enter age \n") 

    sum_assured = float(input("Enter sum assured \n"))

    adb_sum_assured = float(input("Enter adb_sum_assured"))

    health_extra_rate = float(input("Health extra"))

    occoupation_rate = float(input("Enter occoupation extra rate"))

    group_discount_rate  = float(input("Group discount rate"))


    adb_occoupation_rate = 0
    
    # Base rate calculated based on age and term from user input fields. 
    base_rate = rate[age][term ]

    # Base rate after discounted. 
    final_base_rate = base_rate + occoupation_rate + health_extra_rate - group_discount_rate 

    # Adb rate 
    final_adb_rate = adb_rate + adb_occoupation_rate 

    # Basic premium yearly. 

    basic_yearly_premium =  sum_assured * final_base_rate / 10000.0
    basic_adb_premium = adb_sum_assured * final_adb_rate / 1000.0 

    total_yearly_premium = math.ceil(basic_yearly_premium +  basic_adb_premium) 

    total_half_yearly_premium =  math.ceil(total_yearly_premium * 1.3 / half_yearly)
    total_quarterly_premium = math.ceil(total_yearly_premium * 1.4 / quarterly)
    total_monthly_premium = math.ceil(total_yearly_premium * 1.6 /monthly)


    print(total_yearly_premium)
    print(total_half_yearly_premium)
    print(total_quarterly_premium)
    print(total_monthly_premium)



def excel_to_json(filename):
    """
        First key is age and second key is term 
        
    """
    # Parse the excel file and save to datbase
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    headings = sheet.row(0) # Sheet headings 
    data = {} 

    for i, row in enumerate(sheet.get_rows()):
        if i == 0:
            headings = row 
            continue    
        
        rate = {}
        
        for count, (key, cell) in enumerate(zip(headings, row)):
            # Skip the first column
            if count == 0:
                continue; 
            
            rate[int(key.value)] = cell.value # 
        
    
        data[int(row[0].value)] = rate 


    # Write data to file 
    with open("{}.json".format(filename.split(".")[0]), "w") as file_obj:
        json.dump(data, file_obj, indent=4)
    










