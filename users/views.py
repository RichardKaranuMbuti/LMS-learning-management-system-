from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
from .models import UserDetails


# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')  # Replace 'home' with the appropriate URL name for your landing page
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})


# Home View
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')  # Return a rendered template
    else:
        # Handle other request methods if needed
        return HttpResponse("This is the home page")  # Return a valid response



# Login View

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the username is email or phone number
            user = None
            try:
                # Try to get the user by email
                user = UserDetails.objects.get(email=username).user
            except UserDetails.DoesNotExist:
                try:
                    # Try to get the user by phone number
                    user = UserDetails.objects.get(phone=username).user
                except UserDetails.DoesNotExist:
                    pass

            if user is not None:
                # Authenticate the user
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    # Login the user
                    # login(request, user)
                    return render(request, 'home.html')

        # Invalid form or authentication failed
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

