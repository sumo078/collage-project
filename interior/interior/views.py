from django.http import HttpResponse
from django.shortcuts import render,redirect
# from loginpage.models import userdetail
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from loginpage.models import signdetail
from loginpage.models import feedback
from loginpage.models import contactdetail
from loginpage.models import registerdetail
from loginpage.models import bookingdetail
from django.contrib.auth import authenticate,login
from django.contrib.auth import login,logout
from django.contrib import messages
from django.conf import settings
# from customer.models import contact
# from customer import models
# def loginview(request):
#     if request.method=="POST":
#         Email=request.POST.get('Email')
#         Password=request.POST.get('Password')
#         print(Email,Password)
#         User=authenticate(request,Email=Email,Password=Password)
        
#         if User is not None:
#          login(request,User)
#          return redirect('home')
#         else:
#             return HttpResponse("is not correct!!!")
            # return redirect("login")
    # return render(request,"signinlogin.html")
# def submitform(request):
#     return HttpResponse(request)


# for data save in database
# def saveEinquery(request):
#     n=''
#     if request.method=="POST":
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         user=authenticate(request,email=email,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse("email is not correct!!!")
#         # data=userdetail(email=email,password=password)
#         # data.save()
#         # return redirect('ogin')
        
    
#     return render(request,"signinlogin.html")
def book(request):
    return render(request,'booking2.html')
# def bookdata(request):

    # if request.method=='POST':
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     phone=request.POST.get('phone')
    #     appoint=request.POST.get('appointmentDate')
    #     service=request.POST.get('services')
    #     timeslot=request.POST.get('timeSlot')
    #     d=bookingdetail(name=name,email=email,phone=phone,appointmentDate=appoint,services=service,timeSlot=timeslot)
    #     d.save()
    return render(request,'booking2.html')
def bookdata(request):
     if request.method=='POST':
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         appoint=request.POST.get('appointmentDate')
         service=request.POST.get('services')
         timeslot=request.POST.get('timeSlot')
         d=bookingdetail(name=name,email=email,phone=phone,appointmentDate=appoint,services=service,timeSlot=timeslot)
         d.save()
        #  return redirect('thanku')
        #  return redirect()
     return render(request,'booking2.html')
def logout1(request):
    logout(request)
    return redirect('loginview')
    
def thank(request):
    return render(request,'thankyou.html')
def contact(request):
   return render(request,'samplecontact.html')

def pillow(request):
   return render(request,'cauch.html')

def interior(request):
   return render(request,'interior.html')


def contactinfo(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        text=request.POST.get('text')
        en=contactdetail(name=name,email=email,text=text)
        # print(name=name,email=email,text=text)
        en.save()
        # print(request,name=name,email=email,text=text)
        return redirect('thank')
    return render(request,"samplecontact.html")



def loginpage(request):
    
    if request.method=='POST':
        Email1=request.POST.get('Email')
        Pass1=request.POST.get('Password')
        # print(Email1,Pass1)
        User=authenticate(request,username=Email1,password=Pass1)
        if User is not None:
           login(request,User)
           return redirect('home')
        else:
            return HttpResponse("username and password is wrong")
           
    
    return render(request,"signinlogin.html")


def signEinquery(request):
    
    if request.method=='POST':
        Name=request.POST.get('Name')
        email1=request.POST.get('Email1')
        password2=request.POST.get('Password2')
        Cpassword=request.POST.get('Cpassword')
        print(Name,email1,password2,Cpassword)
        if password2!=Cpassword:
            return HttpResponse("YOU PASSWORD AND CONFORM PASSWORD ARE NOT SOME")
        else:
           my_user=User.objects.create_user(Name,email1,password2)
           my_user.save()
        return redirect('loginview')
        return HttpResponse("user has been created succesfully")
       
            
    return render(request,"signinlogin.html")



# check for errorneous inputs
# if 
    
def feedback1(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Feed=request.POST.get('feed')
        a=feedback(name=Name,email=Email,message=Feed)
        a.save()
        
        # print(name,email,message)
        # return HttpResponse("user has been created succesfully")
    return render(request,"service2.html")

def thanku(request):
    return render(request,"thanku.html")

def about(request):
    return render(request,"about-us.html")
def service(request):
    return render(request,"service2.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        s=registerdetail(name=name,email=email,pass1=password)
        s.save()
        
    return render(request,"service2.html")




# def contact(request):
#     return render(request,"contac.html")

# @login_required
def h(request):
    return render(request,"header.html")

def layOut(request):
    return render(request,"layout.html")

def portfolio(request):
    return render(request,"portfolio.html")

def furniture(request):
    return render(request,"FURNITURE.html")


def chair(request):
    return render(request,"chairs.html")

def table(request):
    return render(request,"table.html")

def sofa(request):
    return render(request,"sofa.html")


def curtain(request):
    return render(request,"curtains.html")


def do(request):
    return render(request,"doors.html")


def win(request):
    return render(request,"window.html")

def bed(request):
    return render(request,"bed.html")


def all(request):
    return render(request,"allcategories.html")

def the(request):
    return render(request,"theinside.html")



def magzine(request):
    return render(request,"magzine.html")

def bedroom(request):
    return render(request,"badroom.html")

def kichen(request):
    return render(request,"kichen.html")


def light(request):
    return render(request,"lighting.html")

def living(request):
    return render(request,"living.html")








