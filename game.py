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
num_of_players=int(input("How many people are playing this game?"))


for i in num_of_players:
    user_name=input("Please enter your username: ") 
    pts=0
    question1=input(trivia_questions.keys[0])
    if question1==trivia_questions[trivia_questions.keys[0]]:
        pts+=1
    question2=input(trivia_questions.keys[1])
    if question2==trivia_questions[trivia_questions.keys[1]]:
        pts+=1
    question3=input(trivia_questions.keys[2])
    if question3==trivia_questions[trivia_questions.keys[2]]:
        pts+=1
    question4=input(trivia_questions.keys[3])
    if question4==trivia_questions[trivia_questions.keys[3]]:
        pts+=1
    question5=input(trivia_questions.keys[4])
    if question5==trivia_questions[trivia_questions.keys[4]]:
        pts+=1
    question6=input(trivia_questions.keys[5])
    if question6==trivia_questions[trivia_questions.keys[5]]:
        pts+=1
    ser.save(user_name, pts)
    