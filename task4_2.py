import re

def load_data(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except:
        print("Файл не знайдено")
        return None  
    
filename = "cats_file.txt"
cats_data = load_data(filename)
if cats_data != None:
   cats_info = []
   for el in cats_data:
       el2 = re.split(',',el.strip())
       cats_info.append({"id": el2[0], "name": el2[1], "age": el2[2]})

    #print(cats_info)
   for el in cats_info:    
       print(el)    