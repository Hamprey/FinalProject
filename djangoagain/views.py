from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from djangoagain.form import SignUpForm, LoginForm
from .form import ContactForm


def User_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                # Handle invalid login credentials
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'User_login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    # Your view logic goes here
    return render(request, 'success.html')


def home(request):
    return render(request, "index.html", )


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')
