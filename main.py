import csv
import datetime

def view():
    with open("TODO.list","r") as file:
        try:
            data = csv.reader(file)
            print("Your TODO items:")
            for line in data:
                if len(line) >= 4:
                    date, dline, title, description = line[0], line[1], line[2], line[3]
                    print(f"\nDate: {date}\nDeadline: {dline}\nTitle: {title}\nDescription:\n\t{description}")
                else:
                    print(line[0])
        except EOFError:
            print("No TODO items found / TODO is clear!!")
    
def modify():
    with open("TODO.list","r") as file:
        data = list(csv.reader(file))
    for index, line in enumerate(data):
        if len(line) >= 4:
            date, dline, title, description = line[0], line[1], line[2], line[3]
            print(f"\nIndex: {index}\nDate: {date}\nDeadline: {dline}\nTitle: {title}\nDescription:\n\t{description}")
        else:
            print(f"Index: {index}\n{line[0]}")
    mod_index = int(input("\nEnter the index of the item to modify: "))
    if 0 <= mod_index < len(data):
        dline = input("Enter a new deadline (YYYY-MM-DD) or leave blank to keep current: ")
        title = input("Enter a new one-liner title or leave blank to keep current: ")
        description = input("Enter a new description or leave blank to keep current: ")
        if dline:
            data[mod_index][1] = dline
        if title:
            data[mod_index][2] = title
        if description:
            data[mod_index][3] = description
        with open("TODO.list","w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Item modified.")
    else:
        print("Invalid index.")

def add():
    with open("TODO.list","a") as file:
        date = datetime.date.today().strftime('%Y-%m-%d')
        dline = input("Enter a deadline (YYYY-MM-DD) or leave blank for today: ")
        if not dline:
            dline = date
        title = input("Enter a one-liner title: ")
        description = input("Enter the description: ")
        csv.writer(file).writerow([date, dline, title, description])
        print("Item added.")

def clear():
    with open("TODO.list","w") as file:
        pass
    print("All TODO items cleared.")

def delete():
    with open("TODO.list","r") as file:
        data = list(csv.reader(file))
    for index, line in enumerate(data):
        if len(line) >= 4:
            date, dline, title, description = line[0], line[1], line[2], line[3]
            print(f"\nIndex: {index}\nDate: {date}\nDeadline: {dline}\nTitle: {title}\nDescription:\n\t{description}")
        else:
            print(f"Index: {index}\n{line[0]}")
    del_index = int(input("\nEnter the index of the item to delete: "))
    if 0 <= del_index < len(data):
        data.pop(del_index)
        with open("TODO.list","w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Item deleted.")
    else:
        print("Invalid index.")

def main():
    print("Welcome to GeverForget, a simple TODO list manager.")
    print("Available Commands:")
    print("     view   -  View all TODO items")
    print("     add    -  Add a new TODO item")
    print("     modify -  Modify an existing TODO item")
    print("     delete -  Delete a TODO item")
    print("     clear  -  Clear all TODO items")
    print("     exit")
    while True:
        command = input("\n> ")
        if command == "view":
            view()
        elif command == "add":
            add()
        elif command == "modify":
            modify()
        elif command == "exit":
            print("Exiting GeverForget. Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()