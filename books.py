import json

def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books_list):
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)

def add_book(books_list):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    
    # گرفتن priority با اعتبارسنجی ساده
    priority = input("Enter book priority (low, medium, high): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        print("Invalid priority! Defaulting to 'medium'.")
        priority = "medium"
    
    books_list.append({
        "title": title,
        "author": author,
        "priority": priority
    })
    save_books(books_list)
    print("Book added successfully with priority!")

def display_books(books_list):
    if not books_list:
        print("No books found.")
        return
    
    for i, book in enumerate(books_list, 1):
        print(f"{i}. Title: {book['title']} | Author: {book['author']} | Priority: {book.get('priority', 'medium').capitalize()}")

def delete_book(books_list):
    display_books(books_list)
    if not books_list:
        return
    
    try:
        choice = int(input("Enter book number to delete: "))
        removed = books_list.pop(choice - 1)
        save_books(books_list)
        print(f"Book '{removed['title']}' deleted!")
    except (ValueError, IndexError):
        print("Invalid number.")
