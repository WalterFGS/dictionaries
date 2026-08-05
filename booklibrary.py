books = {
    "diary of a wimpy kid": "jeff kinney",
    "harry potter and the sorcerers stone": "jk rowling",
    "big nate": "peirce",
    "attack on titan volume 3": "isayama"
}

print("Welcome to the Digital Library!")

while True:
    print("\n===== MENU =====")
    print("1. View books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("\nAdmin Panel:")
    print("4. Add a book")
    print("5. Delete a book")
    print("6. Update a book's details")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nBooks Available:")
        for book, author in books.items():
            print(f"{book} - {author}")

    elif choice == "2":
        book = input("Enter the name of the book to borrow: ").lower()

        if book in books:
            print(f"You borrowed '{book}'. Enjoy reading!")
            del books[book]
        else:
            print("Sorry, that book is not available.")

    elif choice == "3":
        book = input("Enter the name of the book to return: ").lower()
        author = input("Enter the author's name: ").lower()

        books[book] = author
        print("Book returned successfully!")

    elif choice == "4":
        book = input("Enter the new book name: ").lower()
        author = input("Enter the author's name: ").lower()

        books[book] = author
        print("Book added successfully!")

    elif choice == "5":
        book = input("Enter the book to delete: ").lower()

        if book in books:
            del books[book]
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    elif choice == "6":
        book = input("Enter the book to update: ").lower()

        if book in books:
            new_author = input("Enter the new author's name: ").lower()
            books[book] = new_author
            print("Book details updated!")
        else:
            print("Book not found.")

    elif choice == "7":
        print("Thank you for using the Digital Library!")
        break

    else:
        print("Invalid choice. Please try again.")