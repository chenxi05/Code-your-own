import serialization as ser

trivia_questions = {
    "Which country consumes the most chocolate per capita? " : "Switzerland",
    "What is the only edible food that never goes bad? " : "Honey",
    "What is the name of the biggest technology company in South Korea? " : "Samsung",
    "Who was the first women to win a Nobel Prize in 1903? " : "Marie Curie",
    "Who was the first woman pilot to fly solo across the Atlantic? " : "Amelia Earhart",
    "How many hearts does an octopus have? " : "3"
}

print("Welcome to our trivia game!")
game = True

def playing():
    if not game:
        user_name=input("Please enter your username: ") 
        pts=0
    else:
        for i in trivia_questions.keys():
            answer = input(i) == trivia_questions[i]
            if answer:
                pts += 1
            else:
                continue
            print()
        score = ser.libel(user_name, pts)
        print(score)
    game = input("Enter U for a new user and G to play again: ").upper() == "G"