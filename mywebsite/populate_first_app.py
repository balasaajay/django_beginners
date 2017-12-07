import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()


from first_app.models import User
from faker import Faker
fakegen=Faker()

def populate(N):
    for i in range(N):
        fake_lname=fakegen.last_name()
        fake_fname=fakegen.first_name()
        fake_email=fakegen.ascii_free_email()
        u = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, emailid=fake_email)[0]

if __name__=='__main__':
    print ("Poping script")
    populate(20)
