import serialization as ser



trivia_questions = {
    "Which country consumes the most chocolate per capita?" : "Switzerland",
    "What is the only edible food that never goes bad?" : "Honey",
    "What is the name of the biggest technology company in South Korea?" : "Samsung",
    "Who was the first women to win a Nobel Prize in 1903?" : "Marie Curie",
    "Who was the first woman pilot to fly solo across the Atlantic?" : "Amelia Earhart",
    "How many hearts does an octopus have?" : "3"
}

print("Welcome to our trivia game!")

user_name=input("Please enter your username: ") 
pts=0
for i in range(len(trivia_questions)):
    print(trivia_questions.keys[i])
#     if answer:
#        pts += 1
    #   else:
    #      continue

    