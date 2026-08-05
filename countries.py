countries = {"Malaysia": "Kuala Lumpur", "France": "Paris", "USA": "Washingtion DC", "Germany": "Berlin", "Syria": "Damascus", "Iraq": "Baghdad", "UAE": "Abu Dhabi", "KSA": "Riyadh", "Russia": "Moscow", "India": "Delhi", "Argentina": "Buneos Aries", "Portugal": "Lisbon", "UK": "London", "Spain": "Madrid", "Brazil": "Sao Paulo"}

print("Welcome to the Countries of the World!")

while True:
    print("\n ====MENU====")
    print("1. Find the Capital of a Country")
    print("2. Add a Country and it's Capital")
    print("3. Update a Country' Information")
    print("4. Remove a Country and it's Capital")
    print("5. Display All Countries and their Capitals")
    choice1 = input("Enter your choice: ")

    if choice1 == "1":
        print("\n Enter your Countries name:"),
        choice2 = input("")
        print("The Capital of your Country is :", countries[choice2])

    elif choice1 == "2":
        NewCountry = input("Enter the name of the New Country : ")    
        NewCapital = input("Enter the name of the New Capital : ")

        countries[NewCountry] = NewCapital
        print("New Country Successfully Added!")

    elif choice1 == "3":
        UpdCountry = input("What Country' Capital Would you like to Update: ")
        if UpdCountry in countries:
            UpdCapital = input("Please Enter the new Capital for ")
            print(UpdCountry)
            countries[UpdCountry] = UpdCapital

    elif choice1 == "4":
        delcountry = input("What Country would you like to Delete: ")
        if delcountry in countries:

            del countries[delcountry]
            print("Country deleted successfully!")
        else:
            print("Country not found.")

    elif choice2 == "5":

