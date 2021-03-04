import json
import userandsuperuser
def make_question(teacher_number):
    if teacher_number in userandsuperuser.Super_User.total_college_teachers:
        print('Please proceed towards making new questions!!')
        with open('all_questions.json','w') as fo:
            content = []
            count = 1
            while True:
                choice = input('IF YOU ENTER 1, GO FORWARD TO MAKING MORE QUESTIONS, IF YOU ENTER 0 STOP MAKING QUESTIONS')
                if int(choice) == 1:    
                    print('Total questions are -> ',count)
                    dictionary = {}
                    dictionary['question'] = input('Enter the question.')
                    dictionary['options'] = []
                    dictionary['options'].append(input('Enter options A.'))
                    dictionary['options'].append(input('Enter options B.'))
                    dictionary['options'].append(input('Enter options C.'))
                    dictionary['options'].append(input('Enter options D.'))
                    dictionary['answer'] = input('Enter the solution.')
                    content.append(dictionary)
                    count +=1
                else:
                    print('Your total number of questions are -> ',count)
                    break
            json.dump(content,fo)
    else:
        print('YOU ARE NOT A MEMBER OF FACULTY, IF YOU ARE PLEASE ENTER CORRECT ROLL NUMBER.')
