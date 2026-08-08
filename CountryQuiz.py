import random 
score = 0
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
    "South Africa": "Cape Town",
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

questions = random.sample(list(countries.items()), 10) # randomly pick 10 countries 

for i,j in questions: 
    answer = input(f"Whats the capital of {i}: ")
    if answer == j: 
        print("You got it right! + 10 points")
        score += 10
        print("Your score is : ", score)
    else:
        print("You got it wrong. -5 points")
        score -= 5
        print(f"The capital of {i}, is {j}")
        print("Your score is :", score)

print("Your final score is :", score)