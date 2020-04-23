import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curiousweb.settings')
django.setup()

"""Import the models here to populate"""
from first_app.models import Topic, SubTopic, Question

"""Import Faker if needed"""
#from faker import Faker

TOPICS = [
    'Mathematics',
    'General Engineering and Applied Sciences / Engineering Sciences and Allied Subjects',
    'Electrical Engineering',
    'Electronics Engineering',
    'Electronics Systems and Technologies',
]



def create_topics():


if __name__ == '__main__':
    print('creating fake users...')

    create_fake_users()
    print('fake users creation complete.')
