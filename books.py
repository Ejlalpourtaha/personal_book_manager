import json

def load_books():
    """Load books from books.json file, returning an empty list if file is missing or corrupted."""
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books_list):
    """Save the current list of books to books.json with indentation."""
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)

def add_book(books_list):
    """Add a new book with title, author, and priority to the collection."""
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    
    # Getting priority with validation
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
    """Display all books in a neat and readable format."""
    if not books_list:
        print("No books found.")
        return
    
    print("\n=== YOUR BOOK COLLECTION ===")
    for i, book in enumerate(books_list, 1):
        print(f"[{i}] {book['title']} - Author: {book['author']} (Priority: {book.get('priority', 'medium').upper()})")
    print("=" * 27)

def delete_book(books_list):
    """Delete a book from the collection by its index number."""
    display_books(books_list)
    if not books_list:
        return
    
    try:
        choice = int(input("Enter book number to delete: "))
        removed = books_list.pop(choice - 1)
        save_books(books_list)
        print(f"Book '{removed['title']}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid book number. Please try again.")
