import re

def total_salary(path):
    total = 0.0
    average = 0.0
    try:
        with open(path, 'r', encoding='utf-16', errors='ignore') as salary:
            # якщо копіюиати з прикладу завдання utf-16,  набрати вручну - utf-
            # перший раз записав в файл дані з прикладу дом. завдання,
            # і зчитало utf-16
            n_row = 0
            for el in salary.readlines():
                n_row += 1
                el2 = re.split(',',el.strip())
                total += float(el2[1])

            if n_row > 0:
               average = total/n_row
    except:
        print(f"Файл з даними зарплати {path} не знайдено")

    return total, average
total, average = total_salary("salary_file.txt") 
if total > 0:
   print(f"Загальна сума {total}  Середня сума {average:.2f}")