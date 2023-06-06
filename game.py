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
game = input("Enter U for a new user and G to play again: ").upper() == "G"
print()
playing = True


USER_FILE = "user_info.pkl"
user_info = ser.load(USER_FILE)
if user_info is None:
    user_info = {}

while playing:
    while not game:
        user_name=input("Please enter your username: ").capitalize()
        if user_name  in user_info:
            print ("Welcome back,", user_name)
            print ("The last time you played, you got", user_info[user_name])
        pts=0
        game = True
    while game:
        for i in trivia_questions.keys():
            answer = input(i).capitalize() == trivia_questions[i]
            if answer:
                pts += 1
            print()
        print(pts)
        user_info[user_name] = pts
        ser.save(user_info, USER_FILE)
        game = False
    playing = input("Would you like to play again? Enter Y or N: ").upper() == "Y"
    if not playing:
        break
    game = input("Enter U for a new user, G to play again: ").upper() == "G"

print()
print("Thank you for playing!\n")
user_info = ser.load(USER_FILE)
for i in user_info.keys():
    print("SCORES:")
    print(i +" : " + user_info[i])
