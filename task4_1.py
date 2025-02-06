import re

def total_salary(path):
    total = 0
    average = 0
    try:
        with open(path, 'r', encoding='utf-16', errors='ignore') as salary:
            # якщо копіюиати з прикладу завдання utf-16, yf, набрати вручну - utf-8
            n_row = 0
            total = 0
            for el in salary.readlines():
                n_row += 1
                el2 = re.split(',',el.strip())
                total += int(el2[1])

            average = total/n_row
    except:
        print("Файл з даними зарплати не знайдено")

    return total, average
total, average = total_salary("salary_file.txt") 
if total > 0:
   print(f"Загальна сума {total}  Середня сума {average:.2f}")