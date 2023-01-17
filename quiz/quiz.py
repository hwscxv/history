import json

points = 0

def show_questions(question):
    
    global points
    print()
    print(question["pytanie"])
    print('a', question["a"])
    print('b', question["b"])
    print('c', question["c"])
    print('d', question["d"])

    answer = input('podaj odpowiedz ')

    if answer == question["prawidlowa_odpowiedz"]:
        print('poprawna opowiedz')
        points += 1
        print('posiadasz '+ str(points) + ' punktow.')
    else:
        print('niepoprawna odpowiedz')

with open("quiz.json") as f:
    questions = json.load(f)

for i in range(0, len(questions)):
    show_questions(questions[i])
    