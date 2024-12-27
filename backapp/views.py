from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout

def loginpage(request):
    
    if request.method == "POST":
         print(request.POST)
         user=authenticate(username=request.POST['username'],password=request.POST['password'])
         print(user)
         if user is not None:
              login(request,user)
              return redirect('/frontapp/main/')
         else:
              context={'error':" **invalid username or password"}
              return render(request,'backapp/login.html',context)
         
    return render(request,'backapp/login.html')

def logoutpage(request):
     logout(request)
     return render(request,'backapp/login.html') 
def signup(request):
      context={'error':""}
      if request.method=='POST':
           new_user=User.objects.filter(username=request.POST['username'])
           
           if len(new_user) > 0:
               context= {'new_user':"username already exists"}
             
               
               return render(request,'backapp/signup.html',context) 
            
           else:
                name=User(username=request.POST['username'],
                     first_name=request.POST['first_name'],
                     last_name=request.POST['last_name'],
                     age=request.POST['Age']
                     )
                name.set_password( request.POST['password'])
                name.save()
           return redirect('/backapp/login')
      return render(request,'backapp/signup.html')
          
          