import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','subbajobproject.settings')
import django
django.setup()

from testapp.models import Hydjobs,Bangjobs,Chennaijobs,Punejobs
from faker import Faker
from random import *
fake=Faker()

def phonenumgen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Enginner'))
        feligible=fake.random_element(elements=('B.Tech','M.Tech','MCA','Ph.D'))
        faddress=fake.address()
        femail=fake.email()
        fphonenum=phonenumgen()
        hydjobs_record=Hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eiligibility=feligible,address=faddress,email=femail,phonenumber=fphonenum)
        bangjobs_record = Bangjobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,eiligibility=feligible, address=faddress, email=femail,phonenumber=fphonenum)
        chennaijobs_record = Chennaijobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,eiligibility=feligible, address=faddress, email=femail,phonenumber=fphonenum)
        punejobs_record = Punejobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,eiligibility=feligible, address=faddress, email=femail,phonenumber=fphonenum)


populate(25)