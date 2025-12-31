# GeverForget

A simple command-line TODO list manager written in Python. Never forget your tasks again!

## Features

- **Add Tasks**: Create new TODO items with automatic date stamping, optional deadline, title, and description.
- **View Tasks**: Display all your TODO items in a readable format.
- **Modify Tasks**: Update existing tasks (deadline, title, description).
- **Delete Tasks**: Remove specific tasks by index.
- **Clear All**: Wipe the entire TODO list.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory.

No additional dependencies are required beyond Python's standard library.

## Usage

Run the application:

```bash
python main.py
```

### Commands

- `view`: Display all TODO items.
- `add`: Add a new TODO item. You'll be prompted for:
  - Deadline (YYYY-MM-DD) or leave blank for today.
  - One-liner title.
  - Description.
- `modify`: Modify an existing item. Select by index, then update fields.
- `delete`: Delete an item by index.
- `clear`: Remove all items.
- `exit`: Quit the application.

### Data Storage

Tasks are stored in a CSV file named `TODO.list` in the same directory as the script. Each task has four fields:
- Date (automatically set to creation date)
- Deadline
- Title
- Description

## Example

```
Welcome to GeverForget, a simple TODO list manager.
Available Commands:
     view   -  View all TODO items
     add    -  Add a new TODO item
     modify -  Modify an existing TODO item
     delete -  Delete a TODO item
     clear  -  Clear all TODO items
     exit

> add
Enter a deadline (YYYY-MM-DD) or leave blank for today: 2025-12-31
Enter a one-liner title: Finish project
Enter the description: Complete the final touches on the GeverForget app.

Item added.

> view
Your TODO items:

Date: 2025-12-31
Deadline: 2025-12-31
Title: Finish project
Description:
    Complete the final touches on the GeverForget app.
```

## Contributing

Feel free to fork and submit pull requests for improvements.

## License

This project is open-source. Use at your own risk.
