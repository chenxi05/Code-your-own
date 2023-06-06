import serialization as ser

trivia_questions = {
    "Which country consumes the most chocolate per capita? " : "Switzerland",
    "What is the only edible food that never goes bad? " : "Honey",
    "What is the name of the biggest technology company in South Korea? " : "Samsung",
    "Who was the first women to win a Nobel Prize in 1903? " : "Marie Curie",
    "Who was the first woman pilot to fly solo across the Atlantic? " : "Amelia Earhart",
    "How many hearts does an octopus have? " : "3"
}

dictionary = {}

print("Welcome to our trivia game!")
game = input("Enter U for a new user and G to play again: ").upper() == "G"
playing = True

while playing:
    while not game:
        user_name=input("Please enter your username: ") 
        pts=0
        game = True
    while game:
        for i in trivia_questions.keys():
            answer = input(i).capitalize() == trivia_questions[i]
            if answer:
                pts += 1
            print()
        print(pts)
        dictionary[user_name] = pts
        print(dictionary)
        game = False
    game = input("Enter U for a new user and G to play again: ").upper() == "G"

        