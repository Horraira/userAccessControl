from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from .models import Patient, Doctor, Pharmacy
from .decorators import unauthenticated_user, allowed_users, user_only, patient_only, pharmacy_only
# from .models import user


# Create your views here.
@patient_only
@allowed_users(allowed_roles=['patient'])
def home(request):
    return render(request,'home.html')

@user_only
def doctor_home(request):
    return render(request,'doctor_home.html')

@pharmacy_only
@allowed_users(allowed_roles=['pharmacy'])
def pharmacy_home(request):
    return render(request,'pharmacy_home.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        reg_user = auth.authenticate(username=username,email=email,password=password)

        if reg_user is not None:
            auth.login(request, reg_user)
            return redirect(home)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nid = request.POST['nid']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        address = request.POST['address']
        contact = request.POST['contact']
        bdate = request.POST['date']
        
        patient = Patient(first_name=firstname, last_name=lastname, nid=nid, email=email, password=password, conpassword=conpassword, patient_address=address,contact_number=contact,bdate=bdate)

        if password == conpassword:
            if Patient.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            if Patient.objects.filter(nid = nid).exists():
                messages.info(request,'NID already exist')
                return redirect('register')
                
            else:
                reg_user = User.objects.create_user(username=firstname,email=email,password=password)
                reg_user.save()
                patient.save()

                group = Group.objects.get(name='patient')
                reg_user.groups.add(group)

                messages.info(request,'User created')

                return redirect('login')
            
        else:
        	messages.info(request,'Password not matching')
        	return redirect('register')
    return render(request,"register.html")


def doctor_reg(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nid = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        address = request.POST['address']
        contact = request.POST['contact']
        bdate = request.POST['date']
        
        doctor = Doctor(first_name=firstname, last_name=lastname, nid=nid, email=email, password=password, conpassword=conpassword, patient_address=address,contact_number=contact,bdate=bdate)

        if password == conpassword:
            if Doctor.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('doctor_reg')
            if Doctor.objects.filter(nid = nid).exists():
                messages.info(request,'NID already exist')
                return redirect('doctor_reg')
                
            else:
                reg_user = User.objects.create_user(username=firstname,email=email,password=password)
                reg_user.save()
                doctor.save()

                group = Group.objects.get(name='doctor')
                reg_user.groups.add(group)

                messages.info(request,'User created')

                return redirect('login')
            
        else:
            messages.info(request,'Password not matching')
            return redirect('doctor_reg')
    return render(request,"doctor_registration.html")



def pharmacy_reg(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pharmacy_reg_no = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        address = request.POST['address']
        contact = request.POST['contact']
        bdate = request.POST['date']
        
        pharmacy = Pharmacy(first_name=firstname, last_name=lastname, pharmacy_reg_no=pharmacy_reg_no, email=email, password=password, conpassword=conpassword, patient_address=address,contact_number=contact,bdate=bdate)

        if password == conpassword:
            if Pharmacy.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('pharmacy_reg')
            if Pharmacy.objects.filter(pharmacy_reg_no = pharmacy_reg_no).exists():
                messages.info(request,'Registration number already exist')
                return redirect('pharmacy_reg')
                
            else:
                reg_user = User.objects.create_user(username=firstname,email=email,password=password)
                reg_user.save()
                pharmacy.save()

                group = Group.objects.get(name='pharmacy')
                reg_user.groups.add(group)

                messages.info(request,'User created')

                return redirect('login')
            
        else:
            messages.info(request,'Password not matching')
            return redirect('pharmacy_reg')
    return render(request,"pharmacy_reg.html")


def logout(request):
    auth.logout(request)
    return redirect('login')






