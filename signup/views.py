from django.shortcuts import render, render_to_response, get_object_or_404,redirect,RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.contrib.auth.models import User

from signup.forms import PeopleForm,LocationForm,registerUserForm,LoginForm,HouseForm

from iwmiproject.models import Country,Farm, Crop, People, Village,RelationManager,House,PumpingSource,SystemUser,TechnologyManagement,FarmGroup,Technology

from iwmiproject.functions import personID_generator

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    if request.method =='POST':
        #form = LoginForm(request.POST)
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            remember_me=form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    #if not self.cleaned_data.get('remember_me'):
                        #self.request.session.set_expiry(0)
                    if not remember_me:
                        request.session.set_expiry(0)
                    return render(request,'home.html',locals()) 
                else:
                    message = "This account is inactive."
                    return render(request,'signup/login.html',locals())
            else:
                message="user doesn't exist"
                return render(request,'signup/login.html',locals())
                #return HttpResponseRedirect('/login/')
        else:
            message="wrong username/password or user doesn't exist"
            #message = 'wrong password or username'
            return render(request,'signup/login.html',locals())

    else:
        #user is not subitting the form shows the login form
        form=LoginForm()
        return render(request,'signup/login.html',locals())

def LogoutRequest(request):
    logout(request)
    return redirect('signup:login')


def home(request):
    if request.user.is_authenticated():

        return render(request,'home.html',locals()) 
    else:
        return HttpResponseRedirect(reverse('signup:login'))


def copyright(request): 
    if request.user.is_authenticated():
        return render(request,'copyright.html',locals()) 
    else:
        return HttpResponseRedirect(reverse('signup:login'))
    
def help(request):
    if request.user.is_authenticated():
        return render(request,'signup/help.html',locals()) 
    else:
        return HttpResponseRedirect(reverse('signup:login'))
    
    

