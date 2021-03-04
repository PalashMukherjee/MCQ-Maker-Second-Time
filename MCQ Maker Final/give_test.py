import json
import time
import make_questions
import take_test
import userandsuperuser
if __name__ == '__main__':
    while True:
        time.sleep(2)
        print('YOU HAVE THE FOLLOWING CHOICES !!!')
        print('choice 1. ->  make questions for the test')
        print('choice 2. ->  take the test')
        print('choice 3. ->  give your informations as a student')
        print('choice 4. ->  give your information as a faculty member')
        print('choice 5. ->  part of the faculty and want to check the marks of a given student')
        print('choice 6. ->  if you want to check the information of all the students')
        print('choice 7. ->  GOODBYE!! ')
        time.sleep(1)
        choice = input('Which one of the choices you want to follow?  ')
        time.sleep(1)
        if int(choice) == 1:
            make_questions.make_question(input('Please enter your college roll number! '))
        elif int(choice) == 2:
            take_test.MCQ(input('Please enter your student roll number '))
        elif int(choice) == 3:
            userandsuperuser.User(input('enter your name  '), input('enter your roll number  '), input('enter your mobile number  '),input('enter your course name'))
        elif int(choice) == 4:
            userandsuperuser.Super_User(input('enter you name  '),input('enter your college roll number  '),input('enter your mobile number  '))
        elif int(choice) == 5:
            spl_number = input("if you're a faculty member then please continue and give you college number  ")
            if spl_number in userandsuperuser.Super_User.total_college_teachers:
                with open('marksperstudent.json',encoding='utf-8') as fp:
                    content = json.load(fp)
                    for i in content:
                        print(i)
            else:
                print('You are not allowed to see anything')
        elif int(choice) == 6:
            teacher_num = input("if you're a faculty member then please continue and give you college number  ")
            if teacher_num in userandsuperuser.Super_User.total_college_teachers:
                for a in userandsuperuser.User.total_users:
                    print(a)
        elif int(choice) == 7:
            print('Goodbye !!!! ')
            break
        else:
            print('please enter a valid choice')