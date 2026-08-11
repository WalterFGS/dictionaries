textbooks = {
    "Math": 150,
    "Physics": 180,
    "Chemistry": 170,
    "Biology": 160
}

while True:
    print("\n--- Textbook Store ---")
    print("1. Correct Physics price")
    print("2. Add 2 books")
    print("3. Find a book's cost")
    print("4. Show all books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        textbooks["Physics"] = 200
        print("Physics price has been changed to 200.")

    elif choice == "2":
        textbooks["English"] = 140
        textbooks["Computer Science"] = 220
        print("Two books have been added.")

    elif choice == "3":
        book = input("Enter the book name: ")

        if book in textbooks:
            print("The cost of", book, "is", textbooks[book])
        else:
            print("Book not found.")

    elif choice == "4":
        print("\nAll textbooks and their costs:")
        for book, cost in textbooks.items():
            print(book, ":", cost)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")