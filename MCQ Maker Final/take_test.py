import json
import make_questions
def MCQ(college_rollno):
    all_answers = []
    with open('all_questions.json',encoding='utf-8') as fo:
        content = json.load(fo)
        for j in range(len(content)):
            alpha = 96
            print(content[j]['question'])
            for opt in content[j]['options']:
                alpha +=1
                print(chr(alpha)+')',opt)
            solution = input('Enter your solution. -> ')
            if solution == content[j]['answer']:
                all_answers.append(True)
                print(True)
            else:
                all_answers.append(False)
                print(False)

        score = str(len([i for i in all_answers if i == True])) + '/' + str(len(all_answers))
    # making a json file to add all the marks to the file
    with open('marksperstudent.json',encoding='utf-8') as fo:
        content = json.load(fo)
        dictionary = {}
        dictionary[college_rollno] = score
    content.append(dictionary)
    with open('marksperstudent.json','w',encoding='utf-8') as fp:
        json.dump(content,fp)