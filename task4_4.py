def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if str(args[0]).strip() in contacts:
        contacts[name] = phone
    else:
        return "Контакт не знайдено."     
    return "Contact updated."
# python e:\MyStudy\task4_4.py
def show_phone(args, contacts):
    name = args[0]
    if str(args[0]).strip() in contacts:
       return contacts[name]
    else:
        return "Контакт не знайдено."     

def all(contacts):
    #print(contacts)
    for el in contacts:
        print(el+"  "+contacts.get(el))
    return 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                print(add_contact(args, contacts))
                print(contacts)
            except ValueError:
                print("Невірна кількість введених параметрів") 
                print(contacts)
        elif command == "change":          
            try:
                print(change_contact(args, contacts))
            except ValueError:
                print("Невірна кількість введених параметрів") 
        elif command == "phone":          
            try:
                print(show_phone(args, contacts))
            except ValueError:
                print("Невірна кількість введених параметрів") 
        elif command == "all":          
            try:
                all(contacts)
            except ValueError:
                print("Невірна кількість введених параметрів") 
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()