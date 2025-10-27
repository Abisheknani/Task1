from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Dummy credentials (you can connect to Django auth later)
        if username == 'admin' and password == '1234':
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request,'login.html')

def index_view(request):
    return render(request, 'index.html')

# Create your views here.