def register(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
    
    if request.method == 'POST': 
        locationform = LocationForm(request.POST)
        peopleform = PeopleForm(request.POST)
        houseform = HouseForm(request.POST)
        
        print('*****aaaaa*****')
        if locationform.is_valid()  and peopleform.is_valid() and houseform.is_valid():
            
            register_select = peopleform.cleaned_data['register_select']
            group = peopleform.cleaned_data['group']
            #personID = peopleform.cleaned_data['personID']
            firstname = peopleform.cleaned_data['firstname']
            middlename = peopleform.cleaned_data['middlename']
            lastname = peopleform.cleaned_data['lastname']
            gender = peopleform.cleaned_data['gender']
            phone = peopleform.cleaned_data['phone']
            role = peopleform.cleaned_data['role']
            age_group = peopleform.cleaned_data['age_group']
            groupchoice = peopleform.cleaned_data['groupchoice']
            
            #number_of_plots = peopleform.cleaned_data['number_of_plots']
            #total_land_holding = peopleform.cleaned_data['total_land_holding']
            #total_irrigated_plots_land =  peopleform.cleaned_data['total_irrigated_plots_land']
            #total_irrigated_plots =  peopleform.cleaned_data['total_irrigated_plots']
            
            number_of_plots = peopleform.cleaned_data['number_of_plots']
            landownership = peopleform.cleaned_data['landownership']
            rented_land = peopleform.cleaned_data['rented_land']
            owned_land = peopleform.cleaned_data['owned_land']
            total_irrigated_owned_land = peopleform.cleaned_data['total_irrigated_owned_land']
            total_irrigated_rented_land = peopleform.cleaned_data['total_irrigated_rented_land']
            irrigated_plots = peopleform.cleaned_data['irrigated_plots']

            water_source = peopleform.cleaned_data['water_source']
            pumping_source = peopleform.cleaned_data['pumping_source']
            technology = peopleform.cleaned_data['technology']
            technology_date = peopleform.cleaned_data['technology_date']
            
            well_latitude_degree = peopleform.cleaned_data['well_latitude_degree']
            well_latitude_minutes = peopleform.cleaned_data['well_latitude_minutes']
            well_latitude_seconds = peopleform.cleaned_data['well_latitude_seconds']
            well_latitude_direction = peopleform.cleaned_data['well_latitude_direction']
            
            well_longitude_degree = peopleform.cleaned_data['well_longitude_degree']
            well_longitude_minutes = peopleform.cleaned_data['well_longitude_minutes']
            well_longitude_seconds = peopleform.cleaned_data['well_longitude_seconds']
            well_longitude_direction = peopleform.cleaned_data['well_longitude_direction']
            
            elevation = peopleform.cleaned_data['elevation']
            well_depth = peopleform.cleaned_data['well_depth']
            well_diameter = peopleform.cleaned_data['well_diameter']
            country = locationform.cleaned_data['country']
            region = locationform.cleaned_data['region']
            district = locationform.cleaned_data['district']
            village = locationform.cleaned_data['village']
            
            house_latitude_degree = houseform.cleaned_data['house_latitude_degree']
            house_latitude_minute = houseform.cleaned_data['house_latitude_minute']
            house_latitude_second = houseform.cleaned_data['house_latitude_second']
            house_latitude_direction = houseform.cleaned_data['house_latitude_direction']
            
            house_longitude_degree = houseform.cleaned_data['house_longitude_degree']
            house_longitude_minute = houseform.cleaned_data['house_longitude_minute']
            house_longitude_second = houseform.cleaned_data['house_longitude_second']
            house_longitude_direction = houseform.cleaned_data['house_longitude_direction']
            
            household_members = peopleform.cleaned_data['household_members']
            House_elevation= houseform.cleaned_data['House_elevation']

            country_object = Country.objects.get(name=country).name
            personID_list = [i.personID for i in People.objects.all()]
            personID = personID_generator(country_object,personID_list)
         
            well_latitude = DegreeConverter(well_latitude_degree,well_latitude_minutes,well_latitude_seconds,well_latitude_direction)
            well_longitude = DegreeConverter(well_longitude_degree,well_longitude_minutes,well_longitude_seconds,well_longitude_direction)
            house_longitude = DegreeConverter(house_longitude_degree,house_longitude_minute,house_longitude_second,house_longitude_direction)
            house_latitude = DegreeConverter(house_latitude_degree,house_latitude_minute,house_latitude_second,house_latitude_direction)
            
            print('qqqqqqqqqqq')
            print('technology: {}'.format(technology))
            if str(technology) == 'No technology':
                print('44444')
                technology_date = None
            if not phone:phone = 'N/A'

            if register_select =='Yes':
                try:
                    RelationManager.objects.get(farmer=personID)
                except RelationManager.DoesNotExist:
                    relation_instance = RelationManager(farmer=personID)
                    relation_instance.save()
                else:
                    relation_instance = RelationManager.objects.get(farmer=personID)
                finally:
                    for i in household_members: 
                        relation_instance.family_member.add(i)

            try:
                People.objects.get(personID=personID)
            except People.DoesNotExist:
                if groupchoice == 'Yes':
                    try:
                        FarmGroup.objects.get(name=group)
                    except FarmGroup.DoesNotExist:
                        group_instance = FarmGroup(name=group,village=Village.objects.get(village=village))
                        group_instance.save()
                    finally:
                        group_instance = FarmGroup.objects.get(name=group)
                        people_instance = People(personID=personID,firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,role=role,group=group_instance,village=Village.objects.get(village=village),phone=phone,age_group=age_group)
                else:
                    group_instance = 'N/A'
                    people_instance = People(personID=personID,firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,role=role,village=Village.objects.get(village=village),phone=phone,age_group=age_group)
                people_instance.save()
            else:
                message ='UserID already exist'
                return render(request,'signup/register.html',locals())
            
            '''
            Save house detail for a farmer
            '''
            house_instance = House(latitude=house_latitude,longitude=house_longitude,elevation=House_elevation,owner=People.objects.get(personID=personID))
            house_instance.save()
        
            '''
            farm detail for a farmer
            '''
            if landownership == 'All owned':
                total_irrigated_rented_land = 0
                fieldsize = owned_land
                rented_land = 0
                farm_instance =  Farm(farmID=people_instance,number=number_of_plots,fieldsize=fieldsize,landownership=landownership,rented_land=rented_land,owned_land=owned_land,total_irrigated_owned_land=total_irrigated_owned_land,total_irrigated_rented_land=total_irrigated_rented_land,irrigated_plots=irrigated_plots,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif landownership == 'Partly owned':
                fieldsize = owned_land  + rented_land
                farm_instance =  Farm(farmID=people_instance,number=number_of_plots,fieldsize=fieldsize,landownership=landownership,rented_land=rented_land,owned_land=owned_land,total_irrigated_owned_land=total_irrigated_owned_land,total_irrigated_rented_land=total_irrigated_rented_land,irrigated_plots=irrigated_plots,enteredpersonel=SystemUser.objects.get(user=request.user))
            elif landownership == 'All rented':
                total_irrigated_owned_land = 0
                fieldsize = rented_land
                owned_land =0
                farm_instance =  Farm(farmID=people_instance,number=number_of_plots,fieldsize=fieldsize,landownership=landownership,rented_land=rented_land,owned_land=owned_land,total_irrigated_owned_land=total_irrigated_owned_land,total_irrigated_rented_land=total_irrigated_rented_land,irrigated_plots=irrigated_plots,enteredpersonel=SystemUser.objects.get(user=request.user))
            farm_instance.save()
        
            '''
            Pumping source for a farmer
            '''
            if pumping_source == 'Well':
                pumpingSource_instance = PumpingSource(date=technology_date,farm=farm_instance,source=pumping_source,latitude=well_latitude,longitude=well_longitude,elevation=elevation,depth=well_depth,diameter=well_diameter)
            else:
                pumpingSource_instance = PumpingSource(date=technology_date,farm=farm_instance,source=pumping_source,latitude=well_latitude,longitude=well_longitude)
            pumpingSource_instance.save()
            
            '''
            technology management for a farmer
            '''
            technologyManagement_instance = TechnologyManagement(farm=farm_instance,date=technology_date,technology=Technology.objects.get(name=technology))
            technologyManagement_instance.save()
            
            message="Farmer with ID:'{}' successfully saved..!".format(personID)
            context = {'message':message}
            return render_to_response('iwmiproject/saved.html',context,context_instance=RequestContext(request))
        
        else:
            context = {'locationform':locationform,
                       'peopleform':peopleform,
                       'houseform':houseform
                       }
            return render_to_response('signup/register.html',context,context_instance=RequestContext(request))
    else:
        locationform = LocationForm()
        peopleform = PeopleForm()
        houseform = HouseForm()
        return render(request,'signup/register.html',locals()) 



def registeruser(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('signup:login'))
    
    if request.method == 'POST': 
        locationform = LocationForm(request.POST)
        registeruserform = registerUserForm(request.POST) 
        print('***********')
        if registeruserform.is_valid() and locationform.is_valid():

            country = registeruserform.cleaned_data['country']
            region = locationform.cleaned_data['region']
            district = locationform.cleaned_data['district']
            village = locationform.cleaned_data['village']
            email = registeruserform.cleaned_data['email']
            username = registeruserform.cleaned_data['username']
            firstname = registeruserform.cleaned_data['firstname']
            middlename = registeruserform.cleaned_data['middlename']
            lastname = registeruserform.cleaned_data['lastname']
            gender = registeruserform.cleaned_data['gender']
            phone = registeruserform.cleaned_data['phone']
            role = registeruserform.cleaned_data['role']
            institution = registeruserform.cleaned_data['institution']
            
            print('*****aaa******')
            password = '1234abc'
            
            try:
                User.objects.get(username=username)
            except User.DoesNotExist: 
                user = User.objects.create_user(username=username,email=email,password=password)
                if role == 'ST' or role == 'RA':
                    #print('ST&&RA')
                    user.is_active=True
                    #user.user_permissions.remove('iwmiproject.add_image')
                elif role =='RS':
                    #print('RS')
                    user.is_active=True
                    user.is_staff=True
                    #user.user_permissions.remove('iwmiproject.add_image')
                #elif role=='Image':
                    #print('image')
                    #user.user_permissions.add('iwmiproject.image')
                user.save()                
            else:
                message ='UserID already exist'
                return render(request,'signup/registeruser.html',locals())
            
            if role == 'ST' or role == 'RA':
                registeruser =SystemUser(user=user,firstname=firstname,middlename=middlename,lastname=lastname,
                            role=role,phone=phone,gender = gender,institution=institution,village=village,country=country)
            else:
                registeruser =SystemUser(user=user,firstname=firstname,middlename=middlename,lastname=lastname,
                            role=role,phone=phone,gender = gender,institution=institution,country=country)
            registeruser.save()

                
            #send email with activation key
            email_subject = 'Account creation confirmation'
            email_body = "Hi {} {};\n\nYour account have been created. Your username is '{}' and login password is '1234abc', please change the password soon you login.\n\nYou can login to the system using the link: http://transectz.webfactional.com/signup/login/ . \n\nRegards;\nAdmin.".format(firstname,lastname,username)
                            
            send_mail(email_subject,email_body,'pngimbwa6@gmail.com',[email],fail_silently=False)
            message='Account successfully created..!'
            context = {'message':message}
            return render_to_response('iwmiproject/saved.html',context,context_instance=RequestContext(request))

        
        else:
            context = {'locationform':locationform,
                       'registeruserform':registeruserform
                       }
            return render_to_response('signup/registeruser.html',context,context_instance=RequestContext(request))
    else:
        locationform = LocationForm()
        registeruserform = registerUserForm() 
        return render(request,'signup/registeruser.html',locals()) 


def index(request):
    return render(request,'index.html',locals()) 



def DegreeConverter(degree,minutes,seconds,direction):
	dd = degree + minutes/60 + seconds/(60*60)

	if direction == 'South' or direction == 'West':
		dd = dd * -1
	return dd

'''
def register(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    
    if request.method == 'POST':  
        country = request.POST.get('country')
        region = request.POST.get('region')
        district = request.POST.get('district')
        village = request.POST.get('village')
        personID = request.POST.get('personID')
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        
        instance = People(personID=personID,firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,role=role)
       
        try:
            People.objects.get(personID=personID)
            message ='UserID already exist'
            return render(request,'signup/register.html',locals())
        except People.DoesNotExist:
            village_instance = Village.objects.get(village=village)
            instance.village = village_instance
            instance.save()
        
    countries = Country.objects.all().order_by('name')
    categories = CropVariety.objects.all().order_by('category')
    return render(request,'signup/register.html',locals()) 
'''
