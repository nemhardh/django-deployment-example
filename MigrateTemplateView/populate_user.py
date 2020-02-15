import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MigrateTemplateView.settings')

import django

django.setup()

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populateUser(N=5):
    for createduser in range(N):
        #Create Users
        fake_first = fakegen.first_name()
        fake_last =  fakegen.last_name()
        fake_email = fakegen.free_email_domain()
        #Add to users
        adduser = User.objects.get_or_create(first_Name = fake_first,last_Name= fake_last,user_email=fake_email)[0]

if __name__ == '__main__':
    print('Populating User')
    populateUser(10)
    print('Populating Done')
