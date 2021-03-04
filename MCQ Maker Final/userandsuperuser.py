class User:
    total_users = []
    def __init__(self, username, college_rollno, mobile_no, course_name):
        self.username = username
        self.college_rollno = college_rollno
        self.mobile_no = mobile_no
        self.course_name = course_name
        User.total_users.append({'Name':self.username,'Roll Number':self.college_rollno})
        print('Your details have currently been saved. Proceed towards your test.')

class Super_User:
    # these are the college roll number of teachers that can make test for the student
    total_college_teachers = ['1234AKA','256PAL','258MON','545ANI']
    def __init__(self, Username, College_rollno, Mobile_no):
        self.Username = Username
        self.College_rollno = College_rollno
        self.Mobile_no = Mobile_no
        if self.College_rollno in Super_User.total_college_teachers:
            print("Good Morning, Dear Sir/Dear Ma'am")