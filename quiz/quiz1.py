import json
points = 0

def show_questions(question):
    global points
    print()
    print(question["pytanie"])
    print('a:', question["a"])
    print('b:', question["b"])
    print('c:', question["c"])
    print('d:', question["d"])
    print()

    answer = input('podaj odpowiedz')

    if answer == questions[i]["prawidlowa_odpowiedz"]:
        points += 1
        print('poprawna odpowiedz')
        print('posiadasz', points, 'puntkow')
    else:
        print('niepoprawna odpowiedz')
        





with open("quiz.json") as f:
    questions = json.load(f)

for i in range(0, len(questions)):
    show_questions(questions[i])