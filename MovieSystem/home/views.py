
#from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
# views.py (add to the top with other imports)
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def series(request):
    return render(request, "series.html")

@login_required(login_url='login')
def docu(request):
    return render(request, "documentery.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect after login.
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        contact = request.POST.get('contact')  # Note: The default User model doesn’t include this.
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create a new user using Django's built-in create_user method.
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=full_name
            )
            user.save()
            messages.success(request, "Signup successful. Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
    
    # GET request will simply render the sign-up form.
    return render(request, 'signup.html')






# from django.shortcuts import render,HttpResponse

# # Create your views here.
# def index(request):
#     # context={
#     #     "Variable1" : "This is Shaunak",
#     #     "Variable2" : "This is my first project" 
#     # }
#     return render(request,'index.html')
#     #return render(request,'h2.html',context)
#     # return HttpResponse("This is First Django page")

# def series(request):
#     #return HttpResponse("about this ___________is First Django page")
#     return render(request,"series.html")

# def docu(request):
#     #return HttpResponse("Contact_______is First Django page")
#     return render(request,"documentery.html")

# def login(request):
#     #return HttpResponse("Contact_______is First Django page")
#     return render(request,"login.html")

# def signup(request):
#     #return HttpResponse("Contact_______is First Django page")
#     return render(request,"signup.html")


