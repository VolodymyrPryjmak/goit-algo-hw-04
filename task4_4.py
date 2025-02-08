def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Невірна кількість введених параметрів" 

def change_contact(args, contacts):
    try:
        name, phone = args
        if str(args[0]).strip() in contacts:
            contacts[name] = phone
        else:
            return "Контакт не знайдено."     
        return "Contact updated."
    except ValueError:
        return "Невірна кількість введених параметрів"

# python e:\MyStudy\task4_4.py
def show_phone(args, contacts):
    try:
        name = args[0]
        if str(args[0]).strip() in contacts:
           return contacts[name]
        else:
           return "Контакт не знайдено."     
    except ValueError:
        return "Невірна кількість введених параметрів"

def all():
    pass

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
            print(add_contact(args, contacts))
        elif command == "change":          
            print(change_contact(args, contacts))
        elif command == "phone":          
            print(show_phone(args, contacts))
        elif command == "all":          
             for el in contacts:
                  print(el+"  "+contacts.get(el))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()