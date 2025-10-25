#dictionary pf european countries and its capitals
quiz= {
       "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Switzerland": "Bern",
    "Greece": "Athens"
   }
score=0
for country, capital in quiz.items():
    answer = input("What is the capital of {country}? ").strip().lower()
    
    # Using if, elif, else
    if answer == capital.lower():
        print(" Correct!")
        score += 1
    elif answer == "london":  # Example: a common wrong answer
        print(" Nope, London is the capital of the UK!")
    else:
        print(" Wrong! The correct answer is {capital}.")
