from django.shortcuts import render

# Create your views here.

def register_view(request):
    template_view = "login.html"
    return render(request,template_name=template_view)