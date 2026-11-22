# books.py
import json
import os

def load_books():
    """Load books from books.json file. Returns an empty list if file doesn't exist."""
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Return an empty list if the file has not been created yet
        return []

def save_books(books_list):
    """Save the books list into books.json file."""
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)

def display_books(books_list):
    """Display the list of books with their index."""
    print("\n--- Your Books List ---")
    if not books_list:
        print("Your book list is empty!")
    else:
        for index, book in enumerate(books_list, start=1):
            print(f"{index}. {book}")
# Add this function at the end of books.py

def delete_book(books_list):
    """Delete a book from the list by its index."""
    display_books(books_list)
    if not books_list:
        return
    
    try:
        choice = int(input("Enter the number of the book you want to delete: "))
        if 1 <= choice <= len(books_list):
            removed_book = books_list.pop(choice - 1)
            save_books(books_list)
            print(f"'{removed_book}' has been successfully deleted.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")
