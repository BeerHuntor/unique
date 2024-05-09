from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from authentication.forms import LoginModalForm

# Create your views here.
def index_view (request): 
    return render(request, 'authentication/index.html')

def login_modal (request):
    if request.method == 'POST':
        form = LoginModalForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')
            else:
                print("login invalid")

    else: 
        form = LoginModalForm()
    return render(request, 'authentication/login_form.html', {'form': form })
