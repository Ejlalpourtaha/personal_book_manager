# 📚 Personal Book Manager

A simple and secure command-line book management system built with Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## ✨ Features
- Add new books
- View all saved books
- Persistent storage with JSON
- Protected Admin Mode

## ⚙️ Requirements
- Python
- `python-dotenv`


## 📥 Installation
Install the required packages using `requirements.txt`:
```bash
pip install -r requirements.txt

```

## 📸 Demo
![Project Screenshot](photo_2026-10-28_15-42-55.jpg)

## Project Structure

Here is the file and folder structure of the Personal Book Manager project:

- `main.py`: The entry point of the application, handles user navigation and the main loop.
- `books.py`: Contains core book management functions (loading, saving, adding, displaying, and deleting books).
- `.gitignore`: Specifies files and folders that Git should ignore (like `.env`, `books.json`, and caches).
- `.env.example`: A template file showing the required environment variables.
- `requirements.txt`: Lists external Python package dependencies required by the project.
- `images/`: Directory containing project screenshots and visual demos.


## How It Works

1. **Initialization**: When you run `main.py`, the program loads any previously saved books from `books.json`. If the file is missing or empty, it starts with an empty list.
2. **Main Menu**: The user is presented with options to view books, add a new book, enter Admin Mode, or exit.
3. **Adding Books**: The user inputs the book title and author, which are then appended to the list and automatically saved to `books.json`.
4. **Displaying Books**: The app lists all saved books clearly in the terminal.
5. **Admin Mode**: Protected by an environment variable password from `.env`, allowing authorized users to delete specific books by their index number.


## Troubleshooting

### 1. FileNotFoundError
- **What it means:** Python cannot find the expected file (like `books.json`).
- **Why it happens:** The file hasn't been created yet because no books have been saved, or it was accidentally deleted.
- **What to check first:** Verify if you are running the script from the correct project directory and whether `books.json` is generated upon adding your first book.

### 2. JSONDecodeError
- **What it means:** The app failed to parse `books.json` because the file is empty or corrupted.
- **Why it happens:** The file was opened/saved incorrectly or left completely blank.
- **What to check first:** Open `books.json` and ensure it contains valid JSON structure (e.g., `[]` or a proper list of dictionaries).

### 3. Missing python-dotenv
- **What it means:** Python throws a `ModuleNotFoundError` for `dotenv`.
- **Why it happens:** The required dependencies have not been installed in your active Python environment.
- **What to check first:** Run `pip install -r requirements.txt` to install all necessary packages.

### 4. Password Not Read from .env
- **What it means:** Admin mode authentication fails even with the correct password.
- **Why it happens:** The `.env` file is missing, misnamed, or `load_dotenv()` was not called in `main.py`.
- **What to check first:** Make sure your file is named strictly `.env` (not `.env.txt`) and that `python-dotenv` is properly loaded before checking `os.getenv()`.


## 🌟 Features

- ➕ **Add Books:** Save book titles, authors, and priority levels effortlessly.
- 📖 **View Collection:** Display all saved books in a clean, formatted list.
- 🔒 **Admin Mode:** Securely delete books with a password protected by environment variables (`.env`).
- ⚡ **Priority Tracking:** Categorize books into `low`, `medium`, and `high` priority levels.
- 💾 **Persistent Storage:** Automatically saves and loads your collection from a local `books.json` file.

---

## 🎯 Book Priority System

| Priority Level | Description | Use Case |
| :--- | :--- | :--- |
| 🟢 **Low** | Casual or deferred reading | Books you might read later |
| 🟡 **Medium** *(Default)* | Standard reading queue | Regular books on your list |
| 🔴 **High** | Urgent or high-priority | Books you want to read right now |

---

## 🗂️ Project Structure
```text
personal_book_manager/
│
├── 📜 main.py             # Entry point (handles menus & Admin Mode)
├── 📦 books.py            # Core logic (load, save, add, display, delete)
├── 📄 books.json          # Local database (git-ignored)
├── 🔒 .env                # Secret environment variables (git-ignored)
├── 📋 .env.example        # Template for environment variables
├── 📌 requirements.txt    # Project dependencies
├── 🪵 app.log             # Application logs (git-ignored)
├── ⚠️ error.log           # Error logs (git-ignored)
├── 📖 README.md           # Project documentation
└── 🖼️ images/
└── 📷 screenshot.png  # Application screenshot or demo
