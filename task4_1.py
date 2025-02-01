import re

def total_salary(path):
    sal_list = []
    try:
        with open(path, 'r', encoding='utf-16', errors='ignore') as salary:
            # якщо копіюиати з прикладу завдання utf-16, yf, набрати вручну - utf-8
            n_row = 0
            total = 0
            for el in salary.readlines():
                n_row += 1
                el2 = re.split(',',el.strip())
                total += int(el2[1])
             
            sal_list.append(total)
            sal_list.append(total/n_row)
            
            return sal_list    
    except:
        print("Файл з даними зарплати не знайдено")
        return None
sal_list = total_salary("salary_file.txt") 
if sal_list != None:
    print(f"Загальна сума {sal_list[0]}  Середня сума {sal_list[1]:.2f}")         