import re

def load_data(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except:
        print("Файл не знайдено")
        return None  
    

def get_cats_info(path):
    cats_data = load_data(path)
    cats_info = []
    if cats_data != None:
        for el in cats_data:
            el2 = re.split(',',el.strip())
            cats_info.append({"id": el2[0], "name": el2[1], "age": el2[2]})
    return cats_info

cats_info= get_cats_info("e:\cats_file.txt")
#print(cats_info)
for el in cats_info:    
    print(el)