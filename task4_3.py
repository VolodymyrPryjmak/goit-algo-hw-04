import sys
from pathlib import Path
from colorama import init, Fore, Back, Style
init()

def color_print(path,directory):
    # визначимо к-ість пробілів спереду
    absolute_path = path.absolute()
    relative_path = absolute_path.relative_to(directory)
    kl_probil = len(str(absolute_path)) - len(str(relative_path))-1
    name_st = '/' + str(relative_path)
    i = 0
    st_probil = ""
    while i <= kl_probil:
        i += 1
        st_probil = st_probil +"." 
    dlya_vyvid = st_probil + name_st

    if path.is_dir():
       print(Back.GREEN + dlya_vyvid + Style.RESET_ALL)
    elif path.is_file():  
       print(Fore.YELLOW + Back.BLUE + dlya_vyvid + Style.RESET_ALL)            

    return

def show_directory(directory):
    for path in directory.iterdir():
        color_print(path,directory)
        if path.is_dir():
           show_directory(path)
    return
        
def main():
    if len(sys.argv) > 1:
        directory = Path(sys.argv[1])
        if directory.exists() and directory.is_dir():
           print(Back.RED + str(directory) + Style.RESET_ALL) 
           show_directory(directory)  
        else:   
            print(f"{directory} не існує або це не директорія") 
    else:
        print("Директорію не вказано.")    

if __name__ == "__main__":
     main()

 # python task4_3.py e:\mystudy2