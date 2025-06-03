from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html') 

def color_view(request):
    return render(request, 'colores.html') 

def typography_view(request):
    return render(request, 'typography.html') 

def feather_icons(request):
    return render(request, 'feather-icons.html')

def sample_page(request):
    return render(request, 'sample-page.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
    
