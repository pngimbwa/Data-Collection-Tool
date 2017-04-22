import string
import random
from .models import LabourManagament,SystemUser

def name():
    if register_number_choice == 'One':
        try:
            People.objects.get(personID=regone)
        except People.DoesNotExist:
            message ="UserID doesn't exist"
            return render(request,'signup/register.html',locals())
        else:
            if RelationManager.objects.filter(personA=personID,personB=regone).exists():
                message = 'relation already exist'
                return render(request,'signup/register.html',locals()) 
            relation = RelationManager(personA=personID,personB=regone,relation='Family')
            relation.save()                    
                   
    elif register_number_choice == 'Two':
        for ID in (regone,regtwo):
            try:
                People.objects.get(personID=ID)
            except People.DoesNotExist:
                message ="UserID {} doesn't exist".format(ID)
                return render(request,'signup/register.html',locals())
            else:
                if RelationManager.objects.filter(personA=personID,personB=ID).exists():
                    message = 'relation between {} and {} already exist'.format(personID,ID)
                    return render(request,'signup/register.html',locals()) 
                relation = RelationManager(personA=personID,personB=ID,relation='Family')
                relation.save()
                        
    elif register_number_choice == 'Three':
        for ID in (regone,regtwo,regthree):
            try:
                People.objects.get(personID=ID)
            except People.DoesNotExist:
                message ="UserID {} doesn't exist".format(ID)
                return render(request,'signup/register.html',locals())
            else:
                if RelationManager.objects.filter(personA=personID,personB=ID).exists():
                    message = 'relation between {} and {} already exist'.format(personID,ID)
                    return render(request,'signup/register.html',locals()) 
                relation = RelationManager(personA=personID,personB=ID,relation='Family')
                relation.save()
                        
    elif register_number_choice == 'Four':
        for ID in (regone,regtwo,regthree,regfour):
            try:
                People.objects.get(personID=ID)
            except People.DoesNotExist:
                message ="UserID {} doesn't exist".format(ID)
                return render(request,'signup/register.html',locals())
            else:
                if RelationManager.objects.filter(personA=personID,personB=ID).exists():
                    message = 'relation between {} and {} already exist'.format(personID,ID)
                    return render(request,'signup/register.html',locals()) 
                relation = RelationManager(personA=personID,personB=ID,relation='Family')
                relation.save()
                        
    elif register_number_choice == 'Five':
        for ID in (regone,regtwo,regthree,regfour,regfive):
            try:
                People.objects.get(personID=ID)
            except People.DoesNotExist:
                message ="UserID {} doesn't exist".format(ID)
                return render(request,'signup/register.html',locals())
            else:
                if RelationManager.objects.filter(personA=personID,personB=ID).exists():
                    message = 'relation between {} and {} already exist'.format(personID,ID)
                    return render(request,'signup/register.html',locals()) 
                relation = RelationManager(personA=personID,personB=ID,relation='Family')
                relation.save()

def personID_generator(country,table_list):
    if country == 'Ghana':initial ='GH-'
    elif country == 'Tanzania':initial ='TZ-'
    elif country == 'Ethiopia':initial ='ET-'
    chars=string.ascii_uppercase + string.digits
    myID =''.join(random.choice(chars) for _ in range(4))
    personID = initial + myID
    while personID in table_list:
        myID =''.join(random.choice(chars) for _ in range(4))
        personID = initial + myID
    else:
        personID = initial + myID
        generatedID = personID
    return generatedID

def pick_currency(user_instance):
    if user_instance.country.name == 'Tanzania': currency ='Tsh'
    elif user_instance.country.name == 'Ghana':currency ='Cedi'
    elif user_instance.country.name == 'Ethiopia':currency ='Birr'
    return currency


def DegreeConverter(degree,minutes,seconds,direction):
    
    dd = degree + minutes/60 + seconds/(60*60)
    print('direction: {}'.format(direction))
    if direction == 'South' or direction == 'West':
        dd = dd * -1
    return dd

def labourmanagement(activity,labour,plot_labourmanagament_instance,areadescription,systemuser,date,wage,**kwargs):
#hired_female_number,hired_female_time,hired_male_number,hired_male_time,family_female_number,family_female_time,family_male_number,family_male_time)
#family_female_number,family_female_time,family_male_number,family_male_time)
    print('activity:{}'.format(activity))
    if labour == 'Family':
        plot_labourmanagament_instance.date = date
        plot_labourmanagament_instance.family_female_time = kwargs['family_female_time']
        plot_labourmanagament_instance.family_male_time = kwargs['family_male_time']
        plot_labourmanagament_instance.areadescription = areadescription
        plot_labourmanagament_instance.labour = labour
        plot_labourmanagament_instance.family_female_number = kwargs['family_female_number']
        plot_labourmanagament_instance.family_male_number = kwargs['family_male_number']
        plot_labourmanagament_instance.activity = activity
        plot_labourmanagament_instance.wage = wage
        plot_labourmanagament_instance.hired_female_time = None               
        plot_labourmanagament_instance.hired_male_time = None
        plot_labourmanagament_instance.hired_female_number = None
        plot_labourmanagament_instance.hired_male_number = None
        plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=systemuser)
    elif labour == 'Hired':
        plot_labourmanagament_instance.date = date
        plot_labourmanagament_instance.family_female_time = None
        plot_labourmanagament_instance.family_male_time = None
        plot_labourmanagament_instance.family_female_number = None
        plot_labourmanagament_instance.family_male_number = None 
        plot_labourmanagament_instance.hired_female_time = kwargs['hired_female_time']               
        plot_labourmanagament_instance.hired_male_time = kwargs['hired_male_time']
        plot_labourmanagament_instance.areadescription = areadescription
        plot_labourmanagament_instance.labour = labour
        plot_labourmanagament_instance.hired_female_number = kwargs['hired_female_number']
        plot_labourmanagament_instance.hired_male_number = kwargs['hired_male_number']
        plot_labourmanagament_instance.activity = activity
        plot_labourmanagament_instance.wage = wage
        plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=systemuser)
    elif labour == 'FamilyHired':
        plot_labourmanagament_instance.date = date
        plot_labourmanagament_instance.family_female_time = kwargs['family_female_time']
        plot_labourmanagament_instance.family_male_time = kwargs['family_male_time']
        plot_labourmanagament_instance.areadescription = areadescription
        plot_labourmanagament_instance.labour = labour
        plot_labourmanagament_instance.family_female_number = kwargs['family_female_number']
        plot_labourmanagament_instance.family_male_number = kwargs['family_male_number']
        plot_labourmanagament_instance.hired_female_time = kwargs['hired_female_time']               
        plot_labourmanagament_instance.hired_male_time = kwargs['hired_male_time']
        plot_labourmanagament_instance.hired_female_number = kwargs['hired_female_number']
        plot_labourmanagament_instance.hired_male_number = kwargs['hired_male_number']
        plot_labourmanagament_instance.activity = activity
        plot_labourmanagament_instance.wage = wage
        plot_labourmanagament_instance.enteredpersonel = SystemUser.objects.get(user=systemuser)
    plot_labourmanagament_instance.save()
