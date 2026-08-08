countries = {
    "Malaysia": "Kuala Lumpur",
    "France": "Paris",
    "USA": "Washington DC",
    "Germany": "Berlin",
    "Syria": "Damascus",
    "Iraq": "Baghdad",
    "UAE": "Abu Dhabi",
    "KSA": "Riyadh",
    "Russia": "Moscow",
    "India": "New Delhi",
    "Argentina": "Buenos Aires",
    "Portugal": "Lisbon",
    "UK": "London",
    "Spain": "Madrid",
    "Brazil": "Brasilia",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Australia": "Canberra",
    "New Zealand": "Wellington",
    "Japan": "Tokyo",
    "China": "Beijing",
    "South Korea": "Seoul",
    "North Korea": "Pyongyang",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi",
    "Indonesia": "Jakarta",
    "Philippines": "Manila",
    "Singapore": "Singapore",
    "Pakistan": "Islamabad",
    "Bangladesh": "Dhaka",
    "Nepal": "Kathmandu",
    "Afghanistan": "Kabul",
    "Iran": "Tehran",
    "Turkey": "Ankara",
    "Jordan": "Amman",
    "Lebanon": "Beirut",
    "Qatar": "Doha",
    "Kuwait": "Kuwait City",
    "Bahrain": "Manama",
    "Oman": "Muscat",
    "Italy": "Rome",
    "Greece": "Athens",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Poland": "Warsaw",
    "Ukraine": "Kyiv",
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen",
    "Ireland": "Dublin",
    "Iceland": "Reykjavik",
    "Egypt": "Cairo",
    "Morocco": "Rabat",
    "Algeria": "Algiers",
    "Tunisia": "Tunis",
    "Libya": "Tripoli",
    "South Africa": "Pretoria",
    "Kenya": "Nairobi",
    "Nigeria": "Abuja",
    "Ethiopia": "Addis Ababa",
    "Ghana": "Accra",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Chile": "Santiago",
    "Ecuador": "Quito",
    "Uruguay": "Montevideo",
    "Paraguay": "Asuncion",
    "Bolivia": "Sucre",
    "Venezuela": "Caracas",
    "Czech Republic": "Prague",
    "Hungary": "Budapest",
    "Romania": "Bucharest",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana"
}

print("Welcome to the Countries of the World!")

while True:
    print("\n==== MENU ====")
    print("1. Find the Capital of a Country")
    print("2. Add a Country and its Capital")
    print("3. Update a Country's Information")
    print("4. Remove a Country and its Capital")
    print("5. Display All Countries and their Capitals")
    print("6. Exit")

    choice1 = input("Enter your choice: ")

    # FIND CAPITAL
    if choice1 == "1":
        choice2 = input("\nEnter your country's name: ")

        if choice2 in countries:
            print("The capital of your country is:", countries[choice2])
        else:
            print("Country not found.")

    # ADD COUNTRY
    elif choice1 == "2":
        NewCountry = input("Enter the name of the new country: ")
        NewCapital = input("Enter the name of the new capital: ")

        countries[NewCountry] = NewCapital
        print("New country successfully added!")

    # UPDATE COUNTRY
    elif choice1 == "3":
        UpdCountry = input("What country's capital would you like to update? ")

        if UpdCountry in countries:
            UpdCapital = input("Please enter the new capital: ")
            countries[UpdCountry] = UpdCapital
            print("Country information successfully updated!")
        else:
            print("Country not found.")

    # DELETE COUNTRY
    elif choice1 == "4":
        delcountry = input("What country would you like to delete? ")

        if delcountry in countries:
            del countries[delcountry]
            print("Country deleted successfully!")
        else:
            print("Country not found.")

    # DISPLAY COUNTRIES
    elif choice1 == "5":
        print("\n==== COUNTRIES AND CAPITALS ====")

        for country, capital in countries.items():
            print(country, "->", capital)

    # EXIT
    elif choice1 == "6":
        print("Thanks for using the Countries of the World program!")
        break

    else:
        print("Invalid choice. Please choose 1-6.")