import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curiousweb.settings')
django.setup()

"""Import the models here to populate"""
from main_app.models import User



def create_nw():


if __name__ == '__main__':
    print('creating fake users...')

    create_fake_users()
    print('fake users creation complete.')
