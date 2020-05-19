import os
import django
from faker import Faker
import random
fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curiousweb.settings')
django.setup()

"""Import the models here to populate"""
from exams_app.models import MCQ, ExamTicket
from main_app.models import User
from django.contrib.auth.hashers import make_password


def create_random_mcqs(n = 100):
    mcqs = []
    for i in range(n):
        correct_pattern = [True, False, False, False]
        random.shuffle(correct_pattern)

        new_mcq = MCQ(
            question = fake.paragraph(),
            choice1 = fake.sentence(),
            choice2 = fake.sentence(),
            choice3 = fake.sentence(),
            choice4 = fake.sentence(),
            correct1 = correct_pattern[0],
            correct2 = correct_pattern[1],
            correct3 = correct_pattern[2],
            correct4 = correct_pattern[3],
        )
        mcqs.append(new_mcq)

    many_mcqs = MCQ.objects.bulk_create(mcqs)

def set_user_flags(username):
    superuser = User.objects.get(username = username)
    superuser.is_teacher = True
    superuser.is_ece = True
    superuser.is_ee = True
    superuser.is_tutorial = True
    superuser.is_premium = True
    superuser.is_student = True
    superuser.is_enrolled = True
    superuser.save()

def create_test_superuser():
    superuser = User(
        username = 'leslietutorial',
        password = make_password('testpassword'),
        is_teacher = False,
        is_ece = False,
        is_ee = False,
        is_tutorial = True,
        is_premium = False,
        is_student = True,
        is_enrolled = True,
        )
    superuser.save()

def check_user():
    user = User.objects.get(
        username = 'glenn'
    )
    print('username', user.username)
    print('is_ece', user.is_ece)
    print('is_ee', user.is_ee)
    print('is_tutorial', user.is_tutorial)
    print('is_teacher', user.is_teacher)

def delete_examtickets():
    tickets = ExamTicket.objects.all()
    for ticket in tickets:
        ticket.delete()

if __name__ == '__main__':
    print('running populate.py...')
    print()
    set_user_flags('jiovanni')
    set_user_flags('mariadeborah')
    set_user_flags('glennpaul')
    set_user_flags('leslie')
    print('done.')
